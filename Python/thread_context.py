from threading import Semaphore, Thread
from time import sleep

COUNTER = 0
sem_producer = Semaphore(0)
sem_consumer = Semaphore(1)

def producer():
    while(True):
        sem_producer.acquire()
        global COUNTER
        COUNTER += 1
        sem_consumer.release()

def consumer():
    while(True):
        sem_consumer.acquire()
        global COUNTER
        COUNTER += 1
        sem_producer.release()


t1 = Thread(target=producer, daemon=True)
t2 = Thread(target=consumer, daemon=True)

t1.start()
t2.start()

sleep(1)
print(COUNTER)