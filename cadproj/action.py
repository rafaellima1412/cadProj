from cadproj.models import Projeto


def retorno(pk, valor):
    projeto = Projeto.objects.get(id=pk)
    investimento = int(valor)
    valor_do_projeto = projeto.valor_projeto
    risco = projeto.risco
    if investimento < valor_do_projeto:
        investimento = 0
        return str(investimento)
    if risco == 0:
        investimento = investimento * 0.05
        return str(investimento)
    if risco == 1:
        investimento = investimento * 0.10
        return str(investimento)
    if risco == 2:
        investimento = investimento * 0.20
        return str(investimento)
