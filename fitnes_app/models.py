from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class FitnessProgramm(models.Model):
    CHOICES_1 = (
        ('Pas daraja', 'Pas daraja'),
        ('Vashee qiyin daraja', 'Vashee qiyin daraja'),
        ('O\'rtancha daraja', 'O\'rtancha daraja'),
        ('Kotta daraja', 'Kotta daraja'),
    )
    CHOICES_2 = (
        ('Ozish', 'Ozish'),
        ('Kachka', 'Kachka'),
    )
    CHOICES_3 = (
        ('Ayol', 'Ayol'),
        ('Erkak', 'Erkak'),
    )
    CHOICES_4 = (
        ('Qo\'l', 'Qo\'l'),
        ('Ko\'krak', 'Ko\'krak'),
        ('Bel', 'Bel'),
        ('Qorin', 'Qorin'),
        ('Oyoq', 'Oyoq'),
    )

    slug = models.SlugField()
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='fitness_programm/')
    context = RichTextUploadingField()
    intensity = models.CharField(max_length=255, choices=CHOICES_1, blank=True, null=True)
    type = models.CharField(max_length=100, choices=CHOICES_2, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=CHOICES_3, blank=True, null=True)
    part_of_body = models.CharField(max_length=100, choices=CHOICES_4, blank=True, null=True,)

    def __str__(self):
        return self.title
    

class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    context = RichTextUploadingField()
    picture = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.title


class Favorite(models.Model):
    TYPES = (
        ('Programma', 'Programma'),
        ('Maqola', 'Maqola'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_title = models.CharField(max_length=255)
    favorite_slug = models.SlugField()
    favorite_type = models.CharField(max_length=50, choices=TYPES)

    def __str__(self):
        return '{} - {}'.format(self.user, self.favorite_title)


class SiteInfo(models.Model):
    tg_link = models.CharField(max_length=255)
    wh_link = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.email, self.tel)