from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import SignupForm 

def index(request):
	return render(request, 'core/index.html')

def signup(request):

	if request.method == "POST":
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:
		form = SignupForm()

	return render(request, 'core/signup.html', {
		'form': form,
	})
