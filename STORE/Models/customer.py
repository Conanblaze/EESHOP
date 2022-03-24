from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(max_length=10)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=500)
    add1 = models.CharField(max_length=100, null=True)
    add2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zip = models.IntegerField(max_length=6, null=True)
