from bisect import bisect, bisect_right

def primeiro_do_ranking(qtd_pont, pontuacoes, qtd_pont_do_joao, ponts_do_joao):
    pontuacoes = list(dict.fromkeys(pontuacoes))
    pontuacoes.sort()
    return [len(pontuacoes) - bisect_right(pontuacoes,ptj) + 1 for ptj in ponts_do_joao]

def primeiro(qtd_pontuacoes, pontuacoes, qtd_pontuacoes_do_joaozinho, pontuacoes_do_joaozinho):
    pontuacoes = list(set(pontuacoes))
    pontuacoes.sort()
    qtd_pontuacoes = len(pontuacoes)

    classificacoes = []
    for x in pontuacoes_do_joaozinho:
        classificacao = (qtd_pontuacoes - bisect(pontuacoes, x)) + 1
        classificacoes.append(classificacao)
    return classificacoes
		
print(primeiro_do_ranking(6,[100, 90, 90, 80, 75, 60],5,[50, 65, 77, 90, 102]))
print(primeiro(6,[100, 90, 90, 80, 75, 60],5,[50, 65, 77, 90, 102]))