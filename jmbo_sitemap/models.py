from django.db import models

from preferences.models import Preferences
from ckeditor.fields import RichTextField
from south.modelsinspector import add_introspection_rules


class HTMLSitemap(Preferences):
    content = RichTextField(null=True, blank=True)
    draft = RichTextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'HTML Sitemap'


# Custom fields to be handled by south
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])
