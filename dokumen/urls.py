from django.urls import path
from .views import *
from .viewHtmx import *

urlpatterns = [
    path('', index, name="docs-index"),
    path('docsdetails', docs_details, name="docs-details"),

]

htmx_urlpatterns = [
    # path('detail/<int:pk>', pop_detail, name='dokumen-pop-detail'),
    # path('edit/<int:pk>', pop_edit, name='dokumen-pop-edit'),
    # path('delete/<int:pk>', pop_delete, name='dokumen-pop-delete'),
    # path('delete-confirm/<int:pk>', pop_delete_confirm,
    #      name='dokumen-delete-confirm'),
    # path('empty', return_kosong, name="return-empty"),
]

urlpatterns += htmx_urlpatterns
