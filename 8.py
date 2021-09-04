horas = int(input("cuantas horas trabajo? : "))

total = horas * 20000

desc = (total * (5 / 100))
saldo = total - desc

print("Su descuento es de: ", desc , "Y su salfo final es: ", saldo)