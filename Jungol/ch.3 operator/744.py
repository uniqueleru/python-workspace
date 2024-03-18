def oper(x,y,rev):
    if rev == True:
        return str(x == y)
    else:
        return str(x != y)

a = int(input())
b = int(input())

print(oper(a,b,True))
print(oper(a,b,False))

