tiempo = int(input("cuantos años tienes en la empresa? : "))
suma = 0
if tiempo == 1:
    print("El bono del trabajador es: $ 100.000")
elif tiempo > 1:
    for i in range(tiempo):
        suma = suma + 120000
    print("El bono del trabajador es: $", suma)