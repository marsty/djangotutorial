from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Manufacturer,ProductModel
from .serializers import  ManufacturerSerializer,ProductModelSerializer
class ManufacturerViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定厂商信息
    list:
        返回厂商列表
    update:
        更新厂商信息
    destroy:
        删除厂商记录
    create:
        创建厂商记录
    partial_update:
        更新部分记录

    """
    queryset =  Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定型号信息
    list:
        返回型号列表
    update:
        更新型号信息
    destroy:
        删除型号记录
    create:
        创建型号记录
    partial_update:
        更新部分记录

    """
    queryset =  ProductModel.objects.all()
    serializer_class = ProductModelSerializer
