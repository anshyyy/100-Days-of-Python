from math import sqrt


def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if(n%i==0):
                return False
        return True

n = int(input())
if isprime(n):
    print("YEs")
else:
    print("No")