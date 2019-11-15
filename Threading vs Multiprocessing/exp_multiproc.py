from multiprocessing import Process
import os
import math

def calcular():
	for i in range(0,70000000):
		math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
	print('registrando processo %d' % i)
	processes.append(Process(target=calcular))

for process in processes:
	process.start()

for process in processes:
	process.join()