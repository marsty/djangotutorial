import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()

class UsertFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username",lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']