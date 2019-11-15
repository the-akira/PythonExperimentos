import pickle
import numpy as np 

data_dict = {
	'volts': np.random.random(10),
	'current': np.random.random(10),
}

# Picklando
with open('data_pick.pkl', 'wb') as pickle_file:
	pickle.dump(data_dict, pickle_file)

# Unpicklando
with open('data_pick.pkl', 'rb') as pickle_file:
	new_data = pickle.load(pickle_file)

print(new_data)