'''
a = input("please enter 1 list: ")
b = input("please enter 2 list: ")

a = a.split(",")
b = b.split(",")

c = max(a + b)
print(c)
print(type(c))

'''




a =[1,2,3,4]
b = [2,1,3]
m,n = len(a), len(b)
i,j = 0,0
while i < m and j < n:
    f = list()

    c = a[i]+b[j]

    f.append(c)
    print(f)
    print(c)
    i += 1
    j += 1
    #d = max(f)
    #print(f)



