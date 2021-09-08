print("Welcome to the rollercoaster!")
h=int(input("Whats is your height in cm?\n"))

#we can also make a variable then we can make the bill
if h>=120:
   age=int(input("What is your Age?"))
   do=input("Do you want to click a photo? that will charge extra 2$")
   if age<=12:
       if(do=='Yes'):
          print("you have to pay",5+2,"$")
       else:
           print("you have to pay 5$")

   elif age>12 and age <=18:
       if(do=="Yes"):
           print("you have to pay 9$")
       else:
          print("you have to give 7$")
   else:
       if(do=="Yes"):
           print("you have to pay 14$")
       else:
             print("You have to give 12$")
    
else:
    print("You can't go")
  

