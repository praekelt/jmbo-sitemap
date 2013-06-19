from django.conf.urls.defaults import patterns, url

from preferences import preferences


urlpatterns = patterns(
    '',
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
