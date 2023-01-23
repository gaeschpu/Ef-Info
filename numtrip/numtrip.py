import random

feld= [[2,4,2,4,2],[4,2,8,8,8],[4,8,4,4,4],[2,4,4,8,8],[8,4,8,16,32]]
def spielfeld():
    ynnummer= 1
   
    print('          1      2      3      4      5')

    for y in feld:
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
        ynnummer=ynnummer+1
        print('      |      |      |      |      |      |')
    print('      +------+------+------+------+------+')
   

    




"""
def eingabe_1():
    
    val=False
    while not val:
        try:
            eingabe=input('Welche Spalte soll ausgewählt werden? ')
            eingabe=transform_eingabe(eingabe)
            valid= eingabe is not None
        except:
            print('wissen sie nicht was eine Zahl ist?')
    return(eingabe)
        
        if eingabe <0 or eingabe >4:
            val=True 
        else:
            print('Wissen sie nicht was eine Zahl ist?')
            val=False

"""
        
def eingabe():
    x = input('Welche Spalte soll ausgewählt werden? ')
    try:
            x = int(x)
    except:
        print('Wissen sie nicht was eine Zahl ist?')
        return False

    y = input('Welche y soll ausgewählt werden? ')
    try:
        y = int(y)
    except:
        print('Wissen sie nicht was eine Zahl ist?') 
 
 
    return (x - 1, y - 1)

def aufdecken(zeile, spalte, zahl):
# Rahmenbedingungen
    if zeile < 0 or zeile > 4:
        return False
    if spalte < 0 or spalte> 4:
        return False
# Feldüberprüfung
    if feld[zeile][spalte] == zahl:
        feld[zeile][spalte] = - 1
        aufdecken(zeile + 1, spalte, zahl) # unten 
        aufdecken(zeile - 1, spalte, zahl) # oben 
        aufdecken(zeile, spalte + 1, zahl) # rechts 
        aufdecken(zeile, spalte - 1, zahl) # links return True
    else:
        return False
""""
def nachunten(): # verschiebt die 0 von aufedcken nach oben  
    for a in range(5):
        for b in range(4,0,-1):# weil es von 4 nach o zählen muss 
            for j in range(5):
                if feld[a][b]==0: 
                    feld[a][b]=feld[a-1,b]# -1 dass es das obere Feld nimmt 
                    feld[a-1,b]=0 #so wird das obere Feld auf 0 gesetzt 

def aufüllen(): # die 0 wird mit einer random zahl aus ersatzzahlen aufgefüllt 
    ersatzzahlen=[1,2,4]
    for a in range(0,5):#von 0 bis fünf rauf 
        for b in range(4,-1,-1):
            if feld==0: 
                feld[a][b]= random.choice(ersatzzahlen)
"""




"""
"""
def process(col, row): # col= kollone row= x 
    feld[row][col] = 0 #auf dem spielfeld kollone[] x[] auf null setzen
"""




def aufdecken (x, y, zahl):
# Rahmenbedingungen
    if y < 0 or y > 4:
        return False
    if x < 0 or x> 4:
        return False
#Feldüberprüfung
    if feld[y][x] == zahl:
        feld[y][x] = -1
        aufdecken(y + 1, x, zahl) # unten aufdecken 
        (y - 1, x, zahl) # oben aufdecken
        (y, x + 1, zahl) # rechts aufdecken
        (y, x - 1, zahl) # links
        return True
    else:
        return False


def play():
    spielfeld()
    while True:
        x, y = eingabe()
        zahl = feld[x][y]
        aufdecken(x, y, zahl)
        #nachunten()
        #aufüllen()
spielfeld()
play()