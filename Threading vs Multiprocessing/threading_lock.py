import threading 
import time

tlock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + "Started")
    tlock.acquire()
    print(name + " Has acquired the lock")
    while repeat > 0:
        time.sleep(delay)
        print(name + ":" +str(time.ctime(time.time())))
        repeat -= 1 
    print(name + " is releasing the lock")
    tlock.release()
    print("Timer: "+name+" Completed")

def main():
    t1 = threading.Thread(target=timer, args=("Timer 1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer 2", 2, 5))
    t1.start()
    t2.start()
    print("Function main() Completed")

if __name__ == "__main__":
    main()