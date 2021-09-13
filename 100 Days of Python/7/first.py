import random

arr =["anshuman","jay","shyalli"]

word= random.choice(arr)

n=input("Guess a letter!\n")
s=n.lower()

for i in word:
    if(i==s):
        print("right")
    else:
        print("wrong")
