inv1 = int(input("(Inversionista 1)Cuanto dinero vas a invertir: "))
inv2 = int(input("(Inversionista 2)Cuanto dinero vas a invertir: "))
inv3 = int(input("(Inversionista 3)Cuanto dinero vas a invertir: "))

suma = inv1 + inv2 + inv3

porcentaje = (inv1 / suma) * 100
porcentaje2 = (inv2 / suma) * 100
porcentaje3 = (inv3 / suma) * 100

print("El porcentaje del inversionista 1 es: ", porcentaje)
print("El porcentaje del inversionista 2 es: ", porcentaje2)
print("El porcentaje del inversionista 3 es: ", porcentaje3)