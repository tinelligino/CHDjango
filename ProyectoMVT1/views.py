from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Ponete a ver las clases")