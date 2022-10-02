from django.http import HttpResponse
from django.template import loader
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

