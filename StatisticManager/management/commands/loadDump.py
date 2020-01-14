from django.core.management.base import BaseCommand
from StatisticManager.models import CustomUser, UserStatistic
from dateutil import parser
import json


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfull'))

    def run(self):
        self.load_users()
        self.load_statistic()

    def load_statistic(self):
        data = self.open_file("users_statistic.json")
        for info in data:
            user = CustomUser.objects.get(id=info["user_id"])
            UserStatistic.objects.create(
                user=user,
                date=parser.parse(info['date']),
                page_views=info["page_views"],
                clicks=info["clicks"],
            )

    def load_users(self):
        data = self.open_file("users.json")
        for user in data:
            CustomUser.objects.update_or_create(
                user_id=user["id"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                email=user["email"],
                gender=user["gender"],
                ip_address=user["ip_address"]
            )

    def open_file(self, file_name):
        with open(file_name, "r") as file:
            data = json.loads(file.read())
        return data
