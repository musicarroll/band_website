from django.contrib import admin

# Register your models here.
# band/admin.py
from django.contrib import admin
from .models import Musician, AudioClip, Event, ContactMessage

admin.site.register(Musician)
admin.site.register(AudioClip)
admin.site.register(Event)
admin.site.register(ContactMessage)
