import random

mynum = 5

upperbound = 100
lowerbound = 0

pcguess = random.randint(lowerbound, upperbound)
while True:
    if pcguess > mynum:
        upperbound = int(upperbound/2)
        pcguess = random.randint(lowerbound, upperbound)
        print(pcguess)
    if pcguess < mynum:
        lowerbound = int(upperbound/2)
        pcguess = random.randint(lowerbound, upperbound)
        print(pcguess)
    if pcguess == mynum:
        print(pcguess)
        print("Win!")
        break

#print(pcguess)
