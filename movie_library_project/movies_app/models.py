from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='')
    runtime = models.IntegerField()
    release_date = models.DateField()
    likes = models.IntegerField(default=0)
    watch_count = models.IntegerField(default=0)
    image_url = models.CharField(max_length=500, default='https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg')

class MovieReview(models.Model):
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
