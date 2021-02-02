import math

OPERATORLAENGE = 1
OPERATORADDITION = "+"
OPERATORSUBTRAKTION = "-"
OPERATORDIVISION = ":"
OPERATORMULTIPLIKATION = "*"
ZEILENABSTAND = "\n\n"

def output(string):  # Erstellt, um zu einem spaeteren Zeitpunkt die Ausgabe in eine Textdatei zu schreiben
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
    anzahl_zeilen_fuer_zwischenrechnungen = len(str(faktor2))

    output(str(faktor1) + "*" + str(faktor2))
    output('-' * aufgabenlaenge)  # malt den Strich unter der Rechnung

    for x in str(faktor2):
        temp_result = int(faktor1) * int(x) * (10 ** (anzahl_zeilen_fuer_zwischenrechnungen - 1))  # "-1" Am Ende, da die Einerstelle 10⁰ sein muss
        anzahl_leerzeichen_einruecken_von_links = aufgabenlaenge - len(str(temp_result))

        output((anzahl_leerzeichen_einruecken_von_links * " ") + (str(temp_result)))
        anzahl_zeilen_fuer_zwischenrechnungen = anzahl_zeilen_fuer_zwischenrechnungen - 1

    output('-' * aufgabenlaenge)  # malt den Strich unter der Rechnung
    anzahl_leerzeichen_einruecken_von_links = aufgabenlaenge - len(str(ergebnis))
    output((anzahl_leerzeichen_einruecken_von_links * " ") + (str(ergebnis)) + ZEILENABSTAND)  # gibt das Ergebnis richtig eingerueckt aus


def division(dividend, divisor):
    ergebnis_output = dividend / divisor  # Wird berechnet um es anzuzeigen
    rest_output = dividend % divisor  # Wird berechnet um es anzuzeigen
    output(str(dividend) + ":" + str(divisor) + "=" + str(int(ergebnis_output)) + " Rest: " + str(rest_output))  # gibt die Rechnung aus

    aufgaben_laenge_mit_ergebnis = len(str(dividend) + str(divisor) + str(ergebnis_output) + str(rest_output))  # Addiert die Länge der Zahlen
    aufgaben_laenge_mit_ergebnis = aufgaben_laenge_mit_ergebnis + len(" Rest: " + str(2 * OPERATORLAENGE))  # Addiert die Schrift dazu
    output('-' * aufgaben_laenge_mit_ergebnis) # malt einen Bindestrich unter der Rechnung

    ergebnis = ""  # wird genutzt, um die einzelenen Zahlen auf dem weg zum Gesamtergebnis zu speichern
    tempzahl = ""  # Stellt die Rechnenvariable bei den einzelnen Rechenschritten dar
    einrueckung_zwischen_rechnung = 0  # Hiermit soll die nötige Einrückung zum korrekten Darstellen mitgezaehlt werden
    tempergebnis = ""

    for zahl in str(dividend):  # geht nacheinander durch jede Zahl, die im dividend vorkommt (vlnr)
        tempzahl = tempzahl + str(zahl)

        if divisor > int(tempzahl):
            ergebnis = ergebnis + "0"
            # output(str(einrueckung_zwischen_rechnung * " ") + tempzahl)
            continue

        elif (int(tempzahl) % int(divisor)) == 0:
            zwischenergebnis = int(int(tempzahl) / int(divisor))
            ergebnis = ergebnis + str(zwischenergebnis)
            output(str(einrueckung_zwischen_rechnung * " ") + tempzahl)

            if tempzahl[0] == "0":
                for null in tempzahl:
                    if null == "0":
                        einrueckung_zwischen_rechnung = einrueckung_zwischen_rechnung + 1
                    else:
                        continue

            output(str(einrueckung_zwischen_rechnung * " ") + str(zwischenergebnis * divisor))
            output(str(einrueckung_zwischen_rechnung * " ") + '-' * len(str(int(tempzahl))))

            tempzahl = str(int(int(tempzahl) % int(divisor)))

            einrueckung_zwischen_rechnung = einrueckung_zwischen_rechnung + 1

        else:
            zwischenergebnis = int(int(tempzahl) / int(divisor))
            ergebnis = ergebnis + str(zwischenergebnis)
            output(str((einrueckung_zwischen_rechnung - (len(tempzahl) - len(str(int(tempzahl))))) * " ") + (tempzahl))
            output(str(einrueckung_zwischen_rechnung * " ") + str(zwischenergebnis * divisor))
            output(str(einrueckung_zwischen_rechnung * " ") + '-' * len(str(int(tempzahl))))

            # output(str(einrueckung_zwischen_rechnung * " ") + str((int(tempzahl) % int(divisor))) + str())
            einrueckung_zwischen_rechnung = einrueckung_zwischen_rechnung + 1
            tempzahl = str(int(int(tempzahl) % int(divisor)))

    output(str(einrueckung_zwischen_rechnung * " ") + tempzahl)

    output("Das Ergebnis ist: " + str(int(ergebnis)) + " mit Rest: " + str(int(tempzahl)))
    output(ZEILENABSTAND) # gibt ZEILENABSTAND nachd er Rechnung aus. Soll die einzelnen Rechnungen von einander trennen


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # multiplikation(5, 12345)
    # division(200, 4)
    # division(746, 7)
    # division(12345, 5)
    # division(465733, 7)
    # division(451064, 8)
    division(252546, 6)
    division(26800, 4)
    division(6048, 6)

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
