import random
import word
import logo

print(logo.log)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6


word= random.choice(word.word_list)

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

    for i in range(len(word)):
        x=word[i]
        if(x==s):
            display[i]=s

    if s not in word:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You loose!!")
            break
    
    if(count<=1):
          print("You won!")
          break

    print(display)

print(f"Word was {word}")
print(display)
