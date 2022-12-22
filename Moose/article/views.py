from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Article
from contact.models import ComtactMe
from comment.forms import CommentForm
from comment.models import Comment


# Create your views here.

def article_view(request):
    obj = Article.objects.all()[:12]
    p = Paginator(Article.objects.all(), 3)
    page = request.GET.get('page')
    obj_page = p.get_page(page)
    obj_contactme = ComtactMe.objects.all()
    ctx = {
        'articles': obj,
        'pages': obj_page,
        'contactmes': obj_contactme,
    }

    return render(request, 'blog.html', ctx)


def single_view(request, pk):
    obj = Article.objects.get(id=pk)
    obj_comment = Comment.objects.all()
    obj_contactme = ComtactMe.objects.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.article = obj
        com.save()
        return redirect('.')
    ctx = {
        'form': form,
        'comments': obj_comment,
        'contactmes': obj_contactme,
        'single': obj
    }

    return render(request, 'blog-single.html', ctx)
