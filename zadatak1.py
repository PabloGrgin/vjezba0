"""U datoteci sifre.txt nalazi se niz stringova koji se sastoje samo od malih
slova. Te stringove treba transformirati na sljedeći način: ASCII kood svakog
slova treba umanjiti za 10. Ako je rezultat manji od 97 (malo slovo 'a') onda
treba umanjivanje nastaviti od kraja (to jest, od slova 'z'). Na primjer, slovo
'e' umanjeno za 10 daje slovo 'u'.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko
stringova u datoteci sifre.txt nakon transformacije sadrži barem jedno od slova
a, e, i, o ili u?"""


with open ("sifre.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0

for line in lines:

    transformed = []

    for letter in line:
        ascii_val = ord(letter) - 10

        if ascii_val < 97:
            ascii_val += 26
        
        transformed.append(chr(ascii_val))

    for letter in transformed:
        if letter in vowels:
            count += 1
            break

print(f"{count}")

        
