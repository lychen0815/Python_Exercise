

import re

def test1(filename):
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip()
            if re.search(r"^((?!:).)*$", line) != None:
                del line
            else:
                print("has :")

test1('task1.txt')