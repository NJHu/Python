def add(*args):
    total = 0
    for val in args:
        total+=val
    return total

print(add(1))
print(add(1, 2))
