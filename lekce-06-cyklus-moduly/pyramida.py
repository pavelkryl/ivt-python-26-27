from turtle import *

pocet_schodu = 25
vyska_schodu = 5
hloubka_schodu = 3
delka_plosinky = 40

speed(0)

for i in range(pocet_schodu):
    left(90)
    forward(vyska_schodu)
    right(90)
    forward(hloubka_schodu)

forward(delka_plosinky)

for i in range(pocet_schodu):
    forward(hloubka_schodu)
    right(90)
    forward(vyska_schodu)
    left(90)

delka_zakladny = 2 * pocet_schodu * hloubka_schodu + delka_plosinky
left(180)
forward(delka_zakladny)

done()
