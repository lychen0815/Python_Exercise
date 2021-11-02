"""
Q3 : This question is about Errors & exceptions.
"""
#(a) Please list all errors below.

"""
1.SyntaxError
"""
def mystery_func_2(x,y):
    print(x, y)
    r = x%y
    while r > 0:
        r=x%y
        if r == 0:
            print (y)
        else:
            q=y
            x=q
            y=r
mystery_func_2(126,196)


#(b) Explain what does the mystery_func_2 function do?

"""
mystery_func_2 will find the largest common multiple of the two input values
"""



#(c) What is output for mystery_func_2(126,196) ?
"""
14
"""