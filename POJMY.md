# Slovníček pojmů – Úvod do programování

Pojmy z lekcí 1–5. Slovníček se bude průběžně doplňovat.

---

## Program a jeho spuštění

**Program**
Posloupnost příkazů, které počítač provede. Píšeme ho jako text do souboru (u nás s příponou `.py`).

**Python**
Programovací jazyk, ve kterém píšeme naše programy. Má přesná pravidla zápisu, kterým počítač rozumí.

**VS Code**
Editor, ve kterém programy píšeme a spouštíme. Program sám neprovádí: předá ho interpretu `python3`.

**Příkaz**
Jeden pokyn pro počítač, obvykle na jednom řádku.
Příklad: `print("Ahoj")`

**Lineární provádění (řádek po řádku)**
Program se provádí příkaz po příkazu, shora dolů. Pořadí řádků proto mění výsledek.

```python
print("první")
print("druhý")
```
Vypíše nejdřív `první`, potom `druhý`.

**Výstup**
To, co program vypíše. Ve VS Code ho najdeš v okně terminálu ve spodní části obrazovky.

**print**
Příkaz, který vypíše hodnotu na výstup. Umí vypsat text i číslo.

```python
print("Ahoj")
print(42)
```

---

## Hodnoty a operace

**Literál**
Hodnota zapsaná přímo v kódu.

**Textový literál**
Text v uvozovkách, například `"Ahoj"` nebo `"42"`. Python s ním zachází jako s textem, i když obsahuje číslice.

**Číselný literál**
Číslo zapsané bez uvozovek, například `42` nebo `3.14`. Python s ním umí počítat.

Rozdíl mezi nimi:

```python
print(2 + 3)      # vypíše 5
print("2" + "3")  # vypíše 23 (texty se spojí)
```

**Aritmetické operátory**
`+` sčítání, `-` odčítání, `*` násobení, `/` dělení.
Pozor: `/` dává vždy desetinné číslo, například `6 / 2` je `3.0`.

---

## Syntaxe a sémantika

**Syntaxe**
Pravidla, jak se kód správně zapisuje (závorky, uvozovky, pořadí znaků). Když zápis pravidla porušuje, Python program vůbec nespustí.

**Sémantika**
Co zapsaný kód znamená, tedy co se stane, když ho počítač provede.

**Různý zápis, stejná sémantika**
Dva zápisy mohou vypadat jinak a znamenat totéž:

```python
print(5)
print(2 + 3)
```
Oba řádky vypíšou `5`.

---

## Proměnné

**Proměnná**
Pojmenované místo, kam si program uloží hodnotu, aby ji mohl použít později.

```python
strana = 100
print(strana)
```

**Název proměnné**
Pravidla:
- může obsahovat písmena, číslice a podtržítko `_`,
- nesmí začínat číslicí,
- nesmí obsahovat mezeru ani pomlčku,
- nesmí to být vyhrazené slovo Pythonu (například `for`, `if`),
- záleží na velikosti písmen: `delka` a `Delka` jsou dvě různé proměnné.
- měl by být psaný `snake_case` konvencí
- měl by být psaný malými písmeny
- měli bychom vynechat diakritiku
- měl by vystihovat význam proměnné, nebojte se delších názvů

Platné: `delka`, `delka_schodu`, `x2`
Neplatné: `2x`, `delka schodu`, `delka-schodu`

**x = x + 1**
Nejde o rovnici: `=` tu znamená „ulož“. Provádí se ve dvou krocích:
1. nejdřív se spočítá pravá strana (vezme se současná hodnota `x` a přičte se 1),
2. pak se štítek `x` přelepí na výsledek.

```python
x = 5
x = x + 1
print(x)  # vypíše 6
```

Pozor, nefunguje to jako vzorec v Excelu: do proměnné se uloží hodnota, ne postup výpočtu.

```python
cena = 100
pocet = 3
celkem = cena * pocet
pocet = 5
print(celkem)  # vypíše 300, ne 500
```

**Proč proměnné u schodů**
Když je délka schodu v proměnné, změníš ji na jednom místě a změní se všechny schody. Bez proměnné bys musel/a přepsat každé číslo zvlášť.

---

## Želva

**Želva (turtle)**
Knihovna Pythonu pro kreslení. Želva se pohybuje po obrazovce podle příkazů a za sebou kreslí čáru.

```python
from turtle import *

forward(100)  # dopředu o 100
left(90)      # otočit vlevo o 90 stupňů
right(90)     # otočit vpravo o 90 stupňů

done()
```

**done()**
Patří na konec programu se želvou spouštěného ze souboru. Bez něj se okno s kresbou po doběhnutí programu hned zavře.

---

## Interpret

**Interpret (python3)**
Program, který čte kód v Pythonu a provádí ho. Používá se ve dvou režimech:

**Interaktivní režim**
Spustíš `python3` v terminálu bez souboru. Píšeš příkazy po jednom a každý se hned provede. Hodí se na zkoušení a jako kalkulačka.

**Neinteraktivní spuštění**
Interpret provede celý program ze souboru, například když program spustíš ve VS Code.

**Prompt `>>>`**
Výzva interaktivního interpretu: čeká na další příkaz.

**Prompt `...`**
Interpret čeká na pokračování příkazu, protože ho považuje za nedokončený (třeba chybí zavírací závorka). Doplň, co chybí, nebo odešli prázdný řádek.
Objeví se také po řádku s `for` a dvojtečkou: interpret čeká na tělo cyklu. Prázdný řádek (Enter) tělo ukončí a cyklus se provede.

**Ukončení interpretu**
`Ctrl-D`, nebo příkaz `exit()`.

**Interpret jako kalkulačka**
V interaktivním režimu napíšeš výpočet a interpret hned ukáže výsledek, `print` není potřeba.

---

## Cyklus

**Cyklus (loop)**
Opakuje skupinu příkazů vícekrát, takže je nemusíme kopírovat. Místo 48 řádků pro 12 schodů napíšeme 5.

```python
from turtle import *

for i in range(12):
    forward(20)
    left(90)
    forward(20)
    right(90)

done()
```

**Cyklus for a range**
`for i in range(12):` znamená „proveď tělo cyklu 12x“. Na konci řádku je vždy dvojtečka.

**Tělo cyklu (loop body)**
Odsazené řádky pod `for`. Opakují se. Tělo končí prvním řádkem, který už odsazený není.

```python
for i in range(3):
    print("Ahoj")
print("Konec")
```
Vypíše 3x `Ahoj` a pak jednou `Konec`, protože `print("Konec")` není odsazený, a tedy není v těle cyklu.

**Odsazení (indentation)**
Mezery na začátku řádku. V Pythonu je součástí syntaxe, ne ozdobou: určuje, co patří do těla cyklu. Ve VS Code odsazujeme klávesou Tab, editor vloží 4 mezery.
Chybějící odsazení skončí chybou `IndentationError`.

**Iterace**
Jedno provedení těla cyklu. Druhá iterace je druhé opakování.

**Proměnná cyklu (`i`)**
V každé iteraci má jinou hodnotu. `range(3)` jí postupně dá hodnoty 0, 1, 2: začíná nulou a končí **před** trojkou. Ve druhé iteraci má tedy `i` hodnotu 1.

```python
for i in range(3):
    print(i)
```
Vypíše `0`, `1`, `2`.

Cyklus si můžeme představit jako opakované přiřazení a tělo:

```python
i = 0
print(i)
i = 1
print(i)
i = 2
print(i)
```

Proměnnou cyklu můžeme použít v těle, například aby každá čára byla delší než předchozí:

```python
for i in range(40):
    forward(5 * i)
    left(90)
```

**Vlastní proměnná, která se v cyklu mění**
Stejnou spirálu nakreslíme i bez `i`, pomocí `x = x + 1` v těle cyklu:

```python
delka = 5
for i in range(40):
    forward(delka)
    left(90)
    delka = delka + 5
```
V první iteraci se spočítá `5 + 5`, tedy 10, a štítek `delka` se přelepí na 10. Ve druhé `10 + 5`, tedy 15, a tak dál.

---

## Naše nářadí

Jsme tesaři, kteří staví dřevostavbu (program). Každý pojem je nástroj a s každou lekcí nějaký přibude.

- **kladivo a hřebíky**: lineární provádění, hřebík po hřebíku, příkaz po příkazu
- **tesařská tužka**: proměnná, poznamenám si míru a pak ji používám
- **hřebíkovačka**: cyklus, stejná akce mnohokrát, rychle a bez únavy
