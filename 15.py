pinicial = int(input("Cuanto dinero presto?: "))

interes = (pinicial * (24 / 100))

total = pinicial + interes

div = total / 2
div2 = total / 2

cuota1 = div / 4
cuota2 = div2 / 20

print("El monto total a pagar es: $", total)
print("El valor de las cuotas especiales es: $", cuota1)
print("El valor de las cuotas ordinarias es: $", cuota2)

