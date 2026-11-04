from turtle import *

polomer = 80          # polomer kruznice
pocet_paprsku = 12    # kolik paprsku ma slunicko
delka_paprsku = 40    # jak dlouhy je jeden paprsek

# cela kruznice ma 360 stupnu, rozdelime ji na stejne dily mezi paprsky
vysec = 360 / pocet_paprsku

for i in range(pocet_paprsku):
    # kus kruznice: circle(polomer, uhel) nakresli oblouk o danem uhlu
    circle(polomer, vysec)
    # paprsek ven: zelva jde po kruznici, stred ma po leve ruce,
    # takze ven se otocime doprava
    right(90)
    forward(delka_paprsku)
    # a zpatky na kruznici
    left(180)
    forward(delka_paprsku)
    # natocime se zpet ve smeru kruznice
    right(90)

done()
