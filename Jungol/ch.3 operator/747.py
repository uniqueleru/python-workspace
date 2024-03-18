num = list()
for i in range(0,3):
    num.append(int(input()))

print(str(num[0] > num[1] and num[0] > num[2]), str(num[0] == num[1] and num[1] == num[2]))
