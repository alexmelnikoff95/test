from django import forms
from django.contrib import admin

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PhotoAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCollectInline(admin.StackedInline):
    model = PhotoCollect
    extra = 1


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PhotoAdminForm
    inlines = (PhotoCollectInline,)
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        (None, {
            'fields': ('text', 'photo_image')
        }),

    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Connection)
admin.site.register(PhotoCollect)
