from turtle import *
import math

sirka = 100

# uhlopricka ctverce podle Pythagorovy vety: sirka^2 + sirka^2 = uhlopricka^2
uhlopricka = math.sqrt(sirka * sirka + sirka * sirka)
# strecha s pravym uhlem nahore je presne ctvrtina ctverce rozdeleneho
# uhloprickami, jeji strany jsou tedy polovina uhlopricky
strecha = uhlopricka / 2

# zaciname v levem dolnim rohu, zelva kouka doprava

# spodni hrana
forward(sirka)
# uhlopricka z praveho dolniho do leveho horniho rohu
left(135)
forward(uhlopricka)
# horni hrana doprava
right(135)
forward(sirka)
# prava cast strechy nahoru na vrchol
left(135)
forward(strecha)
# leva cast strechy dolu, na vrcholu je pravy uhel
left(90)
forward(strecha)
# leva hrana dolu
left(45)
forward(sirka)
# uhlopricka z leveho dolniho do praveho horniho rohu
left(135)
forward(uhlopricka)
# prava hrana dolu, koncime v pravem dolnim rohu
right(135)
forward(sirka)

done()
