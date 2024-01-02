from django.urls import path
from . import views

app_name = "challenges"

urlpatterns = [
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]