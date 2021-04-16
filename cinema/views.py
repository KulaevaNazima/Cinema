from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from cinema.serializers import *
from cinema.models import *

@api_view(['GET'])
def cinemaUrls(request):
    cinema_urls = {
        'Movie List' : '/movie-list/',
        'Movie' : '/movie/<int:pk>',
        'Add movie' : '/add-movie/',
        'Category' : '/category/',
        'Add category' : '/add-category/',
        'Actors' : '/actors-list/<int:pk>',
        'Actor' : '/actor/<int:pk>',
        'Add actor' : '/add-actor/',
        'Directors' : '/directors/<int:pk>',
        'Director' : '/director/<int:pk>',
        'Add director' : '/add-director/',
        'Add genre' :'/add-genre/',
        'Genre' : '/genre/<int:pk>',
        'Rating' : '/rating/',
        'Add rating' : '/add-rating/',
        'Rating Star' :'/ratingstar/',
        'Add rating star' : '/add-ratingstar/',
        'Add review' : '/add-review/',        
        'Review' : '/review/',
    }
    return Response(cinema_urls)

class MovieListView(generics.ListAPIView):
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all().order_by('-id')   

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()  

class MovieAddView(generics.CreateAPIView):
    serializer_class = MovieSerializer

class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  

class CategoryAddView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class ActorsListView(generics.ListAPIView):
    serializer_class = ActorsSerializer
    queryset = Actors.objects.all()  

class ActorAddView(generics.CreateAPIView):
    serializer_class = ActorDetailSerializer    

class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorDetailSerializer
    queryset = Actors.objects.all()      

class DirectorsListView(generics.ListAPIView):
    serializer_class = DirectorsListSerializer
    queryset = Directors.objects.all() 

class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DirectorDetailSerializer
    queryset = Directors.objects.all() 

class DirectorAddView(generics.CreateAPIView):
    serializer_class = DirectorDetailSerializer
       
class GenreView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()   

class GenreAddView(generics.CreateAPIView):
    serializer_class = GenreSerializer

class RatingView(generics.ListAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()  

class RatingAddView(generics.CreateAPIView):
    serializer_class = RatingSerializer

class RatingStarView(generics.ListAPIView):
    serializer_class = RatingStarSerializer
    queryset = RatingStar.objects.all()  

class RatingStarAddView(generics.CreateAPIView):
    serializer_class = RatingStarSerializer

class MovieShotsView(generics.ListAPIView):
    serializer_class = MovieShotsSerializer
    queryset = MovieShots.objects.all()  

class MovieShotsAddView(generics.CreateAPIView):
    serializer_class = MovieShotsSerializer

class ReviewView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()   

class ReviewAddView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
