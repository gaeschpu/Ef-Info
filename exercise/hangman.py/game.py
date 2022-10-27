from operator import truediv


gesucht = 'test'
buchstabe = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MESSAGE = [12, 9, 19, 20, 0, 18, 9, 4, 4, 12, 5]



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
    while not is_valid(buchstabe):         #wird überprüft ob es
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

#def endewenngewonnen():
    if gesucht= true 

def game_over():
    if len(falsch_geraten)== 7:
        return True
    else:
         return False

def play():
    #Ab jetzt wird das spiel proggramiert 
    while not game_over():
        buchstabe = eingabe()
        auswerten(buchstabe)
        print(buchstabe)
        show()
    if gewonnen():
        print('You won')
    else:
        print(f'Das gesuchte Wort wäre:' ,gesucht )



play()
