from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .forms import SignupForm, RegistrationForm

from dashboard.models import SalesData

from . models import PriceForCoursesModel


def index(request):
	sales_data = SalesData.objects.values_list('percentage_value', flat=True).last()

	last_price = PriceForCoursesModel.objects.values_list('price', flat=True).order_by('-id').first()
	current_price = last_price - ( last_price * int(sales_data) / 100 )

	return render(request, 'core/index.html', {
		'sales_data': sales_data,
		'last_price': last_price,
		'current_price': current_price,
	})

def success_registration(request):
	return render(request, "core/success_registration.html")

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

@login_required
def register(request):

	if request.method == "POST":
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form_data_instance = form.save(commit=False)
			form_data_instance.user = request.user 
			form_data_instance.save()

			return redirect("core:success_registration")
	
	else:
		form = RegistrationForm()
	
	return render(request, "core/register.html", {
		'form': form,
	})
