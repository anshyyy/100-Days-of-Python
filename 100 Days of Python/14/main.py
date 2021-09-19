import random
import os
from datamy import data
import art

b=random.randint(0,len(data)-1)

print(art.logo)

def game():

    point=0
    while(True):
        a=b
        b=random.randint(0,len(data)-1)
        # while(a==b):
        #     b=random.randint(0,len(data)-1)

        rand_name=data[a]['name']
        rand_des=data[a]['description']
        rand_coun=data[a]['country']
        rand_folo=data[a]['follower_count']
        brand_name=data[b]['name']
        brand_des=data[b]['description']
        brand_coun=data[b]['country']
        brand_folo=data[b]['follower_count']
        print(f"you have {point} points")
        print(f"Compare A:{rand_name} {rand_des} from {rand_coun}")
        print(art.vs)
        print(f"Aganist B:{brand_name} {brand_des} from {brand_coun}")
        choice=input(f"Who has more follower? Type 'A' or 'B':")

        if choice =='A':
            if rand_folo>brand_folo:
                point+=1
                os.system("cls")
            else:
                os.system("cls")
                print(f"You are wrong! your final score is {point}")
                break
        if(choice=="B"):
             if rand_folo<brand_folo:
                point+=1
                os.system("cls")
             else:
                os.system("cls")
                print(f"You are wrong! your final score is {point}")
                break



while True:
    game()
    stop=input("Play again? 'Y' or 'N'")
    os.system("cls")
    if stop=="N":
        break

