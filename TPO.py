def main():
    
    print("============================")
    print("    ANALIZADOR DE TEXTOS    ")
    print("============================")
    
    while True:
        print("1. Cargar texto\n 2. Analizar texto\n 3. Buscar patrones \n 4. mostrar frecuencias de palabras\n 5. Comparar textos\n 6. Salir")
    
        opcion = int(input("Ingrese una opción: "))
    
        if opcion == 1:
            cargar_texto()
        elif opcion == 2:
            analizar_texto()
        elif opcion == 3:
            buscar_patrones()
        elif opcion == 4:
            mostrar_frecuencias()
        elif opcion == 5:
            comparar_textos()
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
main()