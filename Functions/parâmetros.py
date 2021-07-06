def apresentar_info(a, b, *args, instrutor='Gabriel', **kwargs):
    return [a, b, args, instrutor, kwargs]

# a - 1
# b - 2
# args - (3,)
# kwargs - {'sobrenome': 'Felippe', 'profissão': 'Programador'}
print(apresentar_info(1,2,3,sobrenome='Felippe',profissão='Programador'))