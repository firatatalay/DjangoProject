from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import TextInput, ModelForm, Textarea


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


class ContactFormMessage(models.Model):
        STATUS = (
            ('New', 'New'),
            ('Read', 'Read'),
            ('Closed', 'Closed'),
        )
        name = models.CharField(blank=True, max_length=20)
        email = models.CharField(blank=True, max_length=50)
        subject = models.CharField(blank=True, max_length=50)
        message = models.CharField(blank=True, max_length=255)
        status = models.CharField(max_length=10, choices=STATUS, default='New')
        ip = models.CharField(blank=True, max_length=20)
        note = models.CharField(blank=True, max_length=100)
        create_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input',}),
            'subject': TextInput(attrs={'class': 'input',}),
            'email': TextInput(attrs={'class': 'input',}),
            'message': Textarea(attrs={'class': 'input', 'rows':'5'}),
        }