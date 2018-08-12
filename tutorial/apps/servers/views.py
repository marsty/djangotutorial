from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,mixins
from .models import *
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import  ServertFilter

class ServerAutoReportViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    """
    create:
        同步服务器记录
    update:
        更新服务器信息
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer


class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定服务器信息
    list:
        返回服务器列表
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("hostname",)
    filter_class = ServertFilter
    extra_perms_map = {
        'GET': ['servers.view_server'],}


class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定网卡信息
    list:
        返回网卡列表
    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    retrieve:
        返回指定IP信息
    list:
        返回IP列表
    """
    # update:
    #     更新IP信息
    # destroy:
    #     删除IP记录
    # create:
    #     创建IP记录
    # partial_update:
    #     更新部分记录
    #
    # """
    queryset = IP.objects.all()
    serializer_class = IPSerializer