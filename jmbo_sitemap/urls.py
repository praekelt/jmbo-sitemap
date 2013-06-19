from django.conf.urls.defaults import patterns, url

from preferences import preferences

from jmbo_sitemap import sitemaps


urlpatterns = patterns(
    '',

    (r'^sitemap\.xml$', 'jmbo_sitemap.sitemap', {'sitemaps': sitemaps}),

    url(
        r'^sitemap/$',
        'django.views.generic.simple.direct_to_template',
        {
            'template': 'jmbo_sitemap/sitemap.html', 
            'extra_context': {'content': lambda: preferences.HTMLSitemap.content}
        },
        name='html-sitemap'
    ),
)
