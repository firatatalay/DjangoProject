# Generated by Django 3.0.4 on 2020-04-12 13:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_auto_20200405_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
