from django.shortcuts import render

def index(request):

    context ={}

    return render(request, 'charts/index.html', context)
