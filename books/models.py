from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class Book(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.CharField(max_length=500,blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    genre = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('book-home')

