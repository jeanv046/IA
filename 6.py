palabras = int(input("cuantas palabras colocara?   :"))
tam = int(input("Que tamaño tendra el aviso (cm)?  :"))
color = int(input("Cuantos colores tendra el aviso :"))


total1 = palabras * 20000
total2 = tam * 15000
total3 = color * 25000

suma = total1+total2+total3

print("El aviso tiene un costo de: ", suma)