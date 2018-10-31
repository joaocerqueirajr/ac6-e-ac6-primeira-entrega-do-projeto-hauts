from curriculo.models import Curso

def lista_cursos(request):

    return{
         "cursos": Curso.objects.all()
    }