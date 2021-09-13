def num(n):
    if n<1:
        return
    num(n-1)
    print(n)

num(5)