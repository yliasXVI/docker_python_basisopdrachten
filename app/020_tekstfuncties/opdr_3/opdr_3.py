# Opdracht 3 tekstfuncties
# Naam student: Ylias Kok
# Groep: 4ITX


#Optie 1 Simpel maar effectief wel veel print functies
print("     *      " * 5)
print("    ***     " * 5)
print("   ******   " * 5)
print("  ********  " * 5)
print(" ***********" * 5)
print("     ***    " * 5)
print("     ***    " * 5)
print("     ***    " * 5)


#Optie 2 iets minder simple maar inplaats van meerdere print fucties heb ik hier meerdere strings gebruikt om deze vervolgens in 1 print functie te laten tonen.
layer_one =   "     *      " * 5
layer_two =   "    ***     " * 5
layer_three = "   ******   " * 5
layer_four =  "  ********  " * 5
layer_five =  " ***********" * 5
layer_six =   "     ***    " * 5
layer_seven = "     ***    " * 5
layer_eight = "     ***    " * 5

kerstboom = (f'{layer_one}\n{layer_two}\n{layer_three}\n{layer_four}\n{layer_five}\n{layer_six}\n{layer_seven}\n{layer_eight}')
print(kerstboom)

