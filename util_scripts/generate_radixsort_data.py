import random

MAX_INT = 2**31 - 1
N = 100000
with open("../data/radix_sort_data.txt", "w") as f:
    f.write(f"{N}\n")
    for _ in range(N):
        f.write(f"{random.randint(0, MAX_INT)} ")