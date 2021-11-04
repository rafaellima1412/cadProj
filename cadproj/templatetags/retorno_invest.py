from cadproj.models import Projeto
from django import template

register = template.Library()


@register.simple_tag
def retorno_investimento(valor):
    valor_do_projeto = Projeto.valor_projeto
    risco = Projeto.risco
    if valor < valor_do_projeto:
        pass 
    if risco == 0:
        valor = valor * 0.05
        return valor
    if risco == 1:
        valor = valor * 0.10
        return valor
    if risco == 2:
        valor = valor * 0.20
        return valor
