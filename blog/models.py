from django.db import models

from django.contrib.auth.models import User

# STATUS=((0, "Draft"), (1, "Published"))

class Post(models.Model):

	STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )
	
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	author = models.ForeignKey(User, related_name="blog_user", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.IntegerField(choices=STATUS, default=0)

	def save(self, *args, **kwargs):
        
		if not self.slug:
			self.slug = slugify(self.title)
        
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return self.title
