
def factorial(num):
    result = 1
    for n in range(1, num+1):
        result *= n
    return result


m = int(input("m = "))
n = int(input("n = "))

fmn = factorial(m) / factorial(n) / factorial(m-n)

print(fmn)

