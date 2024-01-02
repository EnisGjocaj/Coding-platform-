from django.shortcuts import render, get_object_or_404

from . models import Category, VideoModel

from challenges.models import Quiz

from django.views import View

from django.http import JsonResponse


def labs(request):
    lessons = VideoModel.objects.all()[0:12]

    return render(request, "labs/labsMain.html", {
        'lessons': lessons,
    })


# def lab_detail(request, lab_id):
#     lab = get_object_or_404(VideoModel, pk=lab_id)

#     return render(request, "labs/lab_detail.html", {'lab': lab})

class LabDetailView(View):
    template_name_base = 'labs/lab_detail.html'
    template_name_type1 = 'labs/html_lab.html'
    template_name_CSStype = 'labs/css_lab.html'

    def get(self, request, lab_id):
        video = get_object_or_404(VideoModel, id=lab_id)
        print(video)
        lab_type = video.labs_type.lab_type if video.labs_type else None

        if lab_type == 'Type1':
            template_name = self.template_name_type1
        elif lab_type == "CSStype":
            template_name = self.template_name_CSStype
        else:
            template_name = self.template_name_base

        context = {'lab': video}
        return render(request, template_name, context)



def like_lab(request):
    if request.method == 'POST':
        lab_id = request.POST.get('lab_id')
        lab = VideoModel.objects.get(id=lab_id)

        user = request.user
        if user.is_authenticated:
            if user in lab.likes.all():
                lab.likes.remove(user)
                is_liked = False
            else:
                lab.likes.add(user)
                is_liked = True

            likes_count = lab.likes.count()
            return JsonResponse({'likes_count': likes_count, 'is_liked': is_liked})
    
    return JsonResponse({'error': 'Invalid request'})