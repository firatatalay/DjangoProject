from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField


class Setting(models.Model):
    STATUS = (
        ('true', 'Evet'),
        ('false', 'Hayır'),
    )
    title = models.CharField(blank=True, max_length=255)
    keywords = models.CharField(blank=True, max_length=255)
    descriptions = models.CharField(blank=True, max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    company = models.CharField(blank=True, max_length=150)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=30)
    fax = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=5)
    facebook = models.CharField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=255)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
