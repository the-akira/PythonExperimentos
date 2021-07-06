import time
import unittest
from joao import primeiro_do_ranking
from dados import ENTRADA_TESTE_1, ENTRADA_TESTE_3, SAIDA_TESTE_1, SAIDA_TESTE_3

class TestOPrimeiroDoRanking(unittest.TestCase):

    def test_deve_retornar_posicoes_quando_classificacao_e_pequena(self):
        qtd_pontuacoes = 7
        pontuacoes = [100, 100, 50, 40, 40, 20, 10]
        qtd_pontuacoes_do_joaozinho = 4
        pontuacoes_do_joaozinho = [5, 25, 50, 120]

        resposta = primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)

        self.assertEqual([6, 4, 2, 1], resposta)

    def test_deve_retornar_posicoes_quando_classificacao_e_um_pouco_maior(self):
        qtd_pontuacoes = ENTRADA_TESTE_1['qtd_pontuacoes']
        pontuacoes = list(map(int,ENTRADA_TESTE_1['pontuacoes'].rstrip().split()))
        qtd_pontuacoes_do_joaozinho = ENTRADA_TESTE_1['qtd_pontuacoes_joaozinho']
        pontuacoes_do_joaozinho = list(map(int, ENTRADA_TESTE_1['pontuacoes_joaozinho'].rstrip().split()))

        resposta = primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)

        resposta_esperada = list(map(int, SAIDA_TESTE_1.rstrip().split()))
        self.assertEqual(resposta_esperada, resposta)

    def test_deve_retornar_posicoes_rapidamente_quando_classificacao_e_colossal(self):
        qtd_pontuacoes = ENTRADA_TESTE_3['qtd_pontuacoes']
        pontuacoes = list(map(int,ENTRADA_TESTE_3['pontuacoes'].rstrip().split()))
        qtd_pontuacoes_do_joaozinho = ENTRADA_TESTE_3['qtd_pontuacoes_joaozinho']
        pontuacoes_do_joaozinho = list(map(int, ENTRADA_TESTE_3['pontuacoes_joaozinho'].rstrip().split()))

        tempo_de_inicio = time.time()
        resposta = primeiro_do_ranking(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho)
        tempo_de_execucao = time.time() - tempo_de_inicio

        resposta_esperada = list(map(int, SAIDA_TESTE_3.rstrip().split()))
        self.assertEqual(resposta_esperada, resposta)
        self.assertTrue(tempo_de_execucao < 5) 

if __name__ == '__main__':
    unittest.main()