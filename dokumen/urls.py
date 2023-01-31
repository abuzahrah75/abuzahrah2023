from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="docs-index"),

]

htmx_urlpatterns =[
    path('part_docs', part_docs, name="docs-part-docs")
]

urlpatterns += htmx_urlpatterns