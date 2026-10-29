notas = {"santilli": [], "cataldo": [], "naramjo": [], "diaz": [], "herraiz": []}
def buscar():
    apellido = input("ingrese el apellido: ").capitalize()
    if apellido in notas:
        return apellido
    print("no existe")
def ver_todas():
    for apellido, n in notas.items():
        print(apellido, n)
def ver_alumno():
    apellido = buscar()
    if apellido:
        print(apellido, notas[apellido])
def cargar():
    apellido = buscar()
    if apellido:
        notas[apellido] = [float(input(f"nota {i}: ")) for i in range(1, 6)]
menu = {1: ver_todas, 2: ver_alumno, 3: cargar}
menu1 = True
while menu1 == True:
    print("1. ver todas las notas")
    print("2. ver notas por alumno")
    print("3. cargar notas por apellido de alumno")
    print("4. salir")
    opcion = int(input("elija una opcion: "))
    if opcion == 4:
        menu1 = False
    elif opcion in menu:
        menu[opcion]()
    else:
        print("opcion invalida")
