# Generated by Django 5.1.4 on 2025-01-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
