"""
3.The Pythagorean Theorem is given by
Write a function that takes in 3 arguments (a, b, c). The function should return
a.True, if (a, b, c) are Pythagorean Triples
b.False, otherwise
"""


'''
def pythagorean_theorem(a,b,c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

print(pythagorean_theorem(3,4,5))
'''

#part C different integer powers

def pythagorean_theorem(n,a,b,c):
    if a ** n + b ** n == c ** n:
        return True
    else:
        return False

print(pythagorean_theorem(2,3,4,5))