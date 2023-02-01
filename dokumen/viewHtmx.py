from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Dokumen


def return_kosong(request):
    return render(request, 'dokumen/kosong.html')
