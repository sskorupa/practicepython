number = float(input("Number please: "))

if number % 2:
    print(f"{number} is odd")
else:
    print(f"{number} is even")

if number % 4:
    print(f"{number} is not multiple of 4")
else:
    print(f"{number} is multiple of 4")


num1 = float(input("Num1 please:"))
num2 = float(input("Num2 please:"))

if num1 % num2:
    print(f"{num1} is not divisible by {num2}")
else:
    print(f"{num1} is divisible by {num2}")