import random

randNum = random.randint(1000,9999)
randNumStr = str(randNum)
print(randNumStr)

userGuess = int(input("Your Guess: "))
userGuessStr = str(userGuess)

bull = 0
cow = 0
temp = randNumStr
randNumStr = list(randNumStr)
print(randNumStr)

if userGuessStr[0] == randNumStr[0]:
    bull += 1
    randNumStr[0] = '-'
    print(randNumStr)

if userGuessStr[1] == randNumStr[1]:
    bull += 1
    randNumStr[1] = '-'
    print(randNumStr)

if userGuessStr[2] == randNumStr[2]:
    bull += 1
    randNumStr[2] = '-'
    print(randNumStr)

if userGuessStr[3] == randNumStr[3]:
    bull += 1
    randNumStr[3] = '-'
    print(randNumStr)


if userGuessStr[0] in randNumStr:
    cow += 1
    randNumStr[randNumStr.index(userGuessStr[0])] = '-'
    print(randNumStr)

if userGuessStr[1] in randNumStr:
    cow += 1
    randNumStr[randNumStr.index(userGuessStr[1])] = '-'
    print(randNumStr)

if userGuessStr[2] in randNumStr:
    cow += 1
    randNumStr[randNumStr.index(userGuessStr[2])] = '-'
    print(randNumStr)

if userGuessStr[3] in randNumStr:
    cow += 1
    randNumStr[randNumStr.index(userGuessStr[3])] = '-'
    print(randNumStr)
    
randNumStr = temp

print(f"{cow} cows, {bull} bulls")