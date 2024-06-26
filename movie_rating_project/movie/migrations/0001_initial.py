# Generated by Django 4.2.11 on 2024-04-03 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieScore', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('genre', models.CharField(max_length=255)),
                ('release_date', models.IntegerField(blank=True, default='', max_length=200)),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.rating')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
