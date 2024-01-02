from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import RegistrationModel

class LoginForm(AuthenticationForm):
	
	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Your username', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder':'Your password', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


	username = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder':'Your username', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

	email = forms.CharField(widget=forms.EmailInput(attrs={
		'placeholder':'Your email', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder':'Your password', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))

	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder':'Repeat your password', 
		'class': 'w-full py-2 px-4 rounded-xl text-black'
	}))


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = RegistrationModel
		fields = ("full_name", "age", "email", "phone_number", "students_interst", "from_where", "user_bio",)
	

	full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-black w-full px-3 py-2 mb-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
            'placeholder': 'Emri dhe mbiemri'
        })
    )
	
	age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'text-black w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Mosha juaj'}),
        label='Mosha juaj',  
        min_value=5, 
    )

	email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-black w-full px-3 py-2 mb-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
            'placeholder': 'Email'
        })
    )

	phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-black w-full px-3 py-2 mb-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
            'placeholder': 'Phone Number(Opsionale)'
        })
    )

	students_interst = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Interesi juaj ne programim dhe cka ju pelqen rreth tij',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

	from_where = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Prej nga keni dëgjuar për ne ( Opsionale )',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

	user_bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Shkruani dica rreth vetes tuaj ( Opsionale )',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-2 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)