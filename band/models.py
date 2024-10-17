from django.db import models

# Create your models here.

from PIL import Image
import os

class Musician(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='musicians/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Call the original save method to ensure the photo is saved first
        super().save(*args, **kwargs)

        # Resize the photo if it exists
        if self.photo:
            img_path = self.photo.path
            max_size = (300, 300)  # Set the desired max dimensions

            # Open the image using Pillow
            with Image.open(img_path) as img:
                if img.height > max_size[1] or img.width > max_size[0]:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    img.save(img_path)  # Save resized image back to disk

    def __str__(self):
        return self.name

# class Musician(models.Model):
#     name = models.CharField(max_length=100)
#     instrument = models.CharField(max_length=100)
#     bio = models.TextField()
#     photo = models.ImageField(upload_to='musicians/', blank=True, null=True)

#     def __str__(self):
#         return self.name

class AudioClip(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
