from django.db import models
from django.contrib.auth.models import User

from challenges.models import Quiz

# Create your models here.
class LabTypeModel(models.Model):
    lab_type = models.CharField(max_length=20)

    def __str__(self):
        return self.lab_type


class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class VideoModel(models.Model):
	image = models.ImageField(upload_to="app_images", blank=True, null=True)
	category = models.ForeignKey(Category, related_name="video", on_delete=models.CASCADE)
	labs_type = models.ForeignKey(LabTypeModel, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	content = models.TextField(blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='video_likes', blank=True)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

	def like_count(self):
		return self.likes.count()

	def liked_users(self):
		return [user.username for user in self.likes.all()]