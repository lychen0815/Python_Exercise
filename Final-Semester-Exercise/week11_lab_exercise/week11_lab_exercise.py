a = [3,5,8,7,9]

n = len(a)
for i in range(n-1,0,-1):
    for j in range(i):
        print("this is "+str(j))