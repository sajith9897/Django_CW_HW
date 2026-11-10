from django.db import models
# Create your models here.
class movie(models.Model):
    movie_name = models.CharField(max_length=100)
    release_year = models.IntegerField()