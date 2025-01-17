from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=30, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
