import random

feld= [[2,4,2,4,2],[4,2,8,8,8],[4,8,4,4,4],[2,4,4,8,8],[8,4,8,16,32]]
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
   

    

def eingabe_x(): # EIngabe des Benutzers
    valid=False
    while not valid:
        try:
            x=input('Geben sie eine Spalte ein ')
            if not x.isnumeric():
                continue# macht dass es wieder von vorne (while) anfängt
            x=int(x)
            if x<0 or x>5:# muss doch grösser als O und kleiner als 5 sein?
                print('Zahl muss zwischen 1 und 5 sein')
                continue
            valid=True

        except:    
            print('Sie müssen eine Zahl eingeben')
    
    
        pass
    else:
        print('Zahl muss zwischen 1 und 5 sein')
        eingabe_x()
    return(x-1)
    

def eingabe_y():
    valid=False
    while not valid:
        try:
            y=input('Geben sie eine Zeile ein ')
            if not y.isnumeric and len(y)==1:
                continue
            y=int(y)
            if y<0 or y>5:# muss doch grösser als O und kleiner als 5 sein?
                print('Zahl muss zwischen 1 und 5 sein')
                continue
            valid=True
        except:
            print('Sie müssen eine Zahl eingeben')
    
    return(y-1)
    




    

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













def aufdecken (x, y, zahl):
# Rahmenbedingungen
    if y < 0 or y > 4:
        return False
    if x < 0 or x> 4:
        return False

def aufdecken(zeile, spalte, zahl):
# Rahmenbedingungen
    if zeile < 0 or zeile > 4:
        return False
    if spalte < 0 or spalte> 4:
        return False
# Feldüberprüfung
    if feld[zeile][spalte] == zahl:
        feld[zeile][spalte] = - 1
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
        x= eingabe_x()
        y=eingabe_y()
        zahl = feld[x][y]
        aufdecken(x, y, zahl)
        aufüllen()
        nachunten()
        
        spielfeld()
play()