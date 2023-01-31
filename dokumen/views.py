from django.shortcuts import render

def index(request):
    return render(request, 'dokumen/index.html')


def docs_details(request):
    return render(request, 'dokumen/docs_details.html')



def part_docs(request):
    pass