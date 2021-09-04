
with open("file.exercise.txt","r+") as f:
    line = f.readline(18)
    print(line)
    print(f.tell())
    print(f.readline(35))
    f.seek(18,0)
    line = f.readline()
    print(line)



    '''
    print('---------------')
    print(f.tell())
    print(f.readline(18))
    print('---------------')
    print(f.tell())
    print(f.readline(35))
    '''




