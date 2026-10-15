# Minitest: přípravná zadání

Minitest bude mít tři části: otázku na pojem, otázku „co program vypíše“ a praktickou úlohu, ve které musíte použít cyklus. Tady jsou dvě cvičná zadání ve stejném formátu. Řešení najdete na konci, ale zkuste to nejdřív sami.

## Cvičné zadání 1

**Pojem:** Co je tělo cyklu? Jak Python pozná, kde tělo cyklu končí? Ukažte na krátkém příkladu.

**Co se vypíše?**

```python
x = 1
for i in range(3):
    x = x + 4
print(x)
```

**Úloha:** Nakreslete želvou pravidelný osmiúhelník. Použijte cyklus a délku strany uložte do proměnné.

## Cvičné zadání 2

**Pojem:** Vysvětlete, jak Python provede řádek `x = x + 1`. Proč to není rovnice?

**Co se vypíše?**

```python
x = 10
for i in range(3):
    x = x - 3
    print(x)
```

**Úloha:** Vypište cyklem čísla 10, 20, 30, …, 100 (každé na vlastní řádek).

---

## Řešení

### Zadání 1

**Pojem:** Tělo cyklu jsou odsazené řádky pod řádkem s `for`. Tyto řádky se opakují. Tělo končí prvním řádkem, který už odsazený není.

```python
for i in range(3):
    print("Ahoj")
print("Konec")
```
Vypíše 3x `Ahoj` a pak jednou `Konec`, protože `print("Konec")` není odsazený, a tedy není v těle cyklu.

**Co se vypíše?** `13`. Hodnota `x` postupně: 1, 5, 9, 13. `print(x)` není odsazený, takže se provede jen jednou, až po cyklu.

**Úloha:**

```python
from turtle import *

strana = 50
for i in range(8):
    forward(strana)
    left(45)

done()
```
Želva se celkem otočí o 360 stupňů, takže každé otočení je 360 / 8 = 45 stupňů.

### Zadání 2

**Pojem:** Provádí se ve dvou krocích: nejdřív se spočítá pravá strana (současná hodnota `x` plus 1), pak se štítek `x` přelepí na výsledek. Není to rovnice, `=` tu znamená „ulož“. Když bylo v `x` číslo 5, bude v něm po provedení 6.

**Co se vypíše?** `7`, `4`, `1`, každé na vlastním řádku. `print(x)` je odsazený, takže je v těle cyklu a provede se v každé iteraci.

**Úloha:**

```python
for i in range(10):
    print(10 * (i + 1))
```
`i` začíná nulou, proto `i + 1`. Správně je i řešení s vlastní proměnnou:

```python
cislo = 10
for i in range(10):
    print(cislo)
    cislo = cislo + 10
```
