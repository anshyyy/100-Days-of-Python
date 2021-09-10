import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to pyPassword generator!")
ltr=int(input("How many letters would you like in your password?\n"))
sym=int(input("How many symbols would you like?\n"))
num=int(input("How many numbers would you like?\n"))

#easy version
# passw=" "
# for i in range(0,ltr):
#     passw+=random.choice(letters)

# for i in range(0,sym):
#     passw+=random.choice(symbols)

# for i in range(0,num):
#     passw+=random.choice(numbers)

# print(passw)


#hard version
password=[]
for i in range(0,ltr):
    password.append(random.choice(letters))

for i in range(0,sym):
    password.append(random.choice(symbols))

for i in range(0,num):
    password.append(random.choice(numbers))

    

random.shuffle(password)
mypass=""
for j in password:
    mypass+=j

print(mypass)



