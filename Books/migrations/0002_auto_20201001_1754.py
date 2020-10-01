# Generated by Django 3.1.2 on 2020-10-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='added_by',
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
