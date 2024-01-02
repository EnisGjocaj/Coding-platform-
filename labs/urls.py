from django.urls import path

from . import views

from .views import LabDetailView

app_name = 'labs'

urlpatterns = [
	path('', views.labs, name="labs"),
	# path('lab/<int:lab_id>/', views.lab_detail, name='lab_detail'),
	path('<int:lab_id>/', LabDetailView.as_view(), name='lab_detail'),
	path('like_lab/', views.like_lab, name='like_lab'),
]