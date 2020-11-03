from scipy.stats import rankdata
from bisect import bisect, bisect_right, bisect_left

def calcular_rank(vector):
	mem = {}
	rank = 1
	v = vector[:]
	v.sort(reverse=True)
	for num in v:
		if num not in mem:
			mem[num] = rank
			rank = rank + 1
	return [mem[i] for i in vector]

def calc_rank(v):
	return rankdata([-1 * i for i in v], method="dense").astype(int).tolist()	

def o_primeiro_do_ranking(qtd_pont, pontuacoes, qtd_pont_do_joao, ponts_do_joao):
	resultados = []
	pt = pontuacoes[:]
	ptj = ponts_do_joao[:]
	pt.sort(reverse=True)
	ptj.sort()
	if pt != pontuacoes:
		return "Lista de pontuações não está ordenada decrescentemente"
	if ptj != ponts_do_joao:
		return "Lista de pontuações do João não está ordenada crescentemente"
	for pont_do_joao in ponts_do_joao:
		pontuacoes.append(pont_do_joao)
		resultados.append(calc_rank(pontuacoes))
	return [resultado[-1] for resultado in resultados]

def es_o_primeiro_do_ranking(qtd_pont, pontuacoes, qtd_pont_do_joao, ponts_do_joao):
	resultados = []
	merged = [*pontuacoes, *ponts_do_joao]
	len_pt = len(pontuacoes) + 1
	for _ in ponts_do_joao:
		rank = calc_rank(merged[:len_pt])
		len_pt += 1
		resultados.append(rank[-1])
	return resultados

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
        print(classificacao)
        classificacoes.append(classificacao)

    return classificacoes
		
pontuacoes = [100, 100, 50, 40, 40, 20, 20]
print(calc_rank(pontuacoes))
print(o_primeiro_do_ranking(6,[100, 90, 90, 80, 75, 60],5,[50, 65, 77, 90, 102]))
print(es_o_primeiro_do_ranking(6,[100, 90, 90, 80, 75, 60],5,[50, 65, 77, 90, 102]))
print(primeiro_do_ranking(6,[100, 90, 90, 80, 75, 60],5,[50, 65, 77, 90, 102]))
print(primeiro_do_ranking(7,[100, 100, 50, 40, 40, 20, 10],4,[5, 25, 50, 120]))