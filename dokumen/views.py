from django.shortcuts import render


from .models import *

def index(request):
    # dokumen = Dokumen.objects.all().order_by('id')
    return render(request, 'dokumen/index.html')


def docs_details(request):
    return render(request, 'dokumen/docs_details.html')



def part_docs(request):
    pass
