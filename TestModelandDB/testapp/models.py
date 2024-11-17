from django.db import models

# Create your models here.
class Userdb(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    passwrd = models.CharField(max_length=10)
    role = models.CharField(max_length=1)

class customer(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=2)
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)