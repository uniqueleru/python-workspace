#이거 오답으로 뜸 근데 안고칠거임 귀찮음

iput = list()
out = [0 for x in range(3)]
iput = input().split(" ")

out[0] = int(iput[1])
out[1] = int(iput[2])
out[2] = int(iput[3])
o_sum = sum(out)
o_avg = o_sum/3

print("           name  kor  eng  mat  sum    avg\n     "+ iput[0] +"  %d    %d   %d  %d  %.2f"%(out[0],out[1],out[2],o_sum,o_avg))
print("\n           name  kor  eng  mat  sum    avg\n     "+ iput[0] +"  %d    %d   %d  %d  %.2f"%(out[0],out[1],out[2],o_sum,o_avg))

