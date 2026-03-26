# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings=[]

# Hier de rest van jouw code...
for topping in toppings:
    beschikbare_toppings.append(topping[0])

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

for topping in toppings:
    if topping[0] == keuze:
        prijs = topping[1]
        print(f"Je hebt {keuze} gekozen") 
        print(f"De prijs is {prijs}")
        break
    else:
        print("Uw keuze zit niet in ons assortiment")
    break