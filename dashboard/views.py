from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.views import generic

from django.contrib.auth.models import User

from django.contrib.auth.decorators import user_passes_test

from .models import UserProfile, SalesData, Post, VisitorCounter

from .forms import SalesDataForm, UserProfileForm, CreateLabForm, PostForm, CreateCourseForm, PriceForm, NewQuizForm, CategoryLabForm, CategoryCourseForm, RegistrationForm

from labs.models import VideoModel

from courses.models import CourseModel

from challenges.models import LabScore, Quiz

from core.models import PriceForCoursesModel

from challenges.models import Quiz, Question, Answer, UserAnswer, LabScore

from labs.models import Category as CategoryLab
from courses.models import Category as CategoryCourse

from blog.models import Post

from core.models import RegistrationModel

from django.utils import timezone
from datetime import timedelta

from challenges.models import LabScore

def index(request):

    #code for listing the highest scores START
    top_lab_scores = LabScore.objects.order_by('-score')[:5]
    #NED

    #code to track the number of users that have visited the site START
    counter_instance, created = VisitorCounter.objects.get_or_create(pk=1)

    counter_instance.count += 1
    counter_instance.save()
    #END

    registrated_users = RegistrationModel.objects.all()
    total_users = RegistrationModel.objects.count()

    last_month_start = timezone.now() - timedelta(days=30)

    users_last_month = RegistrationModel.objects.filter(
        user__date_joined__gte=last_month_start
    )

    total_users_last_month = users_last_month.count()

    return render(request, "dashboard/index.html", {
        'total_users': total_users,
        'total_users_last_month': total_users_last_month,
        'visitor_count': counter_instance.count,
        'top_lab_scores': top_lab_scores, 
    })



@login_required
def profile_showcase(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    user = request.user

    # high_scores = LabScore.objects.filter(user=request.user).select_related('quiz')
    high_scores = LabScore.objects.filter(user=request.user).select_related('quiz')

    high_scores_data = []
    overall_best_score = 0
    overall_best_lab = None

    for lab_score in high_scores:
        high_scores_data.append({
            'quiz_title': lab_score.quiz.title,
            'score': lab_score.score,
            'attempts': lab_score.attempts,
        })

        # Update overall best score and lab
        if lab_score.score > overall_best_score:
            overall_best_score = lab_score.score
            overall_best_lab = lab_score.quiz.title

    # high_scores_data = []
    # for lab_score in high_scores:
    #     high_scores_data.append({
    #         'quiz_title': lab_score.quiz.title,
    #         'score': lab_score.score,
    #     })

    return render(request, 'dashboard/profile_showcase.html', {
        'user_profile': user_profile, 
        # 'high_scores_data': high_scores_data,
        'high_scores_data': high_scores_data,
        'overall_best_score': overall_best_score,
        'overall_best_lab': overall_best_lab,
    })

@login_required
def profile_modify(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard:profile_showcase')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'dashboard/profile_modify.html', {
        'form': form, 
    })


def sales(request):
    if request.method == "POST":
        form = SalesDataForm(request.POST)

        if form.is_valid():
            sales_data_instance = form.save(commit=False)
            sales_data_instance.user = request.user 
            sales_data_instance.save()
    
    else:
        form = SalesDataForm()
    
    return render(request, "dashboard/SalesForm.html", {
        'form': form,
    })

def salesData(request):
    sales_data = SalesData.objects.all()

    return render(request, "dashboard/SalesData.html", {
        'sales_data': sales_data,
    })


def labsForm(request):
    if request.method == "POST":
        form = CreateLabForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = CreateLabForm()
    
    return render(request, "dashboard/labsForm.html", {
        'form':form,
    })


def labsData(request):
    labs_data = VideoModel.objects.all()

    return render(request, "dashboard/labsData.html", {
        'labs_data': labs_data,
    })


def coursesForm(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = CreateCourseForm()
    
    return render(request, "dashboard/coursesForm.html", {
        'form':form,
    })


def coursesData(request):
    courses_data = CourseModel.objects.all()

    return render(request, "dashboard/coursesData.html", {
        'courses_data': courses_data,
    })


def priceForm(request):
    if request.method == "POST":
        form = PriceForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = PriceForm()
    
    return render(request, "dashboard/priceForm.html", {
        'form':form,
    })


def priceData(request):
    price_data = PriceForCoursesModel.objects.all()

    return render(request, "dashboard/priceData.html", {
        'price_data': price_data,
    })


def newQuizForm(request):
    if request.method == "POST":
        form = NewQuizForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = NewQuizForm()
    
    return render(request, "dashboard/newQuizForm.html", {
        'form':form,
    })


def quizData(request):
    quiz_data = Quiz.objects.all()

    return render(request, "dashboard/quizData.html", {
        'quiz_data': quiz_data,
    })


def questionForm(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = QuestionForm()
    
    return render(request, "dashboard/questionForm.html", {
        'form':form,
    })


def questionData(request):
    question_data = Question.objects.all()

    return render(request, "dashboard/questionData.html", {
        'question_data': question_data,
    })


def answerForm(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = AnswerForm()
    
    return render(request, "dashboard/answerForm.html", {
        'form':form,
    })


def answerData(request):
    answer_data = Answer.objects.all()

    return render(request, "dashboard/answerData.html", {
        'answer_data': answer_data,
    })

def userAnswerData(request):
    user_answer_data = UserAnswer.objects.all()

    return render(request, "dashboard/userAnswerData.html", {
        'user_answer_data': user_answer_data,
    })

def labScoreData(request):
    labScore_data = LabScore.objects.all()

    return render(request, "dashboard/labScoreData.html", {
        'labScore_data': labScore_data,
    })


def categoryLabForm(request):
    if request.method == "POST":
        form = CategoryLabForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CategoryLabForm()
    
    return render(request, "dashboard/categoryLabForm.html", {
        'form':form,
    })


def categoryLabData(request):
    category_lab_data = CategoryLab.objects.all()

    return render(request, "dashboard/categoryLabData.html", {
        'category_lab_data': category_lab_data,
    })


def categoryCourseForm(request):
    if request.method == "POST":
        form = CategoryCourseForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = CategoryCourseForm()
    
    return render(request, "dashboard/categoryCourseForm.html", {
        'form':form,
    })


def categoryCourseData(request):
    category_course_data = CategoryCourse.objects.all()

    return render(request, "dashboard/categoryCourseData.html", {
        'category_course_data': category_course_data,
    })

def postsData(request):
    posts_data = Post.objects.all()

    return render(request, "dashboard/postsData.html", {
        'posts_data': posts_data,
    })


def labTypeForm(request):
    if request.method == "POST":
        form = LabTypeForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = LabTypeForm()
    
    return render(request, "dashboard/labTypeForm.html", {
        'form':form,
    })


def labTypeData(request):
    lab_type_data = LabTypeModel.objects.all()

    return render(request, "dashboard/labTypeData.html", {
        'lab_type_data': lab_type_data,
    })


def registrationForm(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = RegistrationForm()
    
    return render(request, "dashboard/registrationForm.html", {
        'form':form,
    })


def registrationData(request):
    registration_data = RegistrationModel.objects.all()

    return render(request, "dashboard/registrationData.html", {
        'registration_data': registration_data,
    })

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_at')
	template_name = "dashboard/post.html"

class DetailedView(generic.DetailView):
	model = Post
	template_name = "dashboard/post_detail.html"
	slug_field = "slug"

@login_required
def delete_post(request, pk):
	post = get_object_or_404(Post, pk=pk, author=request.user)
	post.delete()

	return redirect('dashboard:blog')

@login_required
def add_post(request):
	
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect('dashboard:blog') 
	else:
		form = PostForm()

	return render(request, 'dashboard/postForm.html', {'form': form})


def users(request):
    users = User.objects.all()

    return render(request, "dashboard/users.html", {
        'users': users,
    })