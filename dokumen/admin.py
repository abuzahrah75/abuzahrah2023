from unicodedata import category
from django.contrib import admin

from .models import Docs_template, SectJenis, TempSection, Category



admin.site.register(Docs_template)
admin.site.register(Category)
admin.site.register(TempSection)
admin.site.register(SectJenis)
