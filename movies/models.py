from django.db import models
from django.conf import settings

class Movie(models.Model):
    poster_path = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    genre_ids = models.CharField()
    id = models.CharField()
    title = models.CharField(max_length=100)
    popularity = models.CharField()
    vote_count = models.CharField()
    vote_average = models.CharField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

