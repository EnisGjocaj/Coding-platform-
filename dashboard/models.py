from django.db import models

from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.models import AbstractUser



class Post(models.Model):

	STATUS = (
        (0, "Draft"),
        (1, "Published"),
    )
	
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True, max_length=255)
	content = models.TextField()
	author = models.ForeignKey(User, related_name="dashboard_user", on_delete=models.CASCADE)
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


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

#     def __str__(self):
#         return self.user.username

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	is_agent = models.BooleanField(default=False)
	bio = models.TextField(blank=True)
	review = models.TextField(blank=True)
	profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
        
		super().save(*args, **kwargs)

        
		agent_profile, created = AgentProfile.objects.get_or_create(user=self.user)

		agent_profile.is_agent = self.is_agent
		agent_profile.save()


class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class SalesData(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	percentage_value = models.IntegerField()
	# selected_flight_sale = models.ForeignKey(AirlineFlight, on_delete=models.CASCADE)

class VisitorCounter(models.Model):
    count = models.IntegerField(default=0)