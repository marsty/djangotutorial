from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.Serializer):
    """
    用户序列化类
    """
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
