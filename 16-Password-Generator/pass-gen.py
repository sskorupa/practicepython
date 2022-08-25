import random

pass_len = 12
password = []

for i in range(pass_len):
    password.append(chr(random.randint(32, 126)))

password = ''.join(password)
print(password)