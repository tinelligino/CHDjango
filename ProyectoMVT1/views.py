from sys import flags
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Persona


def bienvenida(request):
    return HttpResponse("Pablo, 25 años, Argentina, 21/01")


def registro(request):
    template = loader.get_template("template01.html")
    diccionario = {
        "nombre01":"Sergio",
        "nombre02":"Andrea",
        "nombre03":"Josefina",
        "nombre04":"Santiago",
        }
    response = template.render(diccionario)
    return HttpResponse(response)

def familia(request):
    personas = Persona.objects.all()
    if len(personas)==0:
        Persona.objects.create(
        nombre = "Sergio",
        salario = 80,
        fecha = "1971-03-12"
        )
        Persona.objects.create(
            nombre = "Andrea",
            salario = 35,
            fecha = "1966-07-21"
        )
        Persona.objects.create(
            nombre = "Josefina",
            salario = 100,
            fecha = "2006-07-04"
        )
        Persona.objects.create(
            nombre = "Santiago",
            salario = 80,
            fecha = "2002-06-10"
        )
    personas = Persona.objects.all().order_by("nombre")
    template = loader.get_template("template02.html")
    diccionario = {
        "nombre01":personas[0].nombre,
        "nombre02":personas[1].nombre,
        "nombre03":personas[2].nombre,
        "nombre04":personas[3].nombre,
        "salario01":personas[0].salario,
        "salario02":personas[1].salario,
        "salario03":personas[2].salario,
        "salario04":personas[3].salario,
        "fecha01":personas[0].fecha,
        "fecha02":personas[1].fecha,
        "fecha03":personas[2].fecha,
        "fecha04":personas[3].fecha,
    }
    response = template.render(diccionario)
    return HttpResponse(response)
