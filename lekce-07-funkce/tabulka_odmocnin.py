import math

# cisla 1 az 10 = 10 pruchodu cyklem, i jde od 0 do 9
for i in range(10):
    # i zacina nulou, cislo jednickou, proto + 1
    cislo = i + 1
    odmocnina = math.sqrt(cislo)
    # bonus 1: zaokrouhleni na 2 desetinna mista
    print(cislo, round(odmocnina, 2))
