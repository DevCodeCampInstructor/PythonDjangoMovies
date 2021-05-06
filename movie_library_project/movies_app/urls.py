from django.urls import path
from . import views

app_name = 'movies_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:movie_id>/', views.update, name='update'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
    path('review/<int:movie_id>/', views.create_review, name='create_review'),
    path('add_image/<int:movie_id>/', views.add_image, name='add_image'),
    path('<int:movie_id>/likes/', views.increment_likes, name='increment_likes'),
    path('<int:movie_id>/watched/', views.increment_watch_count, name='increment_watch_count'),
]
