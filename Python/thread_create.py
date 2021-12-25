from threading import Thread
from datetime import datetime

n = 100

def time_in_microsec():
    dt = datetime.now()
    return dt.second * 1000000 + dt.microsecond


def thread_func():
    pass


start_time = time_in_microsec()

t = [0] * n 
for i in range(n):
    t[i] = Thread(target=thread_func)

end_time = time_in_microsec()

print(end_time-start_time)