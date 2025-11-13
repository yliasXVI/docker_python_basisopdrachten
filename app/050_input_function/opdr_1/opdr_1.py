# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

a = int(input("Lengte van de eerste zijde \n"))
b = int(input("Lengte van de tweede zijde \n"))

x = ((a) **2)
y = ((b) **2)
z = (math.sqrt(x + y))

print(z)
