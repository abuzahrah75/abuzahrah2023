from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Dokumen


def return_kosong(request):
    return render(request, 'dokumen/kosong.html')


def pop_detail(request, pk):
    tugasan = Dokumen.objects.get(id=pk)
    return render(request, 'dokumen/partials/pop_detail.html', {'tugas': tugasan})
    # return render(request, 'tugasan/for_debug.html')


def pop_edit(request, pk):
    tugasan = Dokumen.objects.get(id=pk)
    return render(request, 'dokumen/partials/pop_edit.html', {'tugas': tugasan})


def pop_delete(request, pk):
    tugasan = Dokumen.objects.get(id=pk)
    return render(request, 'dokumen/partials/pop_delete.html', {'tugas': tugasan})


def pop_delete_confirm(request, pk):
    tugasan = Dokumen.objects.get(id=pk)
    mytugas = tugasan.nama
    tugasan.delete()
    return render(request, 'dokumen/partials/delete_confirm_notify.html', {'tugas': mytugas})
