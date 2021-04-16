from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    tagline = models.CharField(max_length=255, verbose_name='Слоган')
    description = models.TextField(blank=True, verbose_name='Описание')
    poster = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Постер')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    country = models.CharField(max_length=255, verbose_name='Страна')
    directors = models.ManyToManyField('Directors', verbose_name='Режиссер')
    actors = models.ManyToManyField('Actors', verbose_name='Актеры')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр')
    world_premiere = models.DateField(verbose_name='Дата премьеры')
    budget = models.IntegerField(verbose_name='Бюджет')
    fees_in_usa = models.IntegerField(verbose_name='Сборы в США')
    fees_in_world = models.IntegerField(verbose_name='Сборы в мире')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    url = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={"url":self.url})  

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title']           

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    url = models.SlugField(max_length=255, verbose_name='Url', unique=True) 

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('category', kwargs={"url":self.url})  

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']                  

class Actors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возвраст')
    description = models.TextField(blank=True,verbose_name='Биография')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'
        ordering = ['name']           


class Directors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возвраст')
    description = models.TextField(blank=True,verbose_name='Биография')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')    

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
        ordering = ['name']             

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    url = models.SlugField(max_length=255, verbose_name='Slug', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={"url":self.url})       

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']   

class Rating(models.Model):
    star = models.OneToOneField('RatingStar', on_delete=models.CASCADE)
    ip = models.CharField(max_length=255)
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.star 

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'
        ordering = ['star']      

class RatingStar(models.Model):
    value = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'
        ordering = ['value']      


class MovieShots(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'
        ordering = ['title']   

class Review(models.Model):
    email = models.EmailField(verbose_name='Почта')
    name = models.CharField(max_length=255, verbose_name='Имя')
    text = models.TextField(blank=True, verbose_name='Описание')
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['text']       
