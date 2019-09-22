# Hackathon - Lessons learnt

## Vorbereitungen

### Raspberry Pi

* SD Card mit Raspberian (Fullversion) installiert mitbringen
  * oder ein erprobtes Programm und das Image schon runter geladen
* Displays funktionieren erst nach konfiguration und nach installation von Paketen/gits ....
  * daher einfach auf die ```boot``` partition gehen und dort eine leere Datei mit Namen ```ssh``` erstellen
    dadurch wird ssh aktiviert
* Um den Pi zu finden, kann mit ```nmap``` nach der MAC von Raspberry PIs  gesucht werden. Durch abtrennen vom Netz kann geprüft werden, welche Addressen dazu kommen...
* Standard _User_ des Pi ist ```pi``` mit dem passwort ```raspberry```, da jeder mit nmap die Pis finden kann, sollte das passwort schnell mit ```passwd``` geändert werden.
* Das Layout der Pins kann als ```BCM``` oder als ```Board```
  * ```BCM```: nimmt die Benennung der GPIO pins 
  * ```Board```: nimmt die Nummer des Pins



![Layout](http://webofthings.org/wp-content/uploads/2016/10/pi-gpio.png)



### Bootable Sticks

Es lohnt sich immer noch ein stabiles extra linux auf einem Stick mitzuführen. Damit lassen sich dann auch die SD Karten der Pis manipulieren!!

* Bootable Ubuntu, Mint, ... Stick



### Flash Speicher

Manchmal ist es per Stick einfach schneller als per Netz. Auch können die 3D Drucker oft nur Sticks lesen und haben keine Netzwerkanbindung

* Leere USB Sticks
* Externe SSDs



### Kleben

Ein bisschen was eigenes zu haben, spart Zeit und Mühen!

* Tesafilm (Handreißbar)
* Print Stift
* Duck-Tape
* _alles andere haben sie da_



### Programmiersprachen

Skriptsprachen wie Python oder Javascript (z.b. als nodejs) machen einem das leben deutlich leichter.
Schnelle Prototypen ohne Betrachtung von Edgecases sind Ideal für einen Hackathon!!



* bei nodejs ist ```graphiql``` unglaublich praktisch
* python kann mal eben queries und requests senden



