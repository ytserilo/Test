from .models import UserStatistic, CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id", "first_name", "last_name", "email", "gender", "ip_address"]


class UserStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistic
        fields = ["date", "page_views", "clicks"]
