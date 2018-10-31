from django.shortcuts import render
from .forms import ContatoForm, EntrarForm

# Create your views here.
def home(request):
    context = {
        "titulo":"Home",
    }
    return render(request, "index.html", context)


def contato(request):
    context = {}

    if request.POST:

        form=ContatoForm(request.POST)
        
        if form.is_valid():  
            form.enviar_email()
            context["mensagem"] = "Mensagem Enviada!"
        else:
            context["mensagem"] = "Erro ao enviar a mensagem!"
    
    else:

        form=ContatoForm()
        context["form"] = form
        context["mensagem"] = 'Preencha os campos para enviar a mensagem!'

    return render(request, "contato.html", context)

def entrar(request):
    context = {}

    if request.POST:

        form=EntrarForm(request.POST)
        
        if form.is_valid():  
            form.solicitar_entrada()
            context["solicitacao"] = "Solicitação Requerida!"
        else:
            context["solicitacao"] = "Erro ao requerir solicitação de Entrada!"
    
    else:

        form=EntrarForm()
        context["form"] = form
        context["solicitacao"] = 'Preencha os campos para solicitar entrada!'

    return render(request, "entrar.html", context)


def impacta(request):
    context = {
        "titulo":"Impacta",
    }
    return render(request, "Impacta.html", context)


