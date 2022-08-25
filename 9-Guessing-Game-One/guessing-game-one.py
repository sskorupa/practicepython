import random

while True:
    cnt = 1
    rndNum = random.randint(1,9)
    while True:
        userInput = int(input("Please input a number: "))

        if userInput > rndNum:
            print(f"{userInput} > {rndNum}")
        if userInput < rndNum:
            print(f"{userInput} < {rndNum}")
        if userInput == rndNum:
            print(f"{userInput} == {rndNum} Good Job! Number of tries = {cnt}")
            break
        cnt += 1

    gameEnd = str(input("Restart? y/n\n"))
    if gameEnd == 'n':
        break