from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    # path('about/', views.about, name='site-about'),
    # path('contact/', views.contact, name='site-contact'),
    # path('testimonials/', views.testimonials, name='site-testimonials'),
    # path('sendEDM/', views.sendEDM, name='send-edm'),
]