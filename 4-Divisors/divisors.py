num = int(input("Number please "))
x = range(2, num + 1)

divisors = []

for elem in x:
    if not num % elem:
        divisors.append(elem)

print(divisors)