from django import forms

from .models import UserProfile, SalesData, Post

from labs.models import VideoModel, Category

from courses.models import CourseModel
from courses.models import Category as CategoryForCourses

from core.models import PriceForCoursesModel

from challenges.models import Quiz, Question, Answer

from labs.models import Category as CategoryLab
from courses.models import Category as CategoryCourse

from labs.models import LabTypeModel

from core.models import RegistrationModel

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'review', 'profile_picture']

    bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Bio',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    review = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Mendimi juaj per faqen',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = ("percentage_value",)
    
    percentage_value = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'travelers_input w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Enter the number of travelers', 'id': 'travelers_input'}),
        label='Percentage value decrease:',
        initial=1,
        min_value=1, 
    )

    # selected_flight_sale = forms.ModelChoiceField(
    #     queryset=AirlineFlight.objects.all(),
    #     empty_label='Select Flight for sale:',
    #     required=True,
    #     widget=forms.Select(attrs={'class': ' w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
    #     label='Flight',
    #     initial=3, 
    # )


class CreateLabForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = "__all__"

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a category:',
        required=True,
        widget=forms.Select(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Category',
        initial=3, 
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-black w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
            'placeholder': 'Emri i kursit'
        })
    )

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Përmbajtja',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status',)
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title post',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    slug = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Slug',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Content',
        'class': 'resize-none w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'rows': 5,
    }), label=False)

    status = forms.ChoiceField(choices=Post.STATUS, widget=forms.Select(attrs={
        'class': 'w-1/4 my-2 mb-8 text-black py-4 px-6 rounded-xl border-2 border-gray-200 focus:outline-none focus:border-indigo-500 transition-colors max-[768px]:w-1/2',
    }), label=False)



class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"

    category = forms.ModelChoiceField(
        queryset=CategoryForCourses.objects.all(),
        empty_label='Select a category:',
        required=True,
        widget=forms.Select(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Category',
        initial=3, 
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'text-black w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
            'placeholder': 'Emri i kursit'
        })
    )

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Përmbajtja',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class PriceForm(forms.ModelForm):
    class Meta:
        model = PriceForCoursesModel
        fields = ('price',)
    
    price = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Enter the number of travelers', 'id': 'travelers_input'}),
        label='Price:',
        initial=1,
        min_value=1, 
    )

class NewQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Quiz title',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
    
    quiz = forms.ModelChoiceField(
        queryset=Quiz.objects.all(),
        empty_label='Select a quiz',
        required=True,
        widget=forms.Select(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Quiz',
        initial=3, 
    )

    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Pyetja',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
    
    question = forms.ModelChoiceField(
        queryset=Question.objects.all(),
        empty_label='Select the question',
        required=True,
        widget=forms.Select(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'id': 'category_input'}),
        label='Question',
        initial=3, 
    )

    text = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Pyetja',
        'rows': 5,
        'class': 'text-black resize-none w-full px-3 py-2 my-8 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    is_correct = forms.BooleanField(
        label='Is correct',
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'}),
        required=True
    )


class CategoryLabForm(forms.ModelForm):
    class Meta:
        model = CategoryLab
        fields = "__all__"
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Category name',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class CategoryCourseForm(forms.ModelForm):
    class Meta:
        model = CategoryCourse
        fields = "__all__"
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Category name',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class LabTypeForm(forms.ModelForm):
    class Meta:
        model = LabTypeModel
        fields = "__all__"
    
    lab_type = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Lab type',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = RegistrationModel
        fields = "__all__"
    
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'w-full py-2 px-4 text-black border-2 border-gray-300 rounded-xl my-2', 'placeholder': 'Enter the number of travelers', 'id': 'travelers_input'}),
        # label='Age:',
        initial=1,
        min_value=1, 
    )

    email = forms.CharField(widget=forms.EmailInput(attrs={
		'placeholder':'Your email', 
		'class': 'w-full py-2 px-4 rounded-xl text-black my-2 border-2 border-gray-300 rounded-xl'
	}))

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone number',
        'class': 'w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors'
    }), label=False)

    students_interst = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Students interests',
        'class': 'resize-none w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'rows': 5,
    }), label=False)

    from_where = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Students interests',
        'class': 'resize-none w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'rows': 5,
    }), label=False)

    user_bio = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Students interests',
        'class': 'resize-none w-full px-3 py-2 mb-4 border-2 border-gray-200 rounded-md focus:outline-none focus:border-indigo-500 transition-colors',
        'rows': 5,
    }), label=False)