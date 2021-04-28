from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    runtime = models.IntegerField()
    release_date = models.DateField()
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)

class MovieReview(models.Model):
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
