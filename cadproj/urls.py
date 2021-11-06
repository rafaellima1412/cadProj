from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "cadproj"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("projetos/", views.ListaProjetos, name="lista_projetos"),
    path("projeto/cadastrar/", views.InsereProjeto, name="cadastra_projeto"),
    path("projeto/<int:pk>", views.AtualizaProjeto, name="atualiza_projeto"),
    path("projeto/excluir/<int:pk>", views.ExcluiProjeto, name="deleta_projeto"),
    path("projeto/simulador/<int:pk>", views.simulador, name='simulador'),
    path("projeto/simulador/investimento/<int:pk>", views.investimento, name='investimento'),
]
