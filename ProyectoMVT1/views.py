from sys import flags
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Persona

def bienvenida(request):
    return HttpResponse("Pablo, 25 años, Argentina, 21/01")

def registro(request):
    template = loader.get_template("template01.html")
    diccionario = {
        "nombre01":"Guillermo Tinelli",
        "nombre02":"Paola Bafundo",
        "nombre03":"Giovanni Tinelli",
        "nombre04":"Gino Tinelli",
        }
    response = template.render(diccionario)
    return HttpResponse(response)

def registrobd(request):
    personas = Persona.objects.all()
    if len(personas)==0:
        Persona.objects.create(
        nombre = "Guillermo Tinelli",
        salario = 150,
        fecha = "1979-04-10"
        )
        Persona.objects.create(
            nombre = "Paola Bafundo",
            salario = 95,
            fecha = "1980-07-18"
        )
        Persona.objects.create(
            nombre = "Giovanni Tinelli",
            salario = 30,
            fecha = "2004-02-21"
        )
        Persona.objects.create(
            nombre = "Gino Tinelli",
            salario = 30,
            fecha = "2001-11-01"
        )
    personas = Persona.objects.all().order_by("nombre")
    template = loader.get_template("template02.html")
    # diccionario = {
        # "nombre01":"Guillermo Tinelli",
        # "nombre02":"Paola Bafundo",
        # "nombre03":"Giovanni Tinelli",
        # "nombre04":"Gino Tinelli",
        # }
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

