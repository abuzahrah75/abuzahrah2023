from unicodedata import category
from django.contrib import admin

from .models import *


admin.site.register(Dokumen)
admin.site.register(Docs_template)
admin.site.register(Category)
admin.site.register(TempSection)
admin.site.register(SectJenis)
