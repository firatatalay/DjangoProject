# Generated by Django 3.0.4 on 2020-04-12 20:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_auto_20200412_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='place',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
