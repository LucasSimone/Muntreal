from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

from .utils import *

from .forms import FeedbackForm
from .models import Testimonial
from mailing.models import EmailTemplate


def home(request):
    return render(request, 'main_site/pages/home.html')

def about(request):
    return render(request, 'main_site/pages/about.html', {'title':'About'})

def testimonials(request):
    # Get data from databsse and send it to the page
    context = {
        'title': 'Testimonials',
        'testimonials': Testimonial.objects.all()
    }
    return render(request, 'main_site/pages/testimonials.html', context)

def contact(request):
    context = {
        'title': 'Contact',
        'form' : FeedbackForm()
    }

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            
            # Caputre the IP and save
            instance = form.save(commit=False)
            instance.ip_address = get_ip(request)
            instance.save()

            # Send notification email
            # send_mail(
            #     "Feedback from: " + form.cleaned_data['email'],
            #     form.cleaned_data['content'],
            #     'feedback@nebulous.tech',
            #     ['lucassimone99@gmail.com'],
            # )

            messages.success(request, f'Your feedback has been received and we will get back to you as soon as possible. Thank you for helping us improve.')
            return redirect('site-contact')
        else:
            context['form'] = form


    return render(request, 'main_site/pages/contact.html', context)

def page_not_found(request, exception):
    return render(request, 'main_site/pages/404.html')

def sendEDM(request):

    EmailTemplate.objects.first().sendEmail(['lucassimone99@gmail.com','lucas.simone.careers@gmail.com'],reply_email=['reply@nebulous.tech',])

    return redirect('site-home')
