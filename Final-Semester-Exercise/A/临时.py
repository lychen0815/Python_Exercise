f = open("32009682_monica.txt",'r')

for line in f.readlines():
    #line.strip()
    print(line.rstrip())