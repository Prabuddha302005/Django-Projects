from django.db import models

# Create your models here.
class UserSignUpModel(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)