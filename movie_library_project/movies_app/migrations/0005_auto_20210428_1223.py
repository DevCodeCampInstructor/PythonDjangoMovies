# Generated by Django 3.2 on 2021-04-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0004_movierating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='watch_count',
            field=models.IntegerField(default=0),
        ),
    ]
