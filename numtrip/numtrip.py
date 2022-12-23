1
feld= [2,4,2,4,2],[4,2,8,8,8],[4,8,4,4,4],[2,4,4,8,8],[8,4,8,16,32]
def spielfeld():
    ynnummer= 1
    """
    print('          A      B      C      D      E')
    """
    print('          1      2      3      4      5')

    for y in feld:
        print('      +------+------+------+------+------+')
        print('      |      |      |      |      |      |')
        print(f'   {(ynnummer)}  ', end='')
        for zelle in y:
            if zelle >= 10000:
                print(f'| {(zelle)}', end='')
            elif zelle >= 1000:
                print(f'| {(zelle)} ', end='')
            elif zelle >= 100:
                print(f'|  {(zelle)} ', end='')
            elif zelle >= 10:
                print(f'|  {(zelle)}  ', end='')
            else:
                print(f'|   {(zelle)}  ', end='')
        print('|')
        ynnummer=ynnummer+1
        print('      |      |      |      |      |      |')
    print('      +------+------+------+------+------+')
    

spielfeld()
"""
def eingabe():
    #eingabe= input("Geben sie eine Zahl ein: ")
    x,y=input("Geben sie zwei zahlen ein")
    try:
        eingabe = int(eingabe)
    except:
        print('Das ist keine Zahl!')
    

eingabe()
"""
def eingabe():
    
    x = input('Welche x soll ausgewählt werden? ')
    try:
            x = int(x)
    except:
        print('Wissen sie nicht was eine Zahl ist?')

    y = input('Welche y soll ausgewählt werden? ')
    try:
        y = int(y)
    except:
        print('Wissen sie nicht was eine Zahl ist?')

    return x, y
"""
    if y <1 or y > 5: 
        print('Du bist ein Idiot!!Muss zwischen 1-5 sein!!!')
              
    else:
        return y

    #x und y fürfen nicht ü5 u1 sein
    if y <1 or y > 5: 
        print('Du bist ein Idiot!!Muss zwischen 1-5 sein!!!')
              
    else:
        return y
    
    if x <1 or x > 5: 
        print('Du bist ein Idiot!!Muss zwischen 1-5 sein!!!')
              
    else:
        return x

    return (x - 1, y - 1)




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
        zahl= feld[x-1][y-1]
        aufdecken(x, y, zahl) 
        spielfeld()

play()