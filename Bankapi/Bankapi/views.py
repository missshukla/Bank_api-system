from django.http import HttpResponse

def desk(self):
    print("desk are here")
    return HttpResponse("<h1>deskpage</h1>")