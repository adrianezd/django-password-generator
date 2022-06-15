from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class UserCreado(models.Model):
    username = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)


