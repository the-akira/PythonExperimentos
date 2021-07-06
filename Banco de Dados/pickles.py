import numpy as np 
import pickle

dados = {
    'volts': np.random.random(10),
    'current': np.random.random(10),
}

# Picklando
with open('dados.pkl', 'wb') as pickle_file:
    pickle.dump(dados, pickle_file)

# Unpicklando
with open('dados.pkl', 'rb') as pickle_file:
    dados_unpickled = pickle.load(pickle_file)

print(dados_unpickled)