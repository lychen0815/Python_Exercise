def foo(b,a):
    if a > b:
        a,b = b,a
    if b == a:
        return 0
    else:
        return 1 + foo(b-1,a)

print(foo(3,1))