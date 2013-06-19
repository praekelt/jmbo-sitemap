from django.contrib import admin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.template.loader import get_template_from_string
from django.template import Context

from preferences.admin import PreferencesAdmin, csrf_protect_m
from foundry.models import Menu, Navbar, Page

from jmbo_sitemap.models import HTMLSitemap


DRAFT_TEMPLATE = '''
{% load i18n %}
<html>
<body>

{% if navbars %}
    {% trans "Navbars" %}:
    <ul>
    {% for navbar in navbars %}
        <li>{{ navbar.title }}</li>
        <li>
            <ul>
                {% for link in navbar.links %}            
                    <li><a href="{{ link.get_absolute_url }}">{{ link.title }}</a></li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
    </ul>
{% endif %}

{% if menus %}
    {% trans "Menus" %}:
    <ul>
    {% for menu in menus %}
        <li>{{ menu.title }}</li>
        <li>
            <ul>
                {% for link in menu.links %}            
                    <li><a href="{{ link.get_absolute_url }}">{{ link.title }}</a></li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
    </ul>
{% endif %}

{% if pages %}
    {% trans "Pages" %}:
    <ul>
    {% for page in pages %}
        <li><a href="{{ page.get_absolute_url }}">{{ page.title }}</a></li>
    {% endfor %}
    </ul>
{% endif %}

</body>
<html>
'''

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

    def response_change(self, request, obj):
        result = super(HTMLSitemapAdmin, self).response_change(request, obj)
        if '_generate_draft' in request.POST:
            msg = _('The draft has been generated.')
            self.message_user(request, msg)
            result = HttpResponseRedirect(request.path) 
        elif '_make_draft_live' in request.POST:
            msg = _('The draft has been made live.')
            self.message_user(request, msg)
            result = HttpResponseRedirect(request.path) 
        return result

    def save_model(self, request, obj, form, change):
        instance = super(HTMLSitemapAdmin, self).save_model(
            request, obj, form, change
        )

        if hasattr(request, 'POST'):

            if '_generate_draft' in request.POST:
                # Assemble navbars, menus and pages in a structure
                navbars = []
                for navbar in Navbar.objects.filter(sites__in=obj.sites.all())\
                    .order_by('title'):
                    navbar.links = []
                    for o in navbar.navbarlinkposition_set.select_related()\
                        .all().order_by('position'):
                        navbar.links.append(o.link)
                    navbars.append(navbar)
                menus = []
                for menu in Menu.objects.filter(sites__in=obj.sites.all())\
                    .order_by('title'):
                    menu.links = []
                    for o in menu.menulinkposition_set.select_related().all()\
                        .order_by('position'):
                        menu.links.append(o.link)
                    menus.append(menu)
                pages = Page.objects.filter(sites__in=obj.sites.all())\
                    .order_by('title')

                # Render
                template = get_template_from_string(DRAFT_TEMPLATE)
                c = dict(navbars=navbars, menus=menus, pages=pages)
                html = template.render(Context(c))
                print html

                # Save draft
                obj.draft = html
                obj.save()

            elif '_make_draft_live' in request.POST:
                obj.content = obj.draft
                obj.draft = ''
                obj.save()


admin.site.register(HTMLSitemap, HTMLSitemapAdmin)
