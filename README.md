# DuA_Prak_02
DuA Praktikum - Aufgabe 2

## Requirements
 - Ersten Argument [-avl, -hash] gibt die Datenstruktur die benutzt werden soll an
 - Letztes Argument entspricht file_name
 - Wörterbuch mit Befehlen[ins, del, search] aus datei einlesen
 - Erste zeile beginnt mit '#' und ist ein Kommentar
 - Ausgabe eine Zeile pro durchgeführte Operation
    -> "ins false", falls eingefügte Zeile schon vorhanden ist
    -> "ins true", falls Zeile erfolgreich eingefügt wurde
    -> "del false", falls zu löschende Zeile nicht vorhanden ist
    -> "del true", falls Zeile erfolgreich gelöscht wurde
    -> "search false", falls zu suchende Zahl nicht gefunden wurde
    -> "search true", falls zu suchende Zahl gefunden wurde
 - Ausgabe auf Konsole

 ## How to Test
 ### Manueller Test:
 Der Manuelle Test läuft einmal durch alle Commandos in `test.txt` und gibt das ergebnis auf der Konosle aus.
 `python main.py -avl test.txt`
 ### Automatisierter Test:
 Der Automatisierte Test läuft durch alle Testfiles in `pubInst/` und gibt aus wie viele Test fehlerfrei sind.
 -> TODO: Ausgabe welche Test an welcher Stelle nicht funktionieren.
 `python test.main.py`
