def my_fun(n):
    s=0
    while(n!=0):
        s=s+n%10
        n/=10
    print(s)

my_fun(123)