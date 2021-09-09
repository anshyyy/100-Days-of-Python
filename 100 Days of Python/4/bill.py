import random

n=input("Name of your friends!")
names=n.split(",")
#names=["Jay","Anshuman","puja","himanshu","Prashant"]
a=len(names)

ran=random.randint(0,a)

print(f"{names[ran-1]} is goint to pay the bill")