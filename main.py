import math

OPERATORLAENGE = 1
OPERATORADDITION = "+"
OPERATORSUBTRAKTION = "-"
OPERATORDIVISION = ":"
OPERATORMULTIPLIKATION = "*"
ZEILENABSTAND = "\n\n"

def output(string):
    print (string)

def multiplikationMitEingabe():
    output("erste Zahl:")
    temp_faktor1: int = input()
    output("\nzweite Zahl:")
    temp_faktor2: int = input()
    multiplikation(temp_faktor1, temp_faktor2)


def multiplikation(faktor1, faktor2):

    ergebnis = int(faktor1) * int(faktor2)

    aufgabenlaenge = len(str(faktor1) + str(faktor2)) + OPERATORLAENGE
    resultlength = len(str(ergebnis))
    anzahl_zeilen_fuer_zwischenrechnungen = len(str(faktor2))

    output(str(faktor1) + "*" + str(faktor2))
    output('-' * aufgabenlaenge) #malt den Strich unter der Rechnung

    for x in str(faktor2):
        temp_result = int(faktor1) * int(x) * (10 ** (anzahl_zeilen_fuer_zwischenrechnungen - 1)) #"-1" Am Ende, da die Einerstelle 10⁰ sein muss
        anzahl_leerzeichen_einruecken_von_links = aufgabenlaenge - len(str(temp_result))

        output((anzahl_leerzeichen_einruecken_von_links * " ") + (str(temp_result)))
        anzahl_zeilen_fuer_zwischenrechnungen = anzahl_zeilen_fuer_zwischenrechnungen - 1

    output('-' * aufgabenlaenge) #malt den Strich unter der Rechnung
    anzahl_leerzeichen_einruecken_von_links = aufgabenlaenge - len(str(ergebnis))
    output((anzahl_leerzeichen_einruecken_von_links * " ") + (str(ergebnis)) + ZEILENABSTAND) #gibt das Ergebnis richtig eingerueckt aus


def division(dividend, divisor):
    ergebnis = dividend / divisor
    rest = dividend % divisor
    output(str(dividend) + ":" + str(divisor) + "=" + str(int(ergebnis)) + " Rest: " + str(rest)) # gibt die Rechnung aus

    aufgaben_laenge_mit_ergebnis = len(str(dividend) + str(divisor) + str(ergebnis) + str(rest)) #Addiert die Länge der Zahlen
    aufgaben_laenge_mit_ergebnis = aufgaben_laenge_mit_ergebnis + len(" Rest: " + str(2 * OPERATORLAENGE)) #Addiert die Schrift dazu

    output('-' * aufgaben_laenge_mit_ergebnis) #malt den Strich unter der Rechnung

    for zahl in str(dividend):
        runtergezogene_zahl = str(zahl)

        #if (int(runtergezogene_zahl) / int(divisor)) > 0:


    output(ZEILENABSTAND) #gibt ZEILENABSTAND nachd er Rechnung aus. Soll die einzelnen Rechnungen von einander trennen




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    multiplikation(5, 12345)

    division(12345, 5)
    division(465733, 7)

    # while True:
    #     multiplication()
    #     print("Nächste Aufgabe?\n1: Ja\n2: Programm verlassen")
    #     auswahl = int(input())
    #
    #     if auswahl == 1:
    #         calculate()
    #         auswahl = 0
    #     elif auswahl == 2:
    #         break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/