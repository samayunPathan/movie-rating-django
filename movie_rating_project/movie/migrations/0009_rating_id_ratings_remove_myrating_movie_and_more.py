# Generated by Django 4.2.11 on 2024-04-03 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0008_alter_movie_movie_logo_alter_movie_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=1)),
                ('movie_id', models.IntegerField(default=1)),
                ('rating_id', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='myrating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='myrating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_logo',
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True),
        ),
        migrations.DeleteModel(
            name='MyList',
        ),
        migrations.DeleteModel(
            name='Myrating',
        ),
        migrations.AddField(
            model_name='ratings',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
