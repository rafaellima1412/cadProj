from cadproj.models import Projeto
from django.test import TestCase


class ProjetoTest(TestCase):

    @classmethod
    def setUpTestData(self):
        self.projeto = Projeto.objects.create(nome_do_projeto="Pepperoni", data_de_inicio="22/01/2021" , data_de_fim="03/11/2021", 
                                              valor_projeto=250000.50, risco=2, participantes="pedro, thiago e João")

    def test_valor_projeto(self):
        self.assertEqual(self.projeto.valor_projeto, 250000.50)
    
    def test_data_inicio(self):
        self.assertEquals(self.projeto.data_de_inicio, "22/01/2021")
