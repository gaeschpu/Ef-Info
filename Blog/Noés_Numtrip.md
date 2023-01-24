# Numtrip in Arbeit 
*** 
[image](numtrip-2a8a9be4a578524153597160fd864606)
Ist doch ein simples Spiel, auf Zahlen drücken und sie Fusionieren, genau so kam mir numtrip vor.
Doch als wir mit der Programmation begannen merkte ich schnell, dass es nicht so einfach ist wie es beim spielen aussieht. 
Schon nur das Spielfeld mit gesetzen zahlen die sich nicht bewegen haben mir mühe bereitet. 
Doch ich bin zuversichtlich dass es irgendwann mal spielbar sein wird;)
**24.01.2023**
24h vor der Abgabe des Games bin zwar zuversichlich dass das Game spielbar sein wird, doch wie gut und wie schön es dann wirklich ist werden wir ja sehen. 
## Zum Game: 
Um es überhaupt spielen zu können müssen Sie: 
1. [Visual studio Code](https://code.visualstudio.com/download) installieren.
2. [Phyton](https://www.python.org/downloads/) installieren
3. [Diesen Code](https://github.com/gaeschpu/Ef-Info/blob/main/numtrip/finalnumtrip.py) kopieren und in Visual Studio Code einfügen.
4. Nun müssen sie nur noch oben rechts auf den Run Knopf und schon sind breit zu spielen.

## Top-Down entwurf
***
Hier könnt ihr sehen was ich mir so als Grundidee und Plangun vorgenommen hatte:
[image](Screenshot_20230124_212259)

## Code erklärung
***
Hier erkläre ich euch einen kleien Auschnitt aus meinem Code:
``` 
def eingabe_x(): 
    valid=False                             >Hier wird bestimmt dass Valid = Falsch ist, somit wird die definition solange laufen bis valid=True ist
    while not valid:
        try:
            x=input('Geben sie eine Spalte ein ')
            if not x.isnumeric():          > Da wird überprüft ob x eine Zahl ist
                continue
            x=int(x)
            if x<0 or x>5:                 > x muss über null und unter 6 sein, da das Spielfeld ja 5 auf 5 Felder ist
                print('Zahl muss zwischen 1 und 5 sein')
                continue
            valid=True                      > Ist alles das überprüft und korrekt ist alles Valid also Valid=True

        except:    
            print('Sie müssen eine Zahl eingeben') > Doch da es auch immer Menschen git die es nicht tscheggen, muss man erwarten dass alles mögliche eingeben wird, deshald das except...
    
    return(x-1)

``` 
## Tipps falls ihr es nachproggramieren wollt
***
Ich würde euch wirklich zu herzen legen einen guten **Top Down Entwurf** zu machen, da es hilft ein bisschen den überblick zu behalten was man noch alles machen muss. Ein anderer Tipp den ich euch geben kann wäre, einfach mal ein **Grundspiel programmieren** und am Schluss dann alles zu Opimieren. Ich habe viel zu lange am Spielfeld herumgetüftelt anstatt einfach mal eines zu machen und dann am Schluss zu optimieren.

