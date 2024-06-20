import threading
import time


def square(a):
    for i in a:
        time.sleep(0.5)
        print("square", i * i)


def cube(a):
    for i in a:
        time.sleep(0.7)
        print("cube", i * i * i)


arr = [1, 2, 3, 4]

t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()
