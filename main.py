nombres = ["abel", "luis", "jose", "carlos", "sterben", "pedro","noemi"]

edades = {
    "abel": 28,
    "luis": 25,
    "jose": 28,
    "carlos": 35,
    "sterben": 22,
    "pedro":50,
    "noemi":47
}

continuar = "s"
while continuar == "s":
    nombre_ingresado = input("Ingresa un nombre: ").lower()

    if nombre_ingresado in edades:
        print(f"{nombre_ingresado} tiene {edades[nombre_ingresado]} años.")
    else:
        print("La persona no fue encontrada.")
    
    continuar = input("Continuar buscando edades (S/N)").lower()
