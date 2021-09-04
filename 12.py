
peli = int(input("Cuantas peliculas alquilo anteriormente: "))
alquiler = int(input("Cuantos dias va alquilar la pelicula: "))

if peli > 10:
    print("El alquiler es gratis.")
else: 
    alquiler1 = alquiler * 1500
    print("El total a pagar es: $", alquiler1)
    