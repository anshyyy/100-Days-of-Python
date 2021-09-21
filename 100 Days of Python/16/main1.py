# import turtle
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# for i in range(0,10):
#     timmy.forward(i)
# my_screen=turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("name",["Anshuman","JAy","Prashant","ray"])
table.add_column("Points",[100,20,500,250])
table.align="l"

print(table)
