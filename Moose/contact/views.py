from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ComtactMe


# Create your views here.


def contact_view(request):
    obj = ComtactMe.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/')
    ctx = {
        'form': form,
        'contactmes': obj,
    }

    return render(request, 'contact.html', ctx)
