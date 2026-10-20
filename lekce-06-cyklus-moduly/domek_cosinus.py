from turtle import *
import math

sirka_domku = 100   # šířka domku
sklon = 50          # sklon střechy ve stupních

# spocitame hodnoty, ktere pouzijeme pro kresleni strechy
polovina_sirky = sirka_domku / 2
uhel_rad = math.radians(sklon)
uhel_kosinus = math.cos(uhel_rad)
delka_strechy = polovina_sirky / uhel_kosinus

# krabice
for i in range(4):
    forward(sirka_domku)
    left(90)

# skoncime v levem dolnim rohu krabice, jdeme zpet na strechu
left(90)
forward(sirka_domku)
right(90)

# zaciname spodnim levym rohem strechy, kreslime strechu
left(sklon)
# leva cast strechy
forward(delka_strechy)
right(2 * sklon)
# prava cast strechy
forward(delka_strechy)

done()