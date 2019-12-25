for num in range(100, 1000) :
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == (low ** 3 + mid ** 3 + high ** 3) :
        print("水仙花数是:", num)
        
print(9//2)
print(-9//2)