from django.db import models
from django.db.models.fields import CharField, FloatField


class Projeto(models.Model):
    nome_do_projeto = CharField(max_length=150, blank=False)
    data_de_inicio = models.DateField('data_inicio', null=True, blank=False)
    data_de_fim = models.DateField('data_fim', null=True, blank=False)
    valor_projeto = FloatField()
    RISCO = (
        (0, 'Baixo'),
        (1, 'Medio'),
        (2, 'Alto'),
    )
    risco = models.IntegerField(default=0, choices=RISCO)
    participantes = CharField(max_length=150, blank=False)
