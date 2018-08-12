from django.contrib.auth.models import Group
from .serializer import  GroupsSerializer
from rest_framework import viewsets
from .filters import GroupFilter
# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupsSerializer
    filter_class = GroupFilter
    filter_fields = ("name", )