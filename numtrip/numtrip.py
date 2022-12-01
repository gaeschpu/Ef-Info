zahlen_matrix = [
    [2, 4, 16, 8, 8],
    [4, 26, 8, 2, 1],
    [4, 4, 16, 4, 2],
    [2, 8, 1, 4, 1],
    [2, 4, 4, 4, 4]
]

#print(zahlen_matrix)
def obere_zeile():
    print(f"      1      2      3      4      5    ")

def rand():
    print(f"  +------+------+------+------+------+")

def leer_zeile():
    print(f"  ¦      ¦      ¦      ¦      ¦      ¦")


def dazwischen_zahl(zahlenliste,nr):
    print(f"{nr} ¦", end = '')
    for zahl in zahlenliste:
        if (zahl<10):
            print(" ", end = '')
        print("  ", end = '')
        if (zahl<0):
            print(" ",end = '')
        else:
            print(zahl, end = '')
        print("  ¦", end = '')
    print("")


def eingabe():
    x,y=input("Welches Feld soll geleert werden: ").split()
    return int(x),int👍
 
def eingabe_ueberprüfen(zahl):
    try:
        if zahl < 0:
            raise 'Achtung Negative Zahl'
        if zahl.isalpha():
            raise 'Achtung Keine Zahl'
    except:
        return False



def auswerten(x,y):
    obere_zeile()
    rand()
    zahlen_matrix[x-1][y-1]=-1
    for i in range(5):
        leer_zeile()
        dazwischen_zahl(zahlen_matrix[i],i+1)
        leer_zeile()
        rand()
while True:
    x,y=eingabe()
    eingabe_ueberprüfen(x)
    eingabe_ueberprüfen
    auswerten(x,y)