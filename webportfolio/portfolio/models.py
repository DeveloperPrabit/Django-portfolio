from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    position = models.CharField(max_length=10, choices=[('left', 'Left'), ('right', 'Right')])
    section_type = models.CharField(max_length=50, choices=[
        ('about', 'About'),
        ('article', 'Article'),
        ('event', 'Event'),
        ('work', 'Work'),
        ('video', 'Video'),
        ('award', 'Award')
    ])

    def __str__(self):
        return self.title


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100, default='Sambeg Khatiwada')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    address = models.CharField(max_length=255)
    website = models.URLField()
    email = models.EmailField()
    phone_numbers = models.CharField(max_length=255, help_text="Separate multiple numbers with '/'")
    whatsapp_viber = models.CharField(max_length=255, help_text="Separate multiple numbers with '/'")
    facebook = models.URLField()
    youtube = models.URLField()
    linkedin = models.URLField()
    image = models.ImageField(upload_to='contact/', blank=True, null=True)

    def __str__(self):
        return "Contact Info"


class HeroSection(models.Model):
    title = models.CharField(max_length=255, help_text="Main heading (e.g. Welcome to my site)")
    subtitle = models.TextField(help_text="Short description or tagline")

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return "Hero Section Content"
