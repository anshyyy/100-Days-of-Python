import random

arr =["anshuman","jay","shyalli"]

word= random.choice(arr)

display =[]
for i in word:
    display+="_"
l=len(word)
while True:
    n=input("Guess a letter!\n")
    s=n.lower()
    count=0
    for i in display:
        if i=="_":
            count+=1
    print(count)

    for i in range(len(word)):
        x=word[i]
        if(x==s):
            display[i]=s
    
    if(count<=1):
          break

    print(display)


print(display)