'''
 Let's write a script that reads textfile.txt and create a csv file spider_man.csv with 2 columns: name and category to store the name of the video and whether it is TV or Film respectively. Below is what the output csv will look like:
'''

with open("textfile.txt") as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]

csv_output = 'name,category\n'

category = None
for line in lines:
    if line == 'TV':
        category = 'TV'
        continue
    elif line == 'film':
        category = 'Film'
        continue
    if category:
        csv_output += ' '.join(line.split()[1:]) + ',' + category + '\n'
with open('spider_man.csv','w') as f:
    f.write(csv_output)
print(csv_output)
