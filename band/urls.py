from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about_page, name='about_page'),
    path('music/', views.music_page, name='music_page'),
    path('musician/<int:musician_id>/', views.bio_page, name='bio_page'),
    path('calendar/', views.calendar_page, name='calendar_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
