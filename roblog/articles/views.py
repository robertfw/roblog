from django.shortcuts import render, redirect
from articles.models import Article


def dashboard(request):
    if request.method == 'POST':
        # check for a new title
        new_title = request.POST.get('title', None)
        if new_title:
            article = Article(title=new_title)
            article.save()

            if request.POST.get('destination') == 'dashboard':
                return redirect('dashboard')
            else:
                return redirect('article_editor', article_id=article.id)

            return redirect('dashboard')

    return render(request, 'dashboard.html', {
        'articles': Article.objects.all()
    })


def article(request, article_id):
    return render(request, 'article.html', {'article': Article.objects.get(id=article_id)})


def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        if request.POST.get('delete1', False) and request.POST.get('delete2', False) and request.POST.get('delete3', False):
            article.delete()
            return redirect('dashboard')
        else:
            article.title = request.POST.get('title')
            article.text = request.POST.get('text')
            article.visible = True if request.POST.get('visible') == '1' else False

            article.save()

            if request.POST.get('destination') == 'dashboard':
                return redirect('dashboard')
            else:
                return redirect('article_editor', article_id=article.id)

    return render(request, 'article_editor.html', {
        'article': article
    })
