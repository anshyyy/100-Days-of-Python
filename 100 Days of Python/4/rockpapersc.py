import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
ans =int(input())
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
arr=[0,1,2]
ans1=arr[ans-1] #answer of user
brr=[0,1,2]

ran =random.randint(0,2)

if ans1==0:
    print(rock)
    if(arr[ran]==0):
        print("Draw")
    elif arr[ran]==1:
        print(paper)
        print("You loose")
    elif arr[ran]==2:
        print(scissors)
        print("You Win")
elif ans1==1:
     print(paper)
     if(arr[ran]==1):
        print("Draw")
     elif arr[ran]==0:
        print(rock)
        print("You Win")
     elif arr[ran]==2:
        print(scissors)
        print("You loose")
elif ans1==2:
    print(scissors)
    if arr[ran]==2:
        print("Draw")
    elif arr[ran]==1:
        print(paper)
        print("You win")
    elif arr[ran]==0:
        print(rock)
        print("You loose")

