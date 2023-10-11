from django.urls import path

from . import views 

app_name = "pro"

urlpatterns = [
    path('', views.pro, name="pro"),
]