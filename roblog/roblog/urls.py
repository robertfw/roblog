from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^dashboard$', 'articles.views.dashboard', name='dashboard'),
    url(r'^article/(?P<article_id>\d+)/edit$', 'articles.views.edit_article', name='article_editor'),
    url(r'^article/(?P<article_id>\d+)$', 'articles.views.article', name='article'),

    url(r'^admin/', include(admin.site.urls)),
)
