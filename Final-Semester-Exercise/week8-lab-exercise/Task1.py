"""
 Let's write a script that reads textfile.txt, extract every other line(The 1st, 3rd, 5th.. lines) and write those to a new file called newFile.txt.
"""
with open('/Users/liuyuchen/Desktop/Python_Exercise/Final-Semester-Exercise/week8-lab-exercise/textfile.txt','r') as f:
    lines = []
    for i, line in enumerate(f):
        if i % 2 == 0:
            lines.append(line)
with open('/Users/liuyuchen/Desktop/Python_Exercise/Final-Semester-Exercise/week8-lab-exercise/newFile.txt','w') as f:
    f.write(''.join(lines))