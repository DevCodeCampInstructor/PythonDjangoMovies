# Generated by Django 3.2 on 2021-04-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0006_auto_20210428_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
