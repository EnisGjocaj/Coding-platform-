from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PriceForCoursesModel(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.price
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)


class RegistrationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(max_length=125)
    phone_number = models.CharField(max_length=100, blank=True)
    students_interst = models.TextField()
    from_where = models.TextField(blank=True, null=True)
    user_bio = models.TextField(blank=True, null=True)
