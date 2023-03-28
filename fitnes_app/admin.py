from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
admin.site.register(User)
admin.site.register(SiteInfo)


@admin.register(FitnessProgramm)
class FitnessProgrammAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'intensity', 'gender', 'part_of_body']


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title']


@admin.register(Favorite)
class FavoriteAdmin(TranslationAdmin):
    prepopulated_fields = {'favorite_slug': ('favorite_title',)}

