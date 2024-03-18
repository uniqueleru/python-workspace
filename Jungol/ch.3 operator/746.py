a = True
b = True
c = False

print(str(not a))
print(str(a and b))
print(str(a or b))
print(str(a and (b or c)))
print(str(a or (b and c)))
print(str(not a or (b and not c)))