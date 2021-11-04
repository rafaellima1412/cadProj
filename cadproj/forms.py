from django import forms

from .models import Projeto


class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto

        widgets = {
            'data_de_inicio': forms.DateInput(format='%d-%m-%Y'),
        }

        fields = '__all__'
