from . import views
from django.conf.urls import url,include
from rest_framework.routers import  DefaultRouter

route = DefaultRouter()
route.register("idcs", views.IdcViewset_v7)
urlpatterns = [
    url(r'^', include(route.urls))
]