from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from jmbo_sitemap import sitemaps, views


urlpatterns = patterns(
    '',

    url(
        r'^sitemap\.xml$',
        'jmbo_sitemap.sitemap',
        {'sitemaps': sitemaps},
        name='sitemap'
    ),

    url(
        r'^xsitemap/$',
        views.SitemapHTMLView.as_view(),
        name='html-sitemap'
    ),
)
