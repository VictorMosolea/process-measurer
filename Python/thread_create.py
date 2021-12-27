from threading import Thread
from timing import timeit
n = 100

def thread_func():
    pass

@timeit
def main():
    t = [0] * n 
    for i in range(n):
        t[i] = Thread(target=thread_func)


if __name__ == '__main__':
    main()