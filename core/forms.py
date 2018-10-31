from django import forms

class ContatoForm(forms.Form):
    email=forms.EmailField()
    nome =forms.CharField()
    #assunto = forms.
    mensagem=forms.CharField()

    def is_valid(self):
        valido=super(ContatoForm, self).is_valid()
        if valido:
            self.enviar_email()
        return valido

    def enviar_email(self):
        print ("Nome: "+self.cleaned_data["nome"])
        print ("E-mail: "+self.cleaned_data["email"])
        print ("Mensagem:"+self.cleaned_data["mensagem"])

class EntrarForm(forms.Form):
    usuario=forms.CharField()
    senha=forms.CharField(widget=forms.PasswordInput)

    def is_valid(self):
        valido=super(EntrarForm, self).is_valid()
        if valido:
            self.solicitar_entrada()
        return valido

    def solicitar_entrada(self):
        print ("Usuario: "+self.cleaned_data["usuario"])
        print ("Senha: "+self.cleaned_data["senha"])
        
        
