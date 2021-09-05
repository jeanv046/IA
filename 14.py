dias = int(input("cuantos dias estuvo hospedado?: "))
suma = 100000
if dias == 1:
    print("Su estadia tiene un costo de $100.000")
elif dias > 1:
    for i in range(dias - 1):
        suma = suma + 200000
    print("Su estadia tiene un costo de: $", suma)