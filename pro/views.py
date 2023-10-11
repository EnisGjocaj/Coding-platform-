from django.shortcuts import render

# Create your views here.
def pro(request):
    return render(request, 'pro/pro.html')