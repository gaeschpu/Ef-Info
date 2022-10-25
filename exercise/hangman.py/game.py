gesucht = 'test'

gefunden = [] #ist eine LSite, wenn man einen Buchstaben eigeben hat der ein oder mehrmals im gesuchten Wort vorkommt
falsch_geraten = []# ist eine lsite für der Buchstaben die nicht im wort vorkommen


def show():#
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
            if buchstabe in gefunden:
                print(buchstabe, end=' ')
    else:
                print('_', end=' ')
    print('')

def is_valid(inp):
    return True

def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):         #wird überprüft 
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

def auswerten(valid_inp):
    if valid_inp in gesucht:
     gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

def gewonnen(): #wenn der buchstabe richitg ist dann wird er geprintet
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True

def game_over():
    return False

def play():
    pass



