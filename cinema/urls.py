from django.contrib import admin
from django.urls import path, include
from cinema.views import *

urlpatterns = [
    path('', cinemaUrls),
    path('movie-list/', MovieListView.as_view()),
    path('movie/<int:pk>', MovieDetailView.as_view()),
    path('add-movie/', MovieAddView.as_view()),
    path('category/', CategoryView.as_view()),
    path('add-category/', CategoryAddView.as_view()),
    path('actors-list/', ActorsListView.as_view()),
    path('actor/<int:pk>', ActorDetailView.as_view()),
    path('add-actor/', ActorAddView.as_view()),    
    path('directors/', DirectorsListView.as_view()),
    path('director/<int:pk>', DirectorDetailView.as_view()),
    path('add-director/', DirectorAddView.as_view()),
    path('add-genre/', GenreAddView.as_view()),   
    path('genre/', GenreView.as_view()),
    path('add-rating/', RatingAddView.as_view()),    
    path('rating/', RatingView.as_view()),
    path('add-ratingstar/', RatingStarAddView.as_view()),
    path('ratingstar/', RatingStarView.as_view()),
    path('add-movie_shots/', MovieShotsAddView.as_view()),    
    path('movie_shots/', MovieShotsView.as_view()),
    path('add-review/', ReviewAddView.as_view()),
    path('review/', ReviewView.as_view()),
]
