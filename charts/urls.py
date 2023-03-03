from django.urls import path
from .views import *

urlpatterns = [
   
    path('', index, name='charts-index'),
    # path('core/', include('core.urls')),
]