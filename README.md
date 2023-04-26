# Matte Tentamen Vår 2023 Oppgave 4
Her er slik jeg løste oppgave 4 på matte tentamen vår 2023:

# Setup
For å laste ned denne koden til din PC må du trykke på "Code" også "Download ZIP".
Hvis du ikke vil laste den ned, kan du bruke den i online versjonen av Visual Studio Code ved å gå til [denne linken](https://github.dev/HermanErKu/tentamen_oppgave4).

Skal du laste ned koden er det viktig at du også laster ned Python libariene som koden bruker.

[Oppgave_a.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_a.py) bruker ingen Python libraries.

[Oppgave_b.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_b.py) bruker 2 forskjellige Python libraries.
Disse kan lastes ned ved å kjøre disse kommandoene i terminalen:
pip install keyboard
pip install turtle


# Hvordan bruke
### [Oppgave_a.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_a.py)
Denne koden er veldig enkel å bruke. Den finner de 10 første tallene i et mønster.
Hvis du vil finne mere enn kun de 10 første tallene, så endrer du bare loopen i koden.

Hvis du vil finne de første 20 tallene, så endrer du [linje 3](https://github.com/HermanErKu/tentamen_oppgave4/blob/cd576652e32e32c90af51d5822927572363c4640/oppgave_a.py#L3) i koden fra:
for i in range(10)
Til:
for i in range(20)


### [Oppgave_b.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_b.py)
Denne koden tegner den n'te figuren i mønsteret. I denne koden er det noen innstillinger du kan endre på.

Hvis du vil finne figuren til den 5. figuren i mønsteret, så endrer du [linje 12](https://github.com/HermanErKu/tentamen_oppgave4/blob/cd576652e32e32c90af51d5822927572363c4640/oppgave_b.py#L12) i koden fra:
n = 3
Til:
n = 5


Det går også an å endre på høyden som figuren starter på.
Hvis du vil at figuren skal starte litt høyere kan du endre [linje 13](https://github.com/HermanErKu/tentamen_oppgave4/blob/cd576652e32e32c90af51d5822927572363c4640/oppgave_b.py#L13) i koden fra:
height = 10
Til:
height = -10


Du kan også endre størrelsen på firkantene i figuren. Det kan være lurt å gjøre firkantene mindre hvis du skal lage en stor figur.
Hvis du vil gjøre firkantene litt mindre så kan du endre [linje 14](https://github.com/HermanErKu/tentamen_oppgave4/blob/cd576652e32e32c90af51d5822927572363c4640/oppgave_b.py#L14) i koden fra:
squareSize = 35
Til:
squareSize = 20


# Hvordan koden funker:
### [oppgave_a.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_a.py)
Dette er en veldig enkel og kort kode. Det eneste jeg gjorde her var å kode i Python den pseudokoden vi fikk utdelt i oppgaven.

### [oppgave_b.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_b.py)
Denne koden lager figurer ut ifra koden i [oppgave_a.py](https://github.com/HermanErKu/tentamen_oppgave4/blob/main/oppgave_a.py).

Her er hvordan den gjør det:
1. Den lager 3 firkanter, 2 på hver sin side av figuren og en på toppen i midten av figuren.
2. Etter dette fyller den inn med ett (n+1)*(n+1) stort kvadrat i midten av figuren.
3. Den viser dette på et popup vindu.
4. Trykk på 'q' for å komme ut av popup vinduet.

# Skjermbilder:
