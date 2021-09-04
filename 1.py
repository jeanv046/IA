

presion = int(input("Digite la presion:"))
volumen = int(input("Digite la volumen:"))
temperatura = int(input("Digite la temperatura:"))


masa = (presion * volumen) / (0.37 * (temperatura+460))

print("La masa es: ", masa)