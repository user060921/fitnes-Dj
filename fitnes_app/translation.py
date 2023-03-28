from modeltranslation.translator import register, TranslationOptions
from fitnes_app.models import *


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('slug','title','context',)


@register(FitnessProgramm)
class FitnessProgrammTranslationOptions(TranslationOptions):
    fields = ('title','context','slug',)


@register(Favorite)
class FavoriteTranslationOptions(TranslationOptions):
    fields = ('favorite_title','favorite_slug',)