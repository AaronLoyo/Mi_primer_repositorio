import random

def Interfaz():
    print("""Bienvenido querido usuario, aqui tiene las opciones
    0): Salir del programa
    1): Comenzar el programa""")

def inicioPrograma():
    print("Elejiste iniciar el programa :D")
    Variable = input("Dime cual es tu nombre: ")
    print(f"Con que {Variable} eh?, Es un nombre muy bonito")
    print("Quieres jugar un juego?")
    Eleccion = input("(Y/N): ")
    if Eleccion == "Y":
        print("!!Exelente!!")
        print("A que quieres jugar??")
        print("""0): Ya no quiero jugar
        1): Tetris
        2): Minecraft
        3): Among us
        4): Roblox
        5): Adivina el numero """)
        Eleccion2 = int(input("Eleccion(5 es la unica que funciona): "))
        if Eleccion2 != 5:
            print("Opcion no valida")
        if Eleccion2 == 5:
            print("!!Perfecto!!")
            print("Adivina el numero entre 1 y 100")
            NumeroPC = random.randint(1,100)
            TuEleccion = int(input("Numero:"))
            while TuEleccion != NumeroPC:
                print("Elije otro")
                if TuEleccion > NumeroPC:
                    print("Tu numero es mayor")
                else:
                    print("Tu numero es menor")
                TuEleccion = int(input("Numero: "))
            else:
                print("Ganastes")

def main():
    end = False
    while end == False:
        Interfaz()
        Variable = int(input("(0 O 1): "))
        if Variable == 0:
            end = True
        elif Variable == 1:
            inicioPrograma()

main()