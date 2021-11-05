from cadproj.models import Projeto
from django import template

register = template.Library()


@register.simple_tag
def retorno():
    investimento = 90
    valor_do_projeto = Projeto.valor_projeto
    risco = Projeto.risco
    if investimento < valor_do_projeto:
        investimento = 0
        return investimento
    if risco == 0:
        investimento = investimento * 0.05
        return investimento
    if risco == 1:
        investimento = investimento * 0.10
        return investimento
    if risco == 2:
        investimento = investimento * 0.20
        return investimento
