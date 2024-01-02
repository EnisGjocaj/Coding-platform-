from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.index, name="index"),
    # path('inbox/', views.inbox, name="inbox"),
    path('users/', views.users, name="users"),
    path('profile/showcase/', views.profile_showcase, name="profile_showcase"),
    path('profile/modify/', views.profile_modify, name="profile_modify"),
    path('salesForm/', views.sales, name="sales"),
    path('salesData/', views.salesData, name="salesData"),
    path('labsForm/', views.labsForm, name="labsForm"),
    path('labsData/', views.labsData, name="labsData"),
    path('coursesForm/', views.coursesForm, name="coursesForm"),
    path('coursesData/', views.coursesData, name="coursesData"),
    
    path('priceForm/', views.priceForm, name="priceForm"),
    path('priceData/', views.priceData, name="priceData"),

    path('newQuizForm/', views.newQuizForm, name="newQuizForm"),
    path('quizData/', views.quizData, name="quizData"),

    path('questionForm/', views.questionForm, name="questionForm"),
    path('questionData/', views.questionData, name="questionData"),

    path('answerForm/', views.answerForm, name="answerForm"),
    path('answerData/', views.answerData, name="answerData"),

    path('newRegistrationForm/', views.registrationForm, name="registrationForm"),
    path('registrationData/', views.registrationData, name="registrationData"),

    path('userAnswersData/', views.userAnswerData, name="userAnswerData"),

    path('labScoreData/', views.labScoreData, name="labScoreData"),

    path('categoryLabForm/', views.categoryLabForm, name="categoryLabForm"),
    path('categoryLabData/', views.categoryLabData, name="categoryLabData"),

    path('categoryCourseForm/', views.categoryCourseForm, name="categoryCourseForm"),
    path('categoryCourseData/', views.categoryCourseData, name="categoryCourseData"),

    path('postsData/', views.postsData, name="postsData"),

    path('labTypeForm/', views.labTypeForm, name="labTypeForm"),
    path('labTypeData/', views.labTypeData, name="labTypeData"),

    path('blogPosts/', views.PostList.as_view(), name="blog"),
	path('addPost/', views.add_post, name="add"),
	path('<slug:slug>/', views.DetailedView.as_view(), name="detail"),
	path('<int:pk>/delete/', views.delete_post, name="delete"),
]