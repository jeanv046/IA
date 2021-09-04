minicial = int(input("Cual es el monto incial? : "))
mfinal = int(input("Cual es el monto final? : "))


if minicial > mfinal:
    resta = mfinal - minicial
    resta = resta * -1
    total = (resta * (20 / 100))
    suma = resta + total
    print("Costo de la llamada: $", suma)


