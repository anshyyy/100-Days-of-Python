import random

arr =["anshuman","jay","shyalli"]

word= random.choice(arr)

display =[]
for i in word:
    display+="_"

n=input("Guess a letter!\n")
s=n.lower()

for i in range(len(word)):
    x=word[i]
    if(x==s):
        display[i]=s

print(display)