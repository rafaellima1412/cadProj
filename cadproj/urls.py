from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "cadproj"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("projeto/cadastrar/", views.InsereProjeto, name="cadastra_projeto"),
    path("projetos/", views.ListaProjetos, name="lista_projetos"),
    path("projetos/<int:id>", views.AtualizaProjeto, name="atualiza_projeto"),
    path("projeto/excluir/<int:id>", views.ExcluiProjeto, name="deleta_projeto"),
]
