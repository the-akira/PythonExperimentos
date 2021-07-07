import sys 
import math 
import random 
import threading 
import time

def execute_thread(i):
    print(f'Thread {i} sleeps at {time.strftime("%H:%M:%S", time.gmtime())}')
    rand_sleep_time = random.randint(1,5)
    time.sleep(rand_sleep_time)
    print(f'Thread {i} stops sleeping at {time.strftime("%H:%M:%S", time.gmtime())}')

for i in range(100):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print(f'Active Thread: {threading.activeCount()}')
    print(f'Thread Objects: {threading.enumerate()}')