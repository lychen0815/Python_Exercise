"""
Write a program that displays
a.every integer [1, 10)
b.every integer [1, 100)
c.every second integer [1, 100)
	[1, 100) means 1 to 100, including 1 but not 100
"""

#part(a)
for i in range(1, 10):
    print(i)

#part(b)
for j in range(1,100):
    print(j)

#part(c)
for x in range(1,100,2):
    print(x)
