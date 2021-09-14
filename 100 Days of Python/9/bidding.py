import os

data={}
print("Welcome to secret auction program.")
while True:
    
    name=input("What is your name?\n")
    money=int(input("Whats your bid? : $ "))
    ans=input("Are there another bidders ? Type 'yes' or 'no'")
    data[name]=money
    maxi=0
    n=""
    for i in data:
        if maxi<data[i]:
            maxi=data[i]
            n=i

    if ans=='no':
        os.system('cls')
        print(f"the highest bid is ${maxi} of {n}")
        break
    else :
        os.system('cls')

