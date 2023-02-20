from django.urls import path

from .views import index
from .crudutils import *

urlpatterns = [
    path('', index, name='mycrud-index'),
    # path('search/', search, name='search'),
]


htmx_urlpatterns = [
    path('senarai/<int:myid>', crud_list_all, name='crud-listAll'), 
    path('index2/<int:myid>', index2, name='crud-index2'),
    path('detals/<int:myid>/<int:pk>', crud_detail, name='crud-detail'), 
    path('edit/<int:myid>/<int:pk>', crud_edit, name='crud-edit'), 
    path('delete/<int:myid>/<int:pk>', crud_delete, name='crud-delete'), 
    path('delete-confirm/<int:myid>/<int:pk>', crud_delete_confirm, name='crud-delete-confirm'),
    path('empty', return_kosong, name="crud-return-empty"),

    path('add_item/<int:myid>', add_item, name="crud-add-item"),
]

urlpatterns += htmx_urlpatterns
