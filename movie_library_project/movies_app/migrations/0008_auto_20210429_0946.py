# Generated by Django 3.2 on 2021-04-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0007_movie_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg', max_length=500),
        ),
    ]
