def factorial(num) :
    result = 1
    for n in range(1, num+1):
        result *= n
    return result


n = 6
m = 10

print(factorial(m) // factorial(n) // factorial(n - m))

def add(*args) :
    total = 0
    for var in args :
        total += var
    return total

print(add(1, 2, 3, 4))