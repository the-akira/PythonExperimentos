def pessoa(**kwargs):
    print(kwargs)
    for nome, idade in kwargs.items():
        print(f'{nome} tem atualmente {idade} anos de idade')

pessoa(gabriel='33', rafael='47', daniel='22')

def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'{pessoa} tem como cor favorita: {cor}')

cores_favoritas(Gabriel='roxo', Rafael='vermelho', Eliel='azul')
cores_favoritas(Gabriel='roxo', Rafael='vermelho', Eliel='azul', Maria='verde', Julia='amarelo')