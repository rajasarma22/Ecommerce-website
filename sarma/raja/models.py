from django.db import models

# Create your models here.

class mohan(models.Model):
    fistname =models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    Contact = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
