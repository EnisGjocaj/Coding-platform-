from django.shortcuts import render

from . models import Category, VideoModel

# Create your views here.
def labs(request):
    lessons = VideoModel.objects.all()[0:12]

    return render(request, "labs/labsMain.html", {
        'lessons': lessons,
    })