#word = str(input("Input word: "))
word = "redivider"

if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
