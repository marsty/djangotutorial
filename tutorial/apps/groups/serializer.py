from rest_framework import serializers
from django.contrib.auth.models import Group

class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ["id","name"]

