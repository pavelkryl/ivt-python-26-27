from turtle import *
import math

sirka_domku = 100   # šířka domku
sklon = 50          # sklon střechy ve stupních

polovina_sirky = sirka_domku / 2
uhel_rad = math.radians(sklon)
uhel_kosinus = math.cos(uhel_rad)
delka_strechy = polovina_sirky / uhel_kosinus

for i in range(4):
    forward(sirka_domku)
    left(90)

left(90)
forward(sirka_domku)
right(90)

left(sklon)
forward(delka_strechy)
right(2 * sklon)
forward(delka_strechy)

done()