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
    average_rating = False if len(reviews) == 0 else round(sum(review.rating for review in reviews) / len(reviews), 0)
    average_rating = int(average_rating)
    full_stars = range(average_rating if average_rating <= 5 else 5)
    empty_stars = range(5 - average_rating if 5 - average_rating > 0 else 0)
    context = {
        'movie': movie,
        'reviews': reviews,
        'average_rating': average_rating,
        'full_stars': full_stars,
        'empty_stars': empty_stars,
        'has_image': movie.image_url != '',
    }
    return render(request, 'movies_app/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        runtime = request.POST.get('runtime')
        release_date = request.POST.get('date')
        image_url = request.POST.get('image_url')
        new_movie = Movie(title=name, genre=genre, description=description, runtime=runtime, release_date=release_date)
        if image_url != '':
            new_movie.image_url = image_url
        new_movie.save()
        return HttpResponseRedirect(reverse('movies_app:index'))
    else:
        return render(request, 'movies_app/create.html')


def update(request, movie_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        runtime = request.POST.get('runtime')
        release_date = request.POST.get('date')
        image_url = request.POST.get('image_url')
        Movie.objects.filter(pk=movie_id).update(title=title, genre=genre, description=description, runtime=runtime, release_date=release_date, image_url=image_url)
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


def add_image(request, movie_id):
    image_url = request.POST.get('image_url')
    print(f'Image URL {image_url}')
    Movie.objects.filter(pk=movie_id).update(image_url=image_url)
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