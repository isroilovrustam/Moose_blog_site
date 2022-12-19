from django.urls import path
from .views import article_view, single_view

urlpatterns = [
    path('', article_view, name='article'),
    path('<int:pk>/', single_view, name='single')
]