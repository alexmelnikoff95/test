from django.db import models


class Category(models.Model):
    name = models.CharField('категория', max_length=122)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField('название страны', max_length=122)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('название города', max_length=122)
    country = models.ForeignKey(Country, verbose_name='страна', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Entity(models.Model):
    name = models.CharField('название вещи', max_length=122)
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.CASCADE, default=1, blank=True, null=True)
    photo = models.ForeignKey('Photo', verbose_name='фото сущности', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Photographer(models.Model):
    name = models.CharField('имя фотографа', max_length=122, unique=True)
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', verbose_name='фотографии', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class PhotoPubManager(models.Manager):
    """Все одобренные фото или не одобренные"""

    def pub(self, pub: bool = False):
        return super().get_queryset().filter(published=pub)


class PhotoAll(models.Manager):

    def photo_other(self, name_photo: str = None, name_city: str = None, name_country: str = None):
        """Все фото из города страны или по имени фото"""
        if name_photo:
            return super().get_queryset().filter(name=name_photo)
        if name_city:
            return super().get_queryset().filter(city=name_city)
        if name_country:
            return super().get_queryset().filter(city__country__name=name_country)

        return super().get_queryset().all()

    def photo_entity(self, entity: str = None):
        """Все фото по названию сущности и опубликованные"""
        if entity:
            return super().get_queryset().filter(entity__category=entity, published=True)

        return super().get_queryset().filter(published=True)


class Photo(models.Model):
    name = models.CharField('название фото', max_length=122, default='фотография')
    photo = models.ImageField(verbose_name='фотография', upload_to='photo')
    published = models.BooleanField(verbose_name='опубликовано', default=False)
    city = models.ForeignKey(City, verbose_name='город', on_delete=models.CASCADE, blank=True, null=True)

    objects = models.Manager()

    pub_photo = PhotoPubManager()
    all_photo = PhotoAll()

    def __str__(self):
        return self.name
