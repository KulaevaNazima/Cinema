from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':("title",)}
    list_display = ('title', 'year')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':("name",)}    
    list_display = ('name',)

class ActorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image')

class DirectorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'image')

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url':("name",)}    
    list_display = ('name',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'ip', 'movie')

class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)

class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'movie')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'movie')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actors, ActorsAdmin)     
admin.site.register(Directors, DirectorsAdmin) 
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(RatingStar, RatingStarAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(Review, ReviewAdmin)


