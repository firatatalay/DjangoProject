# Generated by Django 3.0.4 on 2020-04-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200405_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('descriptions', models.CharField(blank=True, max_length=255)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('company', models.CharField(blank=True, max_length=150)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('fax', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('smtpserver', models.CharField(blank=True, max_length=50)),
                ('smtpemail', models.CharField(blank=True, max_length=50)),
                ('smtppassword', models.CharField(blank=True, max_length=20)),
                ('smtpport', models.CharField(blank=True, max_length=5)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('twitter', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('aboutus', models.TextField()),
                ('contact', models.TextField()),
                ('status', models.CharField(choices=[('true', 'Evet'), ('false', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
    ]
