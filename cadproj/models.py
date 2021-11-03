from django.db import models
from django.db.models.fields import CharField, IntegerField


class Projeto(models.Model):
    nome_do_projeto = CharField(max_length=150, blank=False)
    data_de_inicio = CharField(max_length=10, blank=False)
    data_de_fim = CharField(max_length=10, blank=False)
    valor_projeto = IntegerField()
    RISCO = (
        (0, 'Baixo'),
        (1, 'Medio'),
        (2, 'Alto'),
    )
    risco = models.IntegerField(default=0, choices=RISCO)
    participantes = CharField(max_length=150, blank=False)
