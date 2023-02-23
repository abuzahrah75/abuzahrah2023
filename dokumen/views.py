from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *


@login_required
def index(request):
    # dokumen = Dokumen.objects.all().order_by('id')
    return render(request, 'dokumen/index2.html')


def docs_details(request):
    return render(request, 'dokumen/docs_details.html')



def part_docs(request):
    pass
