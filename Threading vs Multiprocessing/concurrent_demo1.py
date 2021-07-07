import time 
import concurrent.futures

start = time.perf_counter()

def realizar_operações(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(realizar_operações, 1)
    f2 = executor.submit(realizar_operações, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')