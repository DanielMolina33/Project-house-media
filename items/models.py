# Items model

# Django
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    picture = models.JSONField(blank=True)
    tags = models.CharField(max_length=200)
    classification = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)




