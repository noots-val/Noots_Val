from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm


def index(request):
    return render(request, 'official_site/index.html')


def profile(request):
    return render(request, 'official_site/profile.html')


def products(request):
    return render(request, 'official_site/products.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return HttpResponseRedirect('official_site/contact.html')
    else:
        form = ContactForm()
    return render(request, 'official_site/contact.html', {'form': form})
