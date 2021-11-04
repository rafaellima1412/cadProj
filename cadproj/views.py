from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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


InsereProjeto = ProjetoCreateView.as_view()
ListaProjetos = ProjetosListView.as_view()
