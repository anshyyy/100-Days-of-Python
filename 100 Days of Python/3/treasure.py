print("welcome to Treasure Island ")
print("you're at cross road take left or right")
p=input()
path=p.lower()
if path=='right':
    print("Fall into a hole!!\n     Game Over.")
else:
    b=input("Do you want to swim or wait for boat?(swim/wait)")
    ans=b.lower()
    if ans=="swim":
        print("Attacked br trout!.\n     Game over")
    else:
        c=input("Wich door you want to go? blue/red/yellow")
        ans1=c.lower()
        if ans1=='red':
            print("Burned by fire.\n      Game over")
        elif ans1=='blue':
            print("Eaten by Beasts.\n   Game over!!!")
        elif ans1=='yellow':
            print("You win!!")
        else:
            print("Game Over")
             
