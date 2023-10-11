from django.shortcuts import render, get_object_or_404, redirect
from . models import Post
from django.views import generic
from django.contrib.auth.decorators import login_required

from .forms import PostForm

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_at')
	template_name = "blog/post.html"

class DetailedView(generic.DetailView):
	model = Post
	template_name = "blog/post_detail.html"
	slug_field = "slug"

@login_required
def delete_post(request, pk):
	post = get_object_or_404(Post, pk=pk, author=request.user)
	post.delete()

	return redirect('blog:blog')

@login_required
def add_post(request):
	
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect('blog:blog') 
	else:
		form = PostForm()

	return render(request, 'blog/postForm.html', {'form': form})