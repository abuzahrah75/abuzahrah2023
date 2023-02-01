from django.shortcuts import render


def index(request):
    # return render(request, 'core/index2.html')
    return render(request, 'core/components/blank.html')


# @require_http_methods(['POST'])
# def search(request):
#     res_todos = []
#     search = request.POST['search']
#     if len(search) == 0:
#         return render(request, 'core/todo.html', {'todos': []})
#     for i in todos:
#         if search in i['title']:
#             res_todos.append(i)
#     return render(request, 'core/todo.html', {'todos': res_todos})
