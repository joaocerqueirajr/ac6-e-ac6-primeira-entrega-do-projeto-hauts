from django.shortcuts import render, get_object_or_404
from curriculo.models import Curso
from curriculo.forms import CursoForm


# Create your views here.
def curso(request, sigla):
    curso = get_object_or_404 (Curso, sigla=sigla)
    context = {
        "curso": curso
    }
    return render(request, "curriculo/curso.html", context)

def novo_curso (request):
    context = {}

    if request.POST:
        pass
    else:
        form = CursoForm()
        
    context["form"] = form
    return render (request, 'curriculo/novo_curso.html')