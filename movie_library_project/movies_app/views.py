from django.shortcuts import render
from .models import Movie, MovieReview
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    all_movies = Movie.objects.all()
    context = {
        'all_movies': all_movies
    }
    return render(request, 'movies_app/index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    reviews = MovieReview.objects.filter(movie_id=movie_id).all()
    context ={
        'movie': movie,
        'reviews': reviews,
        'average_rating': False if len(reviews) == 0 else round(sum(review.rating for review in reviews) / len(reviews), 1)
    }
    return render(request, 'movies_app/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        genre = request.POST.get('genre')
        runtime = request.POST.get('runtime')
        release_date = request.POST.get('date')
        new_movie = Movie(title=name, genre=genre, runtime=runtime, release_date=release_date)
        new_movie.save()
        return HttpResponseRedirect(reverse('movies_app:index'))
    else:
        return render(request, 'movies_app/create.html')


def update(request, movie_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        runtime = request.POST.get('runtime')
        release_date = request.POST.get('date')
        Movie.objects.filter(pk=movie_id).update(title=title, genre=genre, runtime=runtime, release_date=release_date)
        return HttpResponseRedirect(reverse('movies_app:index'))
    else:
        movie = Movie.objects.get(pk=movie_id)
        context = {
            'movie': movie
        }
        return render(request, 'movies_app/update.html', context)


def delete(request, movie_id):
    Movie.objects.filter(pk=movie_id).delete()
    return HttpResponseRedirect(reverse('movies_app:index'))


def create_review(request, movie_id):
    review_text = request.POST.get('review_text')
    rating = int(request.POST.get('rating'))
    rating = 0 if rating < 0 else 10 if rating > 10 else rating
    movie_review = MovieReview(review_text=review_text, rating=rating, movie_id=movie_id)
    movie_review.save()
    return HttpResponseRedirect(reverse('movies_app:detail', kwargs={'movie_id': movie_id}))


def increment_likes(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.likes += 1
    movie.save()
    return HttpResponseRedirect(reverse('movies_app:index'))


def increment_watch_count(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.watch_count += 1
    movie.save()
    return HttpResponseRedirect(reverse('movies_app:index'))