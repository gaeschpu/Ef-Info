zahlen = []
primzahlen = []#liste 
primzahl_bool = True

for counter in range(2, 100000):
    zahlen.append(counter)#zahl zu liste hinzufügen 


for zahl in zahlen:
    if primzahl_bool:
        for primzahl in primzahlen:
            if zahl % primzahl == 0:
                primzahl_bool = False

    if primzahl_bool:
        primzahlen.append(zahl)#zu liste hinzufügen
    primzahl_bool = True

print(primzahlen)
