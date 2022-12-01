feld= [2,4,2,4,2],[4,2,8,8,8],[4,8,4,4,4],[2,4,4,8,8],[8,4,8,16,32]
def spielfeld():
    zeilennummer= 1
    """
    print('          A      B      C      D      E')
    """
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
            else:
                print(f'|   {(zelle)}  ', end='')
        print('|')
        zeilennummer=zeilennummer+1
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
    x = input('Welche Spalte soll ausgewählt werden? ')
    x = int(x)
    y = input('Welche Zeile soll ausgewählt werden? ')
    y = int(y)
    return (x - 1, y - 1)


def process(col, row): # col= kollone row= spalte 
    spielfeld[row][col] = 0 #auf dem spielfeld kollone[] spalte[] auf null setzen

def play():
    spielfeld()
    while True:
        x, y = eingabe()
        process(x, y)
        spielfeld()

play()