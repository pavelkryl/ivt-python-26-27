from turtle import *

schodu = 10
velikost_schodu = 10

speed(0)

for i in range(schodu):
    left(90)
    forward(velikost_schodu)
    right(90)
    forward(velikost_schodu)

for i in range(schodu):
    right(90)
    forward(velikost_schodu)
    left(90)
    forward(velikost_schodu)

done()
