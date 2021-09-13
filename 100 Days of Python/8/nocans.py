import math

def area(l,b):
    return l*b

def cans(area,coverage):
    return math.ceil(area/coverage)


width=int(input("Enter the width of wall\n"))
length=int(input("Enter the length of wall\n"))
cov=int(input("Enetr the coveage of 1 can\n"))

are=area(width,length)

print(cans(are,cov))
