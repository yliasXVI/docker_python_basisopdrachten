# Opdracht 2
# Naam student: Ylias Kok
# Groep: 4ITX

# De my_string de zin warvan we zo de t gaan optellen.
my_string = "Tinus gaat op zijn tandem naar de hottentottententoonstelling"
# t_count zorgt dat de letters eerst naar een .lower gaan zodat de T van tinus dus lowercase wordt en daarna de .count om de letter t op te tellen.
t_count = my_string.lower().count('t')
# Hier wordt de zin in een f-string neergezet om de uitkomst van de .count toe te voegen aan de zin.
print(f'De letter "t" komt {t_count}x voor in my_string')

