import random

choice = int(input("Head(1) or tail(0)\n"))

n= random.randint(0,1)

if n == choice:
    print("You win!!")
    if(n==1):
        print("Its Head")
    else:
        print("Its Tail")
else:
    print("You loose!!")
    if(n==1):
        print("Its Head")
    else:
        print("Its Tail")
