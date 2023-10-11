from django.shortcuts import render

from . models import Category, CourseModel

# Create your views here.
def courses(request):
    courses = CourseModel.objects.all()[0:12]

    return render(request, "courses/coursesMain.html", {
        'courses': courses,
    })
