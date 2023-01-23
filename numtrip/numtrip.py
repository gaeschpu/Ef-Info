1
feld= [[2,4,2,4,2],[4,2,8,8,8],[4,8,4,4,4],[2,4,4,8,8],[8,4,8,16,32]]
def spielfeld():
    zeilennummer= 1
   
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
   

    

spielfeld()


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

    y = input('Welche Zeile soll ausgewählt werden? ')
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




def play():
    spielfeld()
    while True:
        x, y = eingabe()
        zahl = feld[x][y]
        aufdecken(x, y, zahl)
        
        spielfeld()

play()