import random

result = ''
for _ in range(1000):
    result += f'{random.randint(0,2**31 - 1)}, '

print(result)