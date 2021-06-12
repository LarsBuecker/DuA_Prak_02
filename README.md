# DuA_Prak_02
DuA Praktikum - Aufgabe 2

## Requirements
 - Ersten Argument [-avl, -hash] gibt die Datenstruktur die benutzt werden soll an
 - Letztes Argument entspricht file_name
 - Wörterbuch mit Befehlen[ins, del, search] aus datei einlesen
 - Erste zeile beginnt mit '#' und ist ein Kommentar
 - Ausgabe eine Zeile pro durchgeführte Operation <br/>
    -> "ins false", falls eingefügte Zeile schon vorhanden ist <br/>
    -> "ins true", falls Zeile erfolgreich eingefügt wurde <br/>
    -> "del false", falls zu löschende Zeile nicht vorhanden ist <br/>
    -> "del true", falls Zeile erfolgreich gelöscht wurde <br/>
    -> "search false", falls zu suchende Zahl nicht gefunden wurde <br/>
    -> "search true", falls zu suchende Zahl gefunden wurde <br/>
 - Ausgabe auf Konsole <br/>


 ## How to Test
 ### Manueller Test:
 Der Manuelle Test läuft einmal durch alle Commandos in `test.txt` und gibt das ergebnis auf der Konosle aus. 
 <br/>

 Kommando: <br/>
 `python main.py -avl test.txt`
 ### Automatisierter Test:
 Der Automatisierte Test läuft durch alle Testfiles in `pubInst/` und gibt aus wie viele Test fehlerfrei sind. <br/>
 -> TODO: Ausgabe welche Test an welcher Stelle nicht funktionieren.
 <br/>

 Kommando: <br/>
 `python test.main.py`
