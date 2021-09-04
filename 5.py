sueldo = int(input("Digite el sueldo base del trabajador: "))


valor1 = (sueldo * (1 / 100))
valor2 = (sueldo * (4 / 100))
valor3 = (sueldo * (0.5 / 100))
valor4 = (sueldo * (5 / 100))


print("ley de politica pública: ", valor1)
print("seguro social: ", valor2)
print("seguro forzoso: ", valor3)
print("caja de ahorro", valor4)

total = sueldo - (valor1 + valor2 +valor3 + valor4)

print("El monto total a pagar al trabajador es: ", total)