# Generated by Django 3.1.1 on 2020-09-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20200923_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='Poster',
            field=models.URLField(),
        ),
    ]