name1=input("Enter you name\n")
name2=input("Enter you partner name\n")
n=name1.lower()
m=name2.lower()

#we can also combine both the strings
t=n.count("t")
t+=m.count("t")

r=n.count('r')
r+=m.count("r")

u=n.count("u")
u+=m.count("u")

e=n.count("e")
e+=m.count("e")

l=n.count("l")
l+=m.count("l")

o=n.count("o")
o+=m.count("o")
 
v=n.count("v")
v+=m.count("v")

true= t+r+u+e
love= l+o+v+e
lovescore=str(true)+str(love)

if(int(lovescore)<10) or (int(lovescore)>90):
    print("Your love percentage is:",true,love,"%")
elif (int(lovescore)>=40) and (int(lovescore)<=50):
    print("you are alright together")
else:
    print(f"your love score is{int(lovescore)}")
