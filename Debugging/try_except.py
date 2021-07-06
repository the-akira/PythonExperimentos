try:
    print(nome)
except NameError as err:
    print(err)

d = {'nome':'gabriel'}

def get(dic,key):
    try:
        return dic[key]
    except KeyError:
        return 'erro de chave'

print(get(d,'nome'))
print(get(d,'name'))