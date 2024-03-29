"""
URL configuration for NewProjs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from addbd.views import PassesAPIView, EmailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/passeslist/', PassesAPIView.as_view(), name='post_passes'),
    path('api/v1/passeslist/<int:pk>/', PassesAPIView.as_view(), name='get_passes_pk'),
    path('api/v1/passeslist/patch/<int:pk>/', PassesAPIView.as_view(), name='path_passes_pk'),
    path('api/v1/passeslist/user_email/<str:email>/', EmailAPIView.as_view(), name='get_passes_email'),
]
