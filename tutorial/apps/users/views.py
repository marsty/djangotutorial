from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,pagination
from django.contrib.auth.models import User
from .pagination import  Pagination
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.pagination import  PageNumberPagination
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from .filters import UsertFilter
# from django_filters.rest_framework import DjangoFilterBackend
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
    filter_fields = ("username",)
    filter_class = UsertFilter
    # permission_classes = (DjangoModelPermissions,)
 #   pagination_class = Pagination
 #    def get_queryset(self):
 #        queryset = super(UserViewset,self).get_queryset()
 #        username = self.request.query_params.get("username",None)
 #        if username:
 #            queryset = queryset.filter(username__icontains = username)
 #
 #        return queryset
 #    def get_queryset(self):
 #        queryset = super(UserViewset,self).get_queryset()
 #        username = self.request.query_params.get("username",None)
 #        if username:
 #            queryset = queryset.filter(username__icontains = username)
 #        return queryset

import requests,json
class DashboardStatus(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self,request,*args,**kwargs):
        url = 'http://mobile.weather.com.cn/data/sk/101010100.html?_=1381891661455'
        data = requests.get(url,stream=True)
        cc = json.loads(data.text)
        return Response(cc)

from rest_framework import  response
class UserInfoViewset(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self,request,*args,**kwargs):
            data = {
                "username": 'admin',
                "name": 'tianyu'
                 }
            return response.Response(data)