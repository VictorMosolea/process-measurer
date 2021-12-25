import random

MAX_INT = 2**32 - 1
N = 1000000
with open("../data/quick_sort_data.txt", "w") as f:
    f.write(f"{N}\n")
    for _ in range(N):
        f.write(f"{random.randint(0, MAX_INT)} ")