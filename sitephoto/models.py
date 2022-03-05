from django.db import models
from django.urls import reverse


class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название для поля фотографий ')
    slug = models.SlugField(unique=True, verbose_name='Слаг для поля фото')
    text = models.TextField(verbose_name='Описание для фотографий')
    photo_image = models.ImageField(upload_to='photo_image/', verbose_name='Изображение для фото коллекции')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    draft = models.BooleanField(default=True, verbose_name='Чероновик')

    def get_absolute_url(self):
        return reverse('photo_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class PhotoCollect(models.Model):
    '''коментарий'''
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Photo, verbose_name='фото', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Blog(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название блога')
    slug = models.SlugField(unique=True, verbose_name='Слаг для блога')
    description = models.TextField(verbose_name='Текст для блога')
    blog_image = models.ImageField(upload_to='blog_image/', verbose_name='Изображение для блога')
    date = models.DateField(auto_now_add=True, verbose_name='Время публикации')
    draft = models.BooleanField(default=True, verbose_name='Чероновик')

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Слаг')
    text = models.TextField(verbose_name='Описание нас')
    image = models.ImageField(upload_to='about_image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Про меня'
        verbose_name_plural = 'Про нас'
        ordering = ['-title']

    def get_absolute_url(self):
        return reverse('about_detail', kwargs={'slug': self.slug})


class Connection(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    text = models.TextField('сообщение', max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
