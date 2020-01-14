from .models import UserStatistic, CustomUser
from django.core.paginator import Paginator
from .serializers import UserStatisticSerializer, UserSerializer
from dateutil import parser
import datetime, json

class UserManager:
    def search(self, search_query, page):
        first_group = CustomUser.objects.filter(first_name__contains=search_query)
        second_group = CustomUser.objects.filter(last_name__contains=search_query)

        result = []

        for f in first_group:
            result.append(f)
        for s in second_group:
            result.append(s)
        paginator = custom_paginator(result, page)
        return paginator

    def get_user(self, filter_data, id):
        user_info = None
        last_data = None
        start_date = None
        fin_date = None

        try:
            user = CustomUser.objects.get(user_id=id)
            user_info = UserStatistic.objects.filter(user=user)
            user_info = user_info.order_by("date")
        except:
            return {"id-error": "Такого пользователя не существует"}
        try:
            start_date = parser.parse(filter_data["start-date"])
            user_info = user_info.filter(date__gte=start_date)
        except:
            pass
        try:
            fin_date = parser.parse(filter_data["fin-date"])
            user_info = user_info.filter(date__lte=fin_date)
        except:
            pass
        json_info = []
        user_info = user_info.order_by("date")
        for data in user_info:
            json_info.append(UserStatisticSerializer(data).data)

        count = (fin_date-start_date).days - len(json_info)
        last_date = None
        try:
            last_date = json_info[-1]["date"]
            last_date = parser.parse(last_date)
        except:
            last_date = start_date
        for i in range(count):
            append_dict = {
                "date": str(last_date + datetime.timedelta(days=i)),
                "clicks": 0,
                "page_views": 0,
            }
            json_info.append(append_dict)

        return json_info

def custom_paginator(objects, page):
    try:
        page = int(page)
    except:
        page = 0

    max_pages = len(objects) // 50
    if len(objects) % 50 != 0:
        max_pages += 1

    if page < 1:
        page = 1
    elif max_pages < page:
        page = max_pages

    users = []

    for user in objects[(page-1)*50: (page-1)*50+50]:
        data = UserSerializer(user)
        users.append(data.data)

    return {
        "max_pages": max_pages,
        "current_page": page,
        "users": users
    }
