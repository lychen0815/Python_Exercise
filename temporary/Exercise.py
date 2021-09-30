import pandas as pd

file = open("students.txt")
for line in file.readlines():


    df = pd.DataFrame(line, columns=['word', 'freq'])
    print(df)
#df = pd.DataFrame(data)
#print(df)
