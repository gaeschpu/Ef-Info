board = [
    [2, 4, 1, 8, 8],
    [4, 2, 8, 2, 1],
    [4, 4, 8, 4, 2],
    [2, 8, 4, 4, 1],
    [2, 4, 4, 4, 4]
]

def index_zeile(n):
    print('   ', end='')
    for i in range(n):
        print(f' {i + 1} ', end='')
    print('')

def strich_horizontal(n):
    print('  ', end='')
    for i in range(n):
        print('---', end='')
    print('-')

def print_zelle(z):
    print(f'| {z}', end='')

def print_zeile(zeile_nr):
    print(f'{zeile_nr + 1} ', end='')
    for zelle in board[zeile_nr]:
        print_zelle(zelle)
    print('|')

def show():
    index_zeile(len(board[0]))
    for i in range(len(board)):
        strich_horizontal(len(board[i]))
        print_zeile(i)
    strich_horizontal(len(board[0]))

def eingabe():
    x = input('Welche Spalte soll ausgewählt werden? ')
    x = int(x)
    y = input('Welche Zeile soll ausgewählt werden? ')
    y = int(y)
    return (x - 1, y - 1)

def process(col, row):
    board[row][col] = 0

def play():
    show()
    while True:
        x, y = eingabe()
        process(x, y)
        show()

play()