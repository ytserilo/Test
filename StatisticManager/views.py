from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .utils import UserManager
import json

# Create your views here.
class Search(View, UserManager):
    def get(self, request):
        if request.is_ajax():
            search_query = request.GET.get("search_query")
            page = request.GET.get("page")

            paginator = self.search(search_query, page)
            return JsonResponse(paginator)
        else:
            return render(request, "search.html")

class GetUserInfo(View, UserManager):
    def get(self, request, id):
        if request.is_ajax():
            data = request.GET.get("data")
            data = json.loads(data)

            user_info = self.get_user(data, id)
            
            try:
                error = user_info["id-error"]
                return JsonResponse(error)
            except:
                return JsonResponse({"user_info": user_info})
        else:
            return render(request, "user_info.html")
