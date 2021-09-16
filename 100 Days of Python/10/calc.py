import art
import os

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

print(art.logo)
operation ={
    "+":add,
    "-" : subtract,
    "*" : multiply,
    "/" :divide
}
def calculator():
    num1=float(input("Enter the first number:\n"))
    for i in operation:
       print(i)
    cont=True    
    while cont:
        op=input("which operation? ")
        num2=float(input("enter number 2:\n"))

        calcfun=operation[op]
        ans=calcfun(num1,num2)

        print(f"{num1}{op}{num2}={ans}")
        if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ") == 'y':
            num1=ans
        else:
            os.system('cls')
            calculator()
            cont=False

calculator()



