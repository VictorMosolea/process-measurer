from datetime import datetime

def time_in_microsec():
    dt = datetime.now()
    return dt.second * 1000000 + dt.microsecond

def timeit(f):
    def wrap(*args, **kwargs):
        start_time = time_in_microsec()
        result = f(*args, **kwargs)
        end_time = time_in_microsec()
        print(end_time - start_time)
        return result
    return wrap
