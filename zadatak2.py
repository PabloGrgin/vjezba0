"""U datoteci rotacije.txt nalazi se niz stringova. Jedna rotacija stringa u desno
je prebacivanje posljednjeg znaka tog stringa s kraja na početak. Na primjer,
string 'abcde' rotiran tri puta u desno daje 'cdeab', a isti string rotiran
sedam puta u desno daje 'deabc', što se vidi u samom postupku rotacije:
0: abcde
1: eabcd
2: deabc
3: cdeab
4: bcdea
5: abcde
6: eabcd
7: deabc

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Ako svaki
string pretvorimo u binarni broj tako da je slovo s parnim ASCII kodom 0, a
neparnim 1, te svaki takav niz rotiramo tako da dobijemo najveći mogući broj,
koji je najveći broj koji na taj način možemo dobiti od svih stringova u datoteci?

Na primjer, neka se datoteka sastoji od sljedećih stringova:

ABB
HDGGCT
CCBC

Iz ovih stringova možemo dobiti sljedeće rotacije (prikazane kao liste binarnih
brojeva pored kojih se nalazi decimalni prikaz tog binarnog broja):

Redak: ABB
['0', '1', '0'] 2
['0', '0', '1'] 1
['1', '0', '0'] 4
Redak: HDGGCT
['0', '0', '0', '1', '1', '1'] 7
['1', '0', '0', '0', '1', '1'] 35
['1', '1', '0', '0', '0', '1'] 49
['1', '1', '1', '0', '0', '0'] 56
['0', '1', '1', '1', '0', '0'] 28
['0', '0', '1', '1', '1', '0'] 14
Redak: CCBC
['1', '1', '1', '0'] 14
['0', '1', '1', '1'] 7
['1', '0', '1', '1'] 11
['1', '1', '0', '1'] 13

Iz ovog bi odgovor bio 56 jer to je najveći broj koji možemo dobiti iz ove datoteke
stringova. Za konverziju broja iz binarnog u decimalni oblik možete koristiti funkciju
(klasu) int (primjerice, int('1101', 2) daje 13)."""

with open ("rotacije.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

max = 0
for line in lines:
    bin = ""

    for char in line:
        if ord(char) %2 == 0:
            bin += "0"
        else:
            bin += "1"

    length = len(bin)

    for i in range(length):
        rotated = bin[-i:] + bin[:-i]
        decimal = int(rotated, 2)

        if decimal > max:
            max = decimal

print(f"{max}")