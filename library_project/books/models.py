from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    written_year = models.IntegerField()
    birth_year = models.IntegerField()

    def __str__(self):
        return self.title


