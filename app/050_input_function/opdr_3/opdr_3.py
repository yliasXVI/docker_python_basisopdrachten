# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

new_list = input("Vul minimaal 5 steden in, gescheiden door komma's: ")
new_list = [item.strip() for item in new_list.split(",")]
new_list.sort(reverse=True)
print (new_list)