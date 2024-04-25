from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=20,unique=True,null=False)
    password = models.CharField(max_length=20,null=False)
    email = models.EmailField(unique=True)

