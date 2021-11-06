from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView, UpdateView

from cadproj import action
from cadproj.models import Projeto

from .forms import ProjetoForm


class ProjetoCreateView(CreateView):
    template_name = "cria.html"
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy("cadproj:lista_projetos")


class ProjetosListView(ListView):
    template_name = "lista.html"
    model = Projeto
    context_object_name = "projetos"
    

class ProjetoUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Projeto
    context_object_name = "projeto"
    fields = '__all__'
    success_url = reverse_lazy("cadproj:lista_projetos")
    
    def get_object(self, queryset=None):
        projeto = None
        id = self.kwargs.get(self.pk_url_kwarg)
        if id is not None:
            # Busca o projeto apartir do id
            projeto = Projeto.objects.filter(id=id).first() 
        return projeto


class ProjetoDeleteView(DeleteView):
    template_name = "exclui.html"
    model = Projeto
    context_object_name = "projeto"
    success_url = reverse_lazy("cadproj:lista_projetos")


def simulador(request, pk):
    projeto = None
    if pk is not None:
        projeto = Projeto.objects.filter(id=pk).first()        
    context = {'id': pk, 'projeto': projeto}
    return render(request, 'saida.html', context=context)


def investimento(request, pk):
    retorno_calculo = None
    projeto = None
    if request.method == "POST":
        get_text = request.POST["invest"]
        get_id = pk
        retorno_calculo = action.retorno(get_id , get_text)
        if get_id is not None:
            projeto = Projeto.objects.filter(id=get_id).first() 
    context = {'id': get_id, 'retorno_calculo': retorno_calculo, 'projeto': projeto}
    return render(request, 'saida.html', context=context)
       

InsereProjeto = ProjetoCreateView.as_view()
ListaProjetos = ProjetosListView.as_view()
AtualizaProjeto = ProjetoUpdateView.as_view()
ExcluiProjeto = ProjetoDeleteView.as_view()
