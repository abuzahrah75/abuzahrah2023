from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django.apps import apps

@require_http_methods(['POST'])
def add_item(request, app_name, model_name):
    Mymodel = apps.get_model(app_name, model_name)
    tugas = None
    mytugas = request.POST.get('nama', '')
    if mytugas:
        tugas = Mymodel.objects.create(nama=mytugas)

    return render(request, 'core/crudutils/tugasan.html', {'todo': tugas,  "app_name": app_name, "model_name": model_name})

def return_kosong(request):
    return render(request, 'core/crudutils/kosong.html')


def crud_list_all(request, app_name, model_name):
    Mymodel = apps.get_model(app_name, model_name)
    tugasan = Mymodel.objects.all().order_by('id')
    # tugasan = Mymodel.objects.getAll()
    
    return render(request, 'core/crudutils/crud_listAll.html', {"dokumen": tugasan, "app_name": app_name, "model_name": model_name})


def crud_detail(request, app_name, model_name, pk):
    Mymodel = apps.get_model(app_name, model_name)
    tugasan = Mymodel.objects.get(id=pk)
    
    return render(request, 'core/crudutils/crud_detail.html', {'tugas': tugasan,  "app_name": app_name, "model_name": model_name})
    # return render(request, 'tugasan/for_debug.html')


def crud_edit(request, app_name, model_name, pk):
    Mymodel = apps.get_model(app_name, model_name)
    tugasan = Mymodel.objects.get(id=pk)
    return render(request, 'core/crudutils/crud_edit.html', {'tugas': tugasan,  "app_name": app_name, "model_name": model_name})

def crud_edit_save(request, pk):
    pass


def crud_delete(request, app_name, model_name, pk):
    Mymodel = apps.get_model(app_name, model_name)
    tugasan = Mymodel.objects.get(id=pk)
    return render(request, 'core/crudutils/crud_delete.html', {'tugas': tugasan,  "app_name": app_name, "model_name": model_name})


def crud_delete_confirm(request, app_name, model_name, pk):
    Mymodel = apps.get_model(app_name, model_name)
    tugasan = Mymodel.objects.get(id=pk)
    mytugas = tugasan.nama
    tugasan.delete()
    return render(request, 'core/crudutils/crud_delete_confirm_notify.html', {'tugas': mytugas,  "app_name": app_name, "model_name": model_name})
