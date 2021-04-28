from django.contrib import admin
from .models import Movie, MovieReview, MovieRating
# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieReview)
admin.site.register(MovieRating)