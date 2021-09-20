"""
 Let's write a script that reads textfile.txt, extract every other line(The 1st, 3rd, 5th.. lines) and write those to a new file called newFile.txt.
"""

with open('textfile.txt','r') as f:
    lines = []
    for i, line in enumerate(f):
        if i % 2 == 0:
            lines.append(line)
with open('newFile.txt','w') as f:
    f.write(''.join(lines))


