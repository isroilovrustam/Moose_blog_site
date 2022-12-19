from django.shortcuts import render
from .models import Home
from article.models import Article
from contact.models import ComtactMe
# Create your views here.


def index_view(request):
    obj = Home.objects.all()
    obj_article = Article.objects.all()[:6]
    obj_contactme = ComtactMe.objects.all()
    ctx = {
        'homes': obj,
        'articles': obj_article,
        'contactmes': obj_contactme,

    }

    return render(request, 'home.html', ctx)
