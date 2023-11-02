from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

def vistaInicio(request):
    nombre = "juan"
    apellidos="subnormal"
    #doc = open("C:/Users/rober/OneDrive/Escritorio/proyectoDjango/proyecto1/Plantillas/miplantilla.html")
    #doc = open("D:/github/pruebaLinux/index.html")
    #plt =Template(doc.read()) #este template es diferente del del loader
    #doc.close()
    #doc = loader.get_template('miplantilla.html')
    
    #ctx=Context({"nombre_persona":nombre, "apellidos_persona":apellidos})
    #documento=doc.render({"nombre_persona":nombre, "apellidos_persona":apellidos}) #a esto se le pasa un diccionario
    
    
    #return HttpResponse(documento)
    return render(request, "index.html", {"nombre_persona":nombre, "apellidos_persona":apellidos} ) #es solo una linea, no hace flata contextos ni nafa

def vistaMenu(request):
    return render(request, "menu.html" ) #es solo una linea, no hace flata contextos ni nafa


def despedida(request):
    return HttpResponse("Despedida")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request,edad,  anyo):
    edadActual = edad
    periodo=anyo-2020
    edadFutura=edadActual + periodo
    documento="<html><body><h2>En el año %s tendras %s" % (anyo, edadFutura)
    return HttpResponse(documento)

def vistaSobreNosotros(request):
    return render(request, "about.html") #es solo una linea, no hace flata contextos ni nafa

