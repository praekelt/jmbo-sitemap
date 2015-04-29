from django.views.generic import TemplateView

from preferences import preferences


class SitemapHTMLView(TemplateView):
    template_name = "jmbo_sitemap/sitemap.html"

    def get_context_data(self, **kwargs):
        context = super(SitemapHTMLView, self).get_context_data(**kwargs)
        context["content"] = preferences.HTMLSitemap.content
        return context
