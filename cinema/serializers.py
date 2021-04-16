from rest_framework import serializers
from cinema.models import *

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster', 'year', 'genre')

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ActorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actors
        fields = ('name', 'age', 'image')

class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actors
        fields = '__all__'        

class DirectorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Directors
        fields = ('name', 'age', 'image')

class DirectorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Directors
        fields = '__all__'        

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'        

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'          

class RatingStarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingStar
        fields = '__all__'       

class MovieShotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieShots
        fields = '__all__'                     

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'        



