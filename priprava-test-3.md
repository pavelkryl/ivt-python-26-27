# Cvičná zadání k testu (lekce 8)

Test trvá 45 minut a má dvě části:

- **3 teoretické otázky** (bez počítače, 2 body za každou): co program vypíše a proč,
- **2 programovací úlohy** se želvou (ve VS Code, 7 bodů za každou).

Zkouší se všechno, co je ve [slovníčku pojmů](POJMY.md): proměnné, cyklus `for`, želva, import, funkce, parametr a návratová hodnota.

Zadání si nejdřív zkus vyřešit sám/sama a teprve potom rozbal řešení.

---

## Cvičné zadání 1

### Otázka 1: Co program vypíše?

```python
x = 3
y = x + 4
x = x * 2
print(x, y)
```

<details>
<summary>Řešení</summary>

Vypíše `6 7`.

`y` se spočítá ve chvíli, kdy má `x` hodnotu 3, takže `y` je 7. Pozdější změna `x` už na `y` nemá vliv, protože do proměnné se uloží hodnota, ne postup výpočtu. `x = x * 2` vezme současnou hodnotu 3 a výsledek 6 uloží zpět do `x`.

</details>

### Otázka 2: Co program vypíše?

```python
soucet = 0
for i in range(4):
    soucet = soucet + i
print(soucet)
```

<details>
<summary>Řešení</summary>

Vypíše `6`.

Proměnná cyklu `i` má postupně hodnoty 0, 1, 2, 3 (ne 4). `soucet` se tedy postupně mění 0 → 0 → 1 → 3 → 6. `print` není odsazený, provede se jen jednou až po skončení cyklu.

</details>

### Otázka 3: Co program vypíše? U každé funkce v programu urči, jestli něco udělá, nebo vrátí hodnotu.

```python
import math

a = math.sqrt(25)
b = round(2.718, 1)
print(a)
print(b)
```

<details>
<summary>Řešení</summary>

Vypíše `5.0` a potom `2.7`.

`math.sqrt` a `round` něco spočítají a výsledek vrátí, my ho ukládáme do proměnných `a` a `b`. `print` něco udělá: vypíše hodnotu na výstup.

</details>

### Úloha 1: Pila

Nakresli pilu s 8 zuby. Každý zub je stříška ze dvou stejně dlouhých čar. Délku čáry ulož do proměnné, aby šla změnit na jednom místě.

Tip: nejdřív si na papír nakresli jeden zub a zapiš, kam se želva otáčí.

<details>
<summary>Řešení</summary>

```python
from turtle import *

delka = 30

for i in range(8):
    left(45)
    forward(delka)
    right(90)
    forward(delka)
    left(45)

done()
```

Po každém zubu míří želva zase vodorovně doprava, proto se zuby řadí za sebe.

</details>

### Úloha 2: Spirála

Nakresli čtvercovou spirálu z 20 čar. První čára je dlouhá 10 a každá další je o 10 delší. Počáteční délku i přírůstek ulož do proměnných. Na konci vypiš na výstup, jak dlouhá by byla 21. čára.

<details>
<summary>Řešení</summary>

```python
from turtle import *

delka = 10
prirustek = 10

for i in range(20):
    forward(delka)
    left(90)
    delka = delka + prirustek

print(delka)

done()
```

Vypíše `210`. Po 20 iteracích se k původní délce 10 přičetlo dvacetkrát 10.

`print` je před `done()`. Kdyby byl až za ním, výsledek by se vypsal teprve po zavření okna se želvou.

</details>

---

## Cvičné zadání 2

### Otázka 1: Co program vypíše?

```python
a = "3"
b = 3
print(a + a)
print(b + b)
```

<details>
<summary>Řešení</summary>

Vypíše `33` a potom `6`.

`"3"` je textový literál, `+` dva texty spojí. `3` je číselný literál, `+` čísla sečte.

</details>

### Otázka 2: Co program vypíše?

```python
for i in range(3):
    print(i)
    print("x")
print("konec")
```

<details>
<summary>Řešení</summary>

Vypíše:

```
0
x
1
x
2
x
konec
```

Tělo cyklu tvoří oba odsazené řádky, opakují se tedy společně. `print("konec")` už odsazený není, provede se jednou po skončení cyklu.

</details>

### Otázka 3: Program spustíme ze souboru. Co vypíše? Co by se zobrazilo, kdybychom stejné řádky psali jeden po druhém do interaktivního interpretu?

```python
import math

vysledek = math.sqrt(36)
math.sqrt(100)
print(vysledek)
```

<details>
<summary>Řešení</summary>

Ze souboru vypíše jen `6.0`. Řádek `math.sqrt(100)` odmocninu spočítá, ale návratovou hodnotu nikam neuložíme, takže se zahodí. Python přitom nehlásí žádnou chybu.

V interaktivním režimu se po řádku `math.sqrt(100)` zobrazí `10.0`, protože interaktivní interpret vypisuje výsledky sám. Po řádku s `print` se pak zobrazí `6.0`.

</details>

### Úloha 1: Pyramida

Nakresli pyramidu: 5 schodů nahoru a hned 5 schodů dolů. Velikost schodu ulož do proměnné.

Tip: použij dva cykly za sebou.

<details>
<summary>Řešení</summary>

```python
from turtle import *

schod = 30

for i in range(5):
    left(90)
    forward(schod)
    right(90)
    forward(schod)

for i in range(5):
    right(90)
    forward(schod)
    left(90)
    forward(schod)

done()
```

</details>

### Úloha 2: Kytička z kružnic

Nakresli kytičku z kružnic s poloměrem 50. Mezi kružnicemi se želva otočí o stejný úhel tak, aby se za celou kytičku otočila přesně jednou dokola. Počet kružnic ulož do proměnné. Program musí fungovat pro 6, 8 i 12 kružnic, když změníš jen tuto proměnnou. Na výstup vypiš, o kolik stupňů se želva mezi kružnicemi otáčí.

<details>
<summary>Řešení</summary>

```python
from turtle import *

pocet = 8
uhel = 360 / pocet

speed(0)

for i in range(pocet):
    circle(50)
    left(uhel)

print(uhel)

done()
```

Pro 8 kružnic vypíše `45.0`. Dělení `/` dává vždy desetinné číslo.

Kružnice končí tam, kde začala, a želva míří stejným směrem. Proto stačí mezi kružnicemi jen otočit.

</details>
