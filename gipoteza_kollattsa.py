import multiprocessing as mp
import threading
from queue import Queue
from cgitb import reset


def gk(i):
    while i != 1:
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
    return True

def audit(task, result ):
    while not task.empty():
        try:
            i = task.get_nowait()
            if not gk(i):
                result.put(i)

        except:
            break

def main():
    I = 1000000000
    num_w = 10

    task = mp.Queue()
    result = mp.Queue()

    for i in range(1,I+1):
        task.put(i)

    threads = []
    for _ in range(num_w):
        p = threading.Thread(target=audit, args=(task, result))
        threads.append(p)
        p.start()

    for p in threads:
        p.join()

    if result.empty():
        print("The Collatz conjecture is confirmed for all numbers")
    else:
        print("The Collatz hypothesis is NOT confirmed for the numbers:")
        while not result.empty():
            print(result.get())

if __name__ == '__main__':
    main()


