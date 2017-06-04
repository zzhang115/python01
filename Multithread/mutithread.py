from multiprocessing import Process, Lock
import time, os

def sayHi(i):
    for n in range(200):
        print "hello world %d" %i

    # time.sleep(5)

for n in range(100):
    p = Process(target = sayHi(n), args = (n,))
    p.start()
    p.join()