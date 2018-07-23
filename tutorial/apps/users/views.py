from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,pagination
from django.contrib.auth.models import User
from .pagination import  Pagination
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.pagination import  PageNumberPagination
User = get_user_model()

class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    get:
        list
        get
    create
    update
    delete
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
 #   pagination_class = Pagination
