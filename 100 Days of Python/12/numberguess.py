import random
import os

def compare(num,guess):
    if(num>guess):
        return"Too low.\nGuess again"
    elif (num<guess):
        return"Too high.\nGuess again"
    else :
       return"You guessed it right"



def easy(mynum):
    n=10
    for i in range (1,11):
      print(f"Yor have {n} attempts remaining to guess a number")
      guess=int(input("Make a guess:"))
      if compare(mynum,guess)=="You guessed it right":
          print(f"You guessed it right {mynum}")
          break
      else:
          print(compare(mynum,guess))
          n=n-1

def hard(mynum):
    n=5
    for i in range (1,6):
      print(f"Yor have {n} attempts remaining to guess a number")
      guess=int(input("Make a guess:"))
      if compare(mynum,guess)=="You guessed it right":
          print(f"You guessed it right {mynum}")
          break
      else:
          print(compare(mynum,guess))
          n=n-1
         

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100")
mynum=random.randint(0,100)
print(mynum)
if(input("chooose a difficulty. type 'easy' or 'hard'")=="easy"):
    easy(mynum)
else:
    hard(mynum)