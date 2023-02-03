import random

#feld= [[4,4,2,2,8],[4,2,2,8,8],[4,8,4,4,4],[2,2,4,8,8],[8,8,4,4,8]]
feld = [[], [], [], [], []]
#feld = [[16,16,4,8,16],[2,4,8,16,1],[4,8,16,1,2],[8,16,1,2,4],[16,1,2,4,8]]

def generiereFeld():
    zahlen=[1,2,4,8]
    for i in range(5):
        for j in range(5):
            feld[i].append(random.choice(zahlen))

def spielfeld():
    zeilennummer=1
   
    print('          1      2      3      4      5')

    for zeile in feld:
        print('      +------+------+------+------+------+')
        print('      |      |      |      |      |      |')
        print(f'   {(zeilennummer)}  ', end='')

        for zelle in zeile:
            
            if zelle >= 10000:
                print(f'| {(zelle)}', end='')
            elif zelle >= 1000:
                print(f'| {(zelle)} ', end='')
            elif zelle >= 100:
                print(f'|  {(zelle)} ', end='')
            elif zelle >= 10:
                print(f'|  {(zelle)}  ', end='')
            elif zelle <0 :
                print(f'|      ', end='')# das ersetzt DAS fELD WENN ES UNTER 0 ist. 
            else:
                print(f'|   {(zelle)}  ', end='')
        print('|')
        zeilennummer=zeilennummer+1
        print('      |      |      |      |      |      |')
    print('      +------+------+------+------+------+')

def eingabe(zeileoderspalte): # Eingabe des Benutzers
    valid=False
    while not valid:
        try:
            value=input(f'Geben sie eine {zeileoderspalte} ein: ')
            if not value.isnumeric():
                continue# macht dass es wieder von vorne (while) anfängt
            value=int(value)
            if value<0 or value>5:# muss doch grösser als O und kleiner als 5 sein?
                print('Zahl muss zwischen 1 und 5 sein!')
                continue
            valid=True

        except:    
            print(f'Sie müssen eine {zeileoderspalte} eingeben!')
    
    return(value-1)
    

def nachunten(): # verschiebt die 0 von aufedcken nach oben  
    for j in range(5):
        for a in range(4,0,-1):# weil es von 4 nach 1 zählen muss 
            for b in range(5):
                if feld[a][b]==0: 
                    feld[a][b]=feld[a-1][b]# -1 dass es das obere Feld nimmt 
                    feld[a-1][b]=0 #so wird das obere Feld auf 0 gesetzt 

def auffüllen(): # die 0 wird mit einer random zahl aus ersatzzahlen aufgefüllt 
    ersatzzahlen=[1,2,4,8]
    for a in range(0,5):#von 0 bis fünf rauf 
        for b in range(4,-1,-1):
            if feld[a][b]==0: 
                feld[a][b] = random.choice(ersatzzahlen)


#
def überprüfung(): # ausprobiert(Jodoks Code) würde machen dass man keine alleinstehende zahl auswählen kann
    partner = False
    for a in range(5):
        for b in range(5):
            if a > 0:
                if feld[a][b] == feld[a - 1][b]:
                    partner = True
            if a < 4:
                if feld[a][b] == feld[a + 1][b]:
                    partner = True
            if b > 0:
                if feld[a][b] == feld[a][b - 1]:
                    partner = True
            if b < 4:
                if feld[a][b] == feld[a][b + 1]:
                    partner = True
    if partner == True:
        return True
    else:
        print('Keine Nachbarszahl, gib neue Zahl ein!')
    return partner

def aufdecken(zeile, spalte, zahl):
# Rahmenbedingungen
    if zeile < 0 or zeile > 4:
        return False
    if spalte < 0 or spalte> 4:
        return False
# Feldüberprüfung
    if feld[zeile][spalte] == zahl: # kontoliiert ob es rundum das Feld das man ausgewählt hat eine gleiche zahl hat
        feld[zeile][spalte] = 0
        aufdecken(zeile + 1, spalte, zahl) # unten .
        aufdecken(zeile - 1, spalte, zahl) # oben 
        aufdecken (zeile, spalte + 1, zahl) # rechts
        aufdecken (zeile, spalte - 1, zahl) # links 
        return True
    else:
        return False

def play():
    spielfeld()
    while True:
        x= eingabe('zeile')
        y=eingabe('spalte')
        zahl = feld[x][y]
        if überprüfung() == True:
            aufdecken(x, y, zahl)
            feld[x][y] = zahl*2
            nachunten()
            auffüllen()
        spielfeld()
generiereFeld()
play()