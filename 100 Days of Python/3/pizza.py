print("Welcome to pizza deliveries!")
si=input("What size pizza do you want? S,M,L\n")
bill=0

if si=="S":
    bill+=15
if si=='M':
    bill+=20
if si=='L':
    bill+=25

pep=input("Do you want peporonni?\n")
  
if pep=="Yes":
    if si=='L'or si=='M':
        bill+=3
    else:
        bill+=2

ech= input("Do you want extra chesse?\n")
if ech =="Yes":
      bill+=1

print(f"Your final bill is {bill} $")

    

   