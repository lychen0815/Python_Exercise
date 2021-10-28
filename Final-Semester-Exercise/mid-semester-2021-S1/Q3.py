"""
3. Control Structure
Write a function def divisible(N,denominator): to print all integer numbers between 0 and N (inclusive) that are divisible by denominator. Each number that is divisible should be printed on separate lines from largest to smallest. When the function is finished, it should print "End".

Note If N is less than 1, then instead of the above, the program should print: "N must be greater than 0."
"""
def divisible(N,denominator):
    if N < 1:
        print("N must be greater than 0.")
    elif denominator == 0:
        print("Denominator must not be 0")
    else:
        for i in range(N,0,-1):
            if i % denominator == 0:
                print(i,'is divisible by',denominator)
        print('end')


divisible(10,5)
