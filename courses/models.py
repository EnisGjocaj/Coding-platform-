from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class CourseModel(models.Model):
	image = models.ImageField(upload_to="app_images", blank=True, null=True)
	category = models.ForeignKey(Category, related_name="video", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	content = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

