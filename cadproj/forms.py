from django import forms

from .models import Projeto


class ProjetoForm(forms.ModelForm):
    widgets = {'data_de_inicio': forms.DateInput(format='%d/%m/%Y'), }
    widgets = {'data_de_fim': forms.DateInput(format='%d/%m/%Y'), }
     
    class Meta:
        model = Projeto
        fields = '__all__'
