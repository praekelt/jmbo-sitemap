from django.contrib import admin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from preferences.admin import PreferencesAdmin, csrf_protect_m

from jmbo_sitemap.models import HTMLSitemap


class HTMLSitemapAdmin(PreferencesAdmin):   

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
        If we only have a single preference object redirect to it,
        otherwise display listing.
        """
        model = self.model
        if model.objects.all().count() > 1:
            return super(HTMLSitemapAdmin, self).changelist_view(request)
        else:
            obj = model.singleton.get()
            return redirect(reverse('admin:jmbo_sitemap_%s_change' % \
                    model._meta.module_name, args=(obj.id,)))

    def save_model(self, request, obj, form, change):
        instance = super(HTMLSitemapAdmin, self).save_model(
            request, obj, form, change
        )

        if hasattr(request, 'POST'):
            if '_make_draft_live' in request.POST:
                obj.content = obj.draft
                obj.draft = ''
                obj.save()


admin.site.register(HTMLSitemap, HTMLSitemapAdmin)
