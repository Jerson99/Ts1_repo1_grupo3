import lib

def f(n):
    a=1
    if n<0:
        return 0
    elif n==0:
        return 0
    else:
        for i in range(2,n+1):
            a=a*i
        return a

.

