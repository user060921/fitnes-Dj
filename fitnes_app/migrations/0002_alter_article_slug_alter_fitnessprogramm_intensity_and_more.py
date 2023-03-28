# Generated by Django 4.1.7 on 2023-03-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnes_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='fitnessprogramm',
            name='intensity',
            field=models.CharField(blank=True, choices=[('Pas daraja', 'Pas daraja'), ('Vashee qiyin daraja', 'Vashee qiyin daraja'), ("O'rtancha daraja", "O'rtancha daraja"), ('Kotta daraja', 'Kotta daraja')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fitnessprogramm',
            name='part_of_body',
            field=models.CharField(blank=True, choices=[("Qo'l", "Qo'l"), ("Ko'krak", "Ko'krak"), ('Bel', 'Bel'), ('Qorin', 'Qorin'), ('Oyoq', 'Oyoq')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fitnessprogramm',
            name='picture',
            field=models.ImageField(upload_to='fitness_programm/'),
        ),
        migrations.AlterField(
            model_name='fitnessprogramm',
            name='slug',
            field=models.SlugField(),
        ),
    ]