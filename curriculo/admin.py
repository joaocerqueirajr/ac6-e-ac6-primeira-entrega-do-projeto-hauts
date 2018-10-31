from django.contrib import admin
from curriculo.models import Curso, Disciplina

# Register your models here.

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')
    list_filter = ('curso',)



class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'tipo')
    list_filter = ('tipo',)

admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Curso, CursoAdmin)

