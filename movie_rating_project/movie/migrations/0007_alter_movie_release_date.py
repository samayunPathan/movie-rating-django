# Generated by Django 4.2.11 on 2024-04-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_movie_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.IntegerField(blank=True, default='', max_length=200),
        ),
    ]
