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
        Eleccion2 = input("Eleccion(5 es la unica que funciona): ")
        
