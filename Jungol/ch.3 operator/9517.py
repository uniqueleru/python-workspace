def oper(x,y,rev):
    if rev == True:
        return str(x == y)
    else:
        return str(x != y)

num = list()
for i in range(0,3):
    num.append(int(input()))

print(oper(num[0],num[1],True),oper(num[1],num[2],True),end = ' ')
print(oper(num[0],num[1],False),oper(num[1],num[2],False))

