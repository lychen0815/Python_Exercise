def myst_fun(N):
    if N == 1:
        return 1
    elif N % 2 == 0:
        return N + myst_fun(N//2)
    else:
        return N + myst_fun(3*N+1)

print(myst_fun(5))