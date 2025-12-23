# Del 2 i Juljakten

Här finns en skiffertext med ett medelande som kan hjälpa er framåt.
Det finns även ett par program för att hjäpa er på traven att kunna lösa skiffret.
Om man vill går det att lösa med penna och papper men en dator är ju att rekomendera.

## Nyckelfilen

Nykelfilen som används i `dekryptering.py` programmet ser ut som följande:
```
A-B
B-D
K-Z
...
```
I exemplet så kommer A att bytas mot ett B, B mod D och K mot Z. Bara de boktäver som är i den vänstra spalten av nyckelfilen kommer att bytas ut i skiffertextfilen.

## Köra programmen
För att dekryptera eller delvis dekryptera texten.
```
python3 dekryptering.py [nyckelfilen] [skiffertextfilen]
```

För att räkna antalet av varje bokstav och den relativa andelen av varje bokstav.
```
python3 räkna-bokstäver.py [skiffertextfilen]
```
