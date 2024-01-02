from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
	path('', views.index, name="index"),
	path('signup/', views.signup, name="signup"),
	path('login/', auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
	path('register/', views.register, name="register"),
	path('success_registration/', views.success_registration, name="success_registration"),
]
