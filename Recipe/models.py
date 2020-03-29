from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    time_required = models.CharField(max_length=15)
    description = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.title, self.author)
