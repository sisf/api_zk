"""zk_admn_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from zk_app import views

# urlpatterns = [
#     path('index/',views.index),
#     path('admin/', admin.site.urls),
#     path('api/fbv/', views.FBV_LIST),
#     path('api/fbv/<int:pk>', views.FBV_pk)
# ]
# from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# from musics import views
from zk_app.views import MusicViewSet, index

router = DefaultRouter()
router.register('music', MusicViewSet)

urlpatterns = [
    path('index/', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]