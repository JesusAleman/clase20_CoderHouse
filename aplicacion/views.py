from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,"aplicacion/base.html")

def profesores(request):
    return render(request,"aplicacion/profesores.html")

def estudiantes(request):
    return render(request,"aplicacion/estudiantes.html")

def entregables(request):
    return render(request,"aplicacion/entregables.html")

def cursos(request):
    ctx={"cursos": Curso.objects.all()}
    return render(request,"aplicacion/cursos.html",ctx)

def cursoForm(request):
    if request.method=="POST":
        curso =Curso(nombre = request.POST['nombre'], comision = request.POST['comision'])
        curso.save()
        return HttpResponse("El curso se grabó con exito!")
    return render(request, "aplicacion/cursoForm.html")

def CursoForm2(request):
    if request.method=="POST":
        miForm = CursoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            curso = Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = CursoForm()

    return render(request,"aplicacion/cursoForm2.html",{"form":miForm})

def buscarComision(request):
    return render(request,"aplicacion/buscarComision.html")

def buscar2(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request,
                       "aplicacion/resultadosComision.html",
                       {"comision":comision, "cursos":cursos})
    return HttpResponse("No se ingresaron datos para buscar!")