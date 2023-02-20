from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods
import json
from django.apps import apps
# from .dummy import dummy_config
from .utility import getmy_config

# @require_http_methods(['POST'])
def add_item(request, myid):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(model_config.nama_app, model_config.nama_model)
    tugas = None

    item = model_config.nama_model
    theModule = __import__(model_config.nama_app+".forms")
    theClass = getattr(theModule, 'forms')
    theForm = getattr(theClass, model_config.edit_form)
    if request.method == "POST":
        form = theForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'mycrud/crudutils/myscript.js', {'foo': 'bar'},
            #               content_type="application/x-javascript")
            return HttpResponse(
                status = 204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{item} added."
                    })
                }
            )
            
            # return render(request, 'mycrud/crudutils/crud_detail.html', {'tugas': tugasan, "myconfig": model_config})
        # else:
            # return HttpResponse(status=204)
    else :
        form = theForm()

    return render(request, 'mycrud/utils20/crud_form.html', {'todo': tugas, "myconfig": model_config, "form":form, "action": "Add"})

def return_kosong(request):
    return render(request, 'mycrud/crudutils/kosong.html')


def index2(request, myid):
    model_config = getmy_config(myid)
    # Mymodel = apps.get_model(
    #     model_config["app_name"], model_config["model_name"])
    # tugasan = Mymodel.objects.all().order_by('id')
    # print(model_config)

    return render(request, 'mycrud/utils20/crud_listAll.html', {"myconfig": model_config})
    # return render(request, 'mycrud/crudutils/kosong.html')

def crud_list_all(request, myid):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(model_config.nama_app, model_config.nama_model)
    tugasan = Mymodel.objects.all().order_by('id')
    # print(model_config)
   
    return render(request, 'mycrud/utils20/crud_listAll2.html', {"dokumen": tugasan, "myconfig": model_config})


def crud_detail(request, myid, pk):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(model_config.nama_app, model_config.nama_model)
    tugasan = Mymodel.objects.get(id=pk)
    
    return render(request, 'mycrud/utils20/crud_detail.html', {'tugas': tugasan, "myconfig": model_config})
    # return render(request, 'tugasan/for_debug.html')


def crud_edit(request, myid, pk):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(model_config.nama_app, model_config.nama_model)
    tugasan = Mymodel.objects.get(id=pk)

    # for some reason need the .forms part
    theModule = __import__(model_config.nama_app + ".forms")
    theClass = getattr(theModule, 'forms')
    theForm = getattr(theClass, model_config.edit_form)
    if request.method == "POST":
        form = theForm(request.POST, instance=tugasan)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status = 204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{tugasan} editted."
                    })
                }
            )
            
    else :
        form = theForm(instance=tugasan)

    return render(request, 'mycrud/utils20/crud_form.html', {'tugas': tugasan, "myconfig": model_config, 'form': form, "action": "Edit"})


def crud_delete(request, myid, pk):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(
        model_config.nama_app, model_config.nama_model)
    tugasan = Mymodel.objects.get(id=pk)
    return render(request, 'mycrud/utils20/crud_delete.html', {'tugas': tugasan, "myconfig": model_config})


def crud_delete_confirm(request, myid, pk):
    model_config = getmy_config(myid)
    Mymodel = apps.get_model(
        model_config.nama_app, model_config.nama_model)
    tugasan = Mymodel.objects.get(id=pk)
    # mytugas = tugasan
    tugasan.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{tugasan} Deleted."
            })
        }
    )
