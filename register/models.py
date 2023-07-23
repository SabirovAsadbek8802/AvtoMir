from django.db import models

class Accounts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.IntegerField()