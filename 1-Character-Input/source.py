name = input("Your name: ")
age = int(input("Your age: "))
number = int(input("Number: "))
age100 = 2022 - age + 100

for x in range(number):
    print(f"Your name is {name} and you are {age} years old. In {age100} you will turn 100 years old")
