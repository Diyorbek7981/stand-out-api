from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("telegram_id", "first_name", "user_name", "age", "certificate", "phone_number", "is_channel_member", "is_registered", "language")