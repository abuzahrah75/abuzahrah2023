from .models import Mycrud

def getmy_config(myid):
    myconfig= Mycrud.objects.get(id=myid)
    return myconfig

