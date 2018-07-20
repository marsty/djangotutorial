from django.shortcuts import render
from .models import Idc
# Create your views here.
from django.http import HttpResponse
from .serializers import   IdcSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# ###########################版本一###############
# class JSONResponse(HttpResponse):
#      def __init__(self,data,**kwargs):
#          kwargs.setdefault('content_type','application/json')
#          content = JSONRenderer().render(data)
#          super(JSONResponse,self).__init__(content = content,**kwargs)
#
# def idc_list(request,*args,**kwargs):
#     if request.method == 'GET':
#       queryset = Idc.objects.all()
#       serializer = IdcSerializer(queryset,many=True)
#       return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parser(request)
#         serializer = IdcSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONRenderer(serializer.data)
#     return JSONResponse(status=404)
# def idc_detail(request,pk,*args,**kwargs):
#     try:
#         idc = Idc.objects.get(pk)
#     except idc.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = IdcSerializer(idc)
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         content = JSONParser().parser(request)
#         serializer = IdcSerializer(idc,data = content)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors,status=404)
#     elif request.method == 'DELETE':
#         idc.delete()
#         return JSONResponse(status=204)
# ###########################版本二###############
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
#
# @api_view(["GET","POST"])
# def idc_list_v2(request,*args,**kwargs):
#     if request.method == 'GET':
#         queryset = Idc.objects.all()
#         serializer = IdcSerializer(queryset,many =True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = IdcSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#     return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
#
# @api_view(["GET","PUT","DELETE"])
# def idc_detail_v2(request,pk,*args,**kwargs):
#     try:
#         idc = Idc.objects.get(pk)
#     except idc.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = IdcSerializer(idc,data = request.data)
#         return Response(serializer.data,status = status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = IdcSerializer(idc,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)
#     elif request.method == 'DELETE':
#         idc.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
# ###########################版本三###############
# from rest_framework.views import APIView
# from django.http import Http404
# from rest_framework.response import Response
#
# class IdcList(APIView):
#     def get(self,request):
#         queryset = Idc.objects.all()
#         serializer = IdcSerializer(queryset,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer =IdcSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
#
# class IdcDetail(APIView):
#     def get_object(self,pk):
#         try:
#             idc = Idc.objects.get(pk)
#         except idc.DoesNotExist:
#             raise Http404
#     def get(self,request,pk):
#         idc = self.get_object()
#         serializer = IdcSerializer(idc)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         idc = self.get_object(pk)
#         serializer = IdcSerializer(idc,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Respone(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#     def delete(self,request,pk):
#         idc = self.get_object(pk)
#         idc.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# ###########################版本四###############
from rest_framework import viewsets
class IdcViewset(viewsets.ModelViewSet):
    """
    retrieve:
        返回指定IDC信息
    list:
        返回IDC列表
    update:
        更新IDC信息
    destroy:
        删除IDC记录
    create:
        创建IDC记录
    partial_update:
        更新部分记录

    """
    queryset = Idc.objects.all()
    serializer_class =  IdcSerializer