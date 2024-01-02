from django import forms
from . models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status',)
    
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Titulli i postimit',
        'class': 'text-black w-5/6 py-4 px-6 rounded-xl max-[375px]:w-full'
    }), label=False)

    slug = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Slug',
        'class': 'text-black w-5/6 py-4 px-6 rounded-xl max-[375px]:w-full'
    }), label=False)

    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Shkruani përmbajtjen këtu',
        'class': 'text-black w-5/6 py-4 px-6 rounded-xl max-[375px]:w-full',
        'rows': 5,
    }), label=False)

    status = forms.ChoiceField(choices=Post.STATUS, widget=forms.Select(attrs={
        'class': 'my-2 mb-8 text-black w-1/12 py-4 px-6 rounded-xl max-[1025px]:w-1/2',
    }), label=False)


    