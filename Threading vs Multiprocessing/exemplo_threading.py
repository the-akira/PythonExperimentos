from threading import Thread 
import os
import math

def calcular():
    for i in range(0,4000000):
        math.sqrt(i)

threads = []

for i in range(os.cpu_count()):
    print('registrando thread %d' % i)
    threads.append(Thread(target=calcular))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()