happy = []
prime = []

with open('happynumbers.txt', 'r') as open_file:
    for line in open_file:
        happy.append(int(line))

with open('primenumbers.txt', 'r') as open_file:
    for line in open_file:
        prime.append(int(line))


overlapNum = []

for elem in happy:
    if elem in prime:
        overlapNum.append(elem)

print(overlapNum)