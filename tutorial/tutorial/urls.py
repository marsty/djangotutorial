"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from rest_framework.routers import  DefaultRouter
from idcs.views import IdcViewset
from users.views import  UserViewset,DashboardStatus,UserInfoViewset
from cabinet.views import CabinetViewset
from rest_framework.documentation import  include_docs_urls
from manufacturer.views import ManufacturerViewset,ProductModelViewset
from servers.views import ServerAutoReportViewset,NetworkDeviceViewset,IPViewset,ServerViewset
route = DefaultRouter()
route.register("idcs", IdcViewset,base_name="idcs")
route.register("users",UserViewset,base_name="users")
route.register("cabinet",CabinetViewset,base_name="cabinet")
route.register("manufacturer",ManufacturerViewset,base_name="manufacturer")
route.register("ProductModel",ProductModelViewset,base_name="ProductModel")
route.register("ServerAutoReport",ServerAutoReportViewset,base_name="ServerAutoReport")
route.register("NetworkDevice",NetworkDeviceViewset,base_name="NetworkDevice")
route.register("IP",IPViewset,base_name="IP")
route.register("Server",ServerViewset,base_name="Server")
route.register("DashboardStatus",DashboardStatus,base_name="DashboardStatus")
route.register("userinfo",UserInfoViewset,base_name="UserInfo")
from rest_framework_jwt.views import obtain_jwt_token

from groups.route import group_router
route.registry.extend(group_router.registry)

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'docs/',include_docs_urls("practice")),
    url(r'^api-auth/',include('rest_framework.urls')),
    url(r'^api-token-auth/', obtain_jwt_token)
]

# from rest_framework.authtoken import views
# urlpatterns += [
#     url(r'^api-token-auth/', views.obtain_auth_token)
# ]
