familia = int(input("Cuantos familiares son?: "))
dias = int(input("Cuantos dias van a vacacionar: "))

total = familia * 25000
total2 = familia * dias
total3 = (total2 *(12/100))

monto = total2 + total3

print("El total a pagar por la familia es: $", monto)