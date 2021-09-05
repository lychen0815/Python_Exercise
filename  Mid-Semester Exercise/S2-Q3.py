"""
Write a function def divisible(N,denominator): to print all integer numbers between 0 and N (inclusive) that are divisible by denominator. Each number that is divisible should be printed on separate lines from largest to smallest. When the function is finished, it should print "End".

Note If N is less than 1, then instead of the above, the program should print: "N must be greater than 0.
"""
def divisible(N,denominator):
    if N < 1:
        print("N must be greater than 0")

    for i in range(N,0,-1):
        if denominator == 0:
            print("Denominator must not be 8")
            break
        if i % denominator == 0:
            print(str(i) + " is divisilble by " + str(denominator))

divisible(8,0)
divisible(23,5)
divisible(0,8)