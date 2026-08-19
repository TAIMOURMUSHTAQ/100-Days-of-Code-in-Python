# import turtle
# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cornflowerblue")
# turtle.forward(50)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
# table=prettytable.PrettyTable()
# print(table)
table=PrettyTable()
table.add_column("Pokeymon",["Pikachu" ,"Squirl" ,"Elsiveer"],"l")
table.add_column("Type",["Animal","Bird","Snail"],"c")
print(table)
table.align="r" #whole table alignment
print(table.align)
table.align["Pokeymon"]="l"