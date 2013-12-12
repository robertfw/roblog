from django.shortcuts import render
from articles.models import Article


def home(request):
    return render(request, 'home.html', {
        'articles': Article.objects.filter(visible=True).order_by('-publish_date')
    })
