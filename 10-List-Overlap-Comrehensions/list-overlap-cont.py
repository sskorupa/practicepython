import random

a = random.sample(range(10),5)
b = random.sample(range(10),5)

c = [elem for elem in a if elem in b]

print(c)