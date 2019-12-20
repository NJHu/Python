

score = int(input("请输入成绩: "))

if score >= 90 :
    print('A')
elif score >= 80 and score < 90 :
    print('B')
elif score >= 60 and score < 80 :
    print('c')
else :
    print('e')
    

if score <= 0 or score > 100 :
    print("输入错误")
else :
    print("输入正确")