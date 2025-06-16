from django.shortcuts import render
from .models import Service, Image
from .forms import ContactForm

def home(request):
    services = Service.objects.all()
    images = Image.objects.all()
    return render(request, 'home.html', {'services': services, 'images': images})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def privacy(request):
    return render(request, 'privacy.html')

def cookie_policy(request):
    return render(request, 'cookie.html')
