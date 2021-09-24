import colorgram
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.hideturtle()
# colour = colorgram.extract('image.jpg', 30)
# rbg = []
# for i in colour:
#     r= i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     nc = (r, g, b)
#     rbg.append(nc)
#
# print(rbg)

list =[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(1,101):
    tim.dot(20,random.choice(list))
    tim.forward(50)

    if i%10 ==0:
     tim.setheading(90)
     tim.forward(50)
     tim.setheading(180)
     tim.forward(500)
     tim.setheading(0)


screen = t.Screen()
screen.exitonclick()