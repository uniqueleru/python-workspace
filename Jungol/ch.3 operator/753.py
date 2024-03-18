def oper(x,y,rev):
    if rev == True:
        return str(x == y)
    else:
        return str(x != y)
a = int(input("Brother? "))
b = int(input("Sister? "))
print(oper(a,b,False))