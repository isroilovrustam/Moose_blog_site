from django.shortcuts import render
from .models import About
from contact.models import ComtactMe


# Create your views here.

def about_view(request):
    obj = About.objects.all()
    obj_contactme = ComtactMe.objects.all()
    ctx = {
        'abouts': obj,
        'contactmes': obj_contactme
    }

    return render(request, 'about.html', ctx)
