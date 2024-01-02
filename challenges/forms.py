from django import forms 

from .models import Answer, Question, UserAnswer

# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ['text', 'is_correct']
#         widgets = {
#             'is_correct': forms.RadioSelect(),
#         }

class QuizForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        # fields = ['selected_answer']
        fields = "__all__"
        widgets = {
            'selected_answer': forms.RadioSelect(),
        }
