from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(max_length=300)
    content = models.TextField(default='Co chcesz napisać?')
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })


class Shop(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    seats = models.CharField(max_length=10)
    doors = models.CharField(max_length=10)
    petrol = models.CharField(max_length=10)

    ac = models.BooleanField(default=True)
    gridbox = models.CharField(max_length=20)
    car_img = models.ImageField(blank=True)

    def __str__(self):
        return self.name
