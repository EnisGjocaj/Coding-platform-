from django.urls import path
from . import views 

app_name = "blog"

urlpatterns = [
	path('', views.PostList.as_view(), name="blog"),
	path('addPost/', views.add_post, name="add"),
	path('<slug:slug>/', views.DetailedView.as_view(), name="detail"),
	path('<int:pk>/delete/', views.delete_post, name="delete"),
]