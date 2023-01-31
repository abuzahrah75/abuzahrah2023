from django.urls import path

from .views import index, search
from .crudutils import *

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
]


htmx_urlpatterns = [
    path('senarai/<str:app_name>/<str:model_name>',
         crud_list_all, name='crud-listAll'),
    path('detals/<str:app_name>/<str:model_name>/<int:pk>',
         crud_detail, name='crud-detail'),
    path('edit/<str:app_name>/<str:model_name>/<int:pk>',
         crud_edit, name='crud-edit'),
    path('delete/<str:app_name>/<str:model_name>/<int:pk>',
         crud_delete, name='crud-delete'),
    path('delete-confirm/<str:app_name>/<str:model_name>/<int:pk>', crud_delete_confirm,
         name='crud-delete-confirm'),
    path('empty', return_kosong, name="crud-return-empty"),

    path('add_item/<str:app_name>/<str:model_name>',
         add_item, name="crud-add-item"),
]

urlpatterns += htmx_urlpatterns
