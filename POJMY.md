# Slovníček pojmů – Úvod do programování

Pojmy z lekcí 1–4. Slovníček se bude průběžně doplňovat.

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
- měli bychom vynechat diaktritiku
- měl by vystihovat význam proměnné, nebojte se delších názvů


Platné: `delka`, `delka_schodu`, `x2`
Neplatné: `2x`, `delka schodu`, `delka-schodu`

**x = x + 1**
Vezmi současnou hodnotu `x`, přičti 1 a výsledek ulož zpět do `x`. Nejde o rovnici: `=` tu znamená „ulož“.

```python
x = 5
x = x + 1
print(x)  # vypíše 6
```

**Proč proměnné u schodů**
Když je délka schodu v proměnné, změníš ji na jednom místě a změní se všechny schody. Bez proměnné bys musel/a přepsat každé číslo zvlášť.

---

## Želva

**Želva (turtle)**
Knihovna Pythonu pro kreslení. Želva se pohybuje po obrazovce podle příkazů a za sebou kreslí čáru (například dopředu o určitou vzdálenost, otočení vlevo nebo vpravo o daný úhel).

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

**Ukončení interpretu**
`Ctrl-D`, nebo příkaz `exit()`.

**Interpret jako kalkulačka**
V interaktivním režimu napíšeš výpočet a interpret hned ukáže výsledek, `print` není potřeba.
