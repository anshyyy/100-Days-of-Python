import random
import art
import os
def deal_card():
   cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
   card=random.choice(cards)
   return card


def score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,compu_score):
    if user_score>21 and compu_score>21:
        return "You went over. You lose 😤 "

    if user_score==compu_score:
        return "Draw 🙃"
    elif compu_score==0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
       return "Win with a Blackjack 😎"
    elif user_score > 21:
       return "You went over. You lose 😭"
    elif compu_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > compu_score:
       return "You win 😃"
    else:
       return "You lose 😤"



def play_game():
    print(art.logo)
    user=[]
    computer =[]
    play=False
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    
    while not play:
        user_score=score(user)
        comp_score=score(computer)
        print(f"Your cards:{user},current score:{user_score}")
        print(f"Computer's first card:{computer[0]}")
        
        if user_score==0 or comp_score==0 or user_score>21:
            play=True
        else:
            a=input("Type 'y' to get another card ,type 'n' to pass:")
            if a=='y':
                user.append(deal_card())
            else:
                play=True

    while int(comp_score)!=0 and int(comp_score)<17:
        computer.append(deal_card())
        comp_score=score(computer)

    print(f"your final hand :{user},final score:{user_score}")
    print(f"Computer final hand: {computer},final score: {comp_score}")

    print(compare(user_score,comp_score))





while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':

    os.system('cls')
    play_game()


