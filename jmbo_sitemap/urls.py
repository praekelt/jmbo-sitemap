from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from preferences import preferences

from jmbo_sitemap import sitemaps


urlpatterns = patterns(
    '',

    url(
        r'^sitemap\.xml$',
        'jmbo_sitemap.sitemap',
        {'sitemaps': sitemaps},
        name='sitemap'
    ),

    url(
        r'^sitemap/$',
        TemplateView.as_view(template_name='jmbo_sitemap/sitemap.html'),
        {
            'extra_context': {'content': lambda: preferences.HTMLSitemap.content}
        },
        name='html-sitemap'
    ),
)
