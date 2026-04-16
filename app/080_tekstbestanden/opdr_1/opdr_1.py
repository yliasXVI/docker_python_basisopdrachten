# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
lst = []

Question1 = ('Wat vind je van de huidige regering?')
print(Question1)
lst.append(Question1)
answer = input ()

if answer == "":
    print ('Geen anwoord ingevuld')
    lst.append(answer)
else: 
    print (f"Bedankt voor jouw mening: {answer}")
    lst.append(answer)

Question2 = ('Wat vind je van de Python-lessen tot nu toe?')
print(Question2)
lst.append(Question2)
answer = input ()

if answer == "":
    print ('Geen anwoord ingevuld')
    lst.append(answer)
else: 
    print (f"Bedankt voor jouw mening: {answer}")
    lst.append(answer)

Question3 = ('Wat vind jij de mooiste stad van Nederland?')
print(Question3)
lst.append(Question3)
answer = input ()

if answer == "":
    print ('Geen anwoord ingevuld')
    lst.append(answer)
else: 
    print (f"Bedankt voor jouw mening: {answer}")
    lst.append(answer)

        
fo = open('newtext.txt', 'wt')
for answer in lst:
    fo.write(answer + "\n")

fo.close()


