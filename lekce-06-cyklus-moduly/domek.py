from turtle import *

sirka_domku = 100

# nakreslime krabici
for i in range(4):
    forward(sirka_domku)
    left(90)

# jdeme zpet na levou hranu strechy
left(90)
forward(sirka_domku)
right(90)

# kreslime strechu (prekryv spodni hrany strechy s horni hranou krabice)
for i in range(3):
    forward(sirka_domku)
    left(120)

done()