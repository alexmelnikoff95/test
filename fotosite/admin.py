from django.contrib import admin

from fotosite.models import Photo, Country, City, Entity, Photographer, Category

admin.site.register(Photo)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Entity)
admin.site.register(Photographer)
admin.site.register(Category)
