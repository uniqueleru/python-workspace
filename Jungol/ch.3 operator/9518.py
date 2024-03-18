def oper(x,y,rev):
    if rev == 1:
        return str(x > y)
    elif rev == 2:
        return str(x >= y)
    elif rev == 3:
        return str(x <= y)
    elif rev == 4:
        return str(x < y)
    
num = list()

for i in range(0,3):
    num.append(int(input()))

print(oper(num[0],num[1],1),end = ' ')
print(oper(num[1],num[2],2),end = ' ')
print(oper(num[0],num[1],3),end = ' ')
print(oper(num[1],num[2],4))

