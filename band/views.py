from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, AudioClip, Event
from .forms import ContactForm

def landing_page(request):
    return render(request, 'band/landing.html')

def about_page(request):
    return render(request, 'band/about.html')

def music_page(request):
    audio_clips = AudioClip.objects.all()
    return render(request, 'band/music.html', {'audio_clips': audio_clips})

def bio_page(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    return render(request, 'band/bio.html', {'musician': musician})

def calendar_page(request):
    events = Event.objects.order_by('date')
    return render(request, 'band/calendar.html', {'events': events})

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'band/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'band/contact_success.html')

