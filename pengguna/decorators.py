from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
# from django.contrib.auth.models import User

def role_required(allowed_roles=[]):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            # myuser=User.objects.get(username=request.user)
            ret_x =False
            for ix in request.user.groups.all():
                # print(ix)
                if ix in allowed_roles:
                    ret_x= True
            if ret_x:
                return func(request, *args, **kwargs)
            else:
                # print(list(myuser.groups.all()))
                return HttpResponse(allowed_roles)
        return wrap
    return decorator
