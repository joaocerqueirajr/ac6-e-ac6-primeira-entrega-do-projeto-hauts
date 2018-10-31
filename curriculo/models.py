from django.db import models

TIPOS = (
    ('TECNICO', 'Técnico'),
    ('GRADUACAO', 'Graduação'),
    ('PGRADUACAO', 'Pós-Graduação')
) 

# Create your models here.
class Curso(models.Model):
    
    nome = models.CharField(
        'Nome do Curso', 
        max_length=120    
    )

    sigla = models.CharField(
        'Sigla',
        max_length=5,
        unique=True
    )

    tipo = models.CharField(
        'Tipo de Curso',
        max_length=30,
        choices=TIPOS
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'CURSO'

class Disciplina(models.Model):
    nome = models.CharField(
        'Nome da Disciplina', 
        max_length=120    
    )
    
    curso = models.ForeignKey(Curso, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'DISCIPLINA'

