# Generated by Django 4.1.7 on 2023-03-20 06:31

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='articles/')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='FitnessProgramm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to='fitness_programm')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField()),
                ('intensity', models.CharField(blank=True, choices=[('Pas daraja', 'Pas daraja'), ('Vashee qiyin daraja', 'Vashee qiyin daraja'), ('O`rtancha daraja', 'O`rtancha daraja'), ('Kotta daraja', 'Kotta daraja')], max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('Ozish', 'Ozish'), ('Kachka', 'Kachka')], max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')], max_length=50, null=True)),
                ('part_of_body', models.CharField(blank=True, choices=[('Qo`l', 'Qo`l'), ('Ko`krak', 'Ko`krak'), ('Bel', 'Bel'), ('Qorin', 'Qorin'), ('Oyoq', 'Oyoq')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_link', models.CharField(max_length=255)),
                ('wh_link', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_title', models.CharField(max_length=255)),
                ('favorite_slug', models.SlugField()),
                ('favorite_type', models.CharField(choices=[('Programma', 'Programma'), ('Maqola', 'Maqola')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
