num = int(input("请输入一个数字: "))
reversedNum = 0
while num > 0 :
    reversedNum = reversedNum * 10 + num % 10;
    num = num // 10

print("翻转之后的数字是: reversedNum = %d" %(reversedNum))
