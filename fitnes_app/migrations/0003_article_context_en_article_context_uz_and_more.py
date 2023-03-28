# Generated by Django 4.1.7 on 2023-03-26 06:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnes_app', '0002_alter_article_slug_alter_fitnessprogramm_intensity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='context_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='context_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug_en',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug_uz',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_slug_en',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_slug_uz',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='context_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='context_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='slug_en',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='slug_uz',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fitnessprogramm',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]