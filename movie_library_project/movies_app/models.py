from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    runtime = models.IntegerField()
    release_date = models.DateField()
    likes = models.IntegerField()
    watch_count = models.IntegerField()

class MovieReview(models.Model):
    text = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class MovieRating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)