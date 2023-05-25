from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
