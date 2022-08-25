def fibonacci(a = 10):
    idx = 0
    fib = [1, 1]
    while a > 0:
        fib.append(fib[idx]+fib[idx+1])
        idx += 1
        a -= 1
    return fib

print(fibonacci(100))