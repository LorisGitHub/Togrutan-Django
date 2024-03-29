# Generated by Django 3.1.1 on 2020-09-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='Metascore',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='media',
            name='Poster',
            field=models.ImageField(upload_to='./uploads/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='imdbRating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='media',
            name='imdbVotes',
            field=models.FloatField(),
        ),
    ]
