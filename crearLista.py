
numberOfPersons = int(input("Por favor ingrese la cantidad de personas: "))

listOfAges = []

for i in range(0,numberOfPersons):
    listOfAges.append(int(input("Por favor ingrese la edad de la persona: ")))

división = sum(listOfAges) / len(listOfAges)

print(listOfAges)
print(f"El promedio de las edades es {división} años")