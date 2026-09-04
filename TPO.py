diccionario = {
    "saludos": ["hola", "buenos días", "buenas tardes", "buenas noches"],
    "despedidas": ["adiós", "hasta luego", "nos vemos", "chau"],
    "preguntas":[],
    "nombres": [],
    "telefonos": [],
    "correos": [],
    "fechas": []
    
}

def mostrar_frecuencia_letras(texto):
    """Muestra la frecuencia de letras en el texto."""
    frecuencia = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1

    cantidad_total = sum(frecuencia.values())
    return frecuencia, cantidad_total

def mostrar_frecuencia_palabras(texto):
    """Muestra la frecuencia de palabras en el texto."""
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    cantidad_total = sum(frecuencia.values())
    return frecuencia, cantidad_total

def cargar_texto():
    """Ingresa un archivo y lo guarda en texto."""
    
    archivo = input("Ingrese el nombre del archivo a cargar: ")
    with open(archivo, "r") as f:
        texto = f.read()
    
    return texto

def analizar_texto(texto):
    """Analiza el texto proporcionado."""
    
    palabras = texto.split()
    pregunta_actual = []
    
    for palabra in palabras:
        
        if "@" in palabra:
            diccionario["correos"].append(palabra)
        if palabra.isdigit() and len(palabra) == 10:
            diccionario["telefonos"].append(palabra)
        if "/" in palabra or "-" in palabra:
            diccionario["fechas"].append(palabra)
        if "¿" in palabra:
            pregunta_actual = [palabra]
        elif pregunta_actual:
            pregunta_actual.append(palabra)

        if pregunta_actual and "?" in palabra:
            diccionario["preguntas"].append(" ".join(pregunta_actual))
            pregunta_actual = []
        if palabra.istitle():
            diccionario["nombres"].append(palabra)
        

def main():
    
    print("============================")
    print("    ANALIZADOR DE TEXTOS    ")
    print("============================")
    
    while True:
        print("1. Cargar texto\n 2. Analizar texto\n 3. Buscar patrones \n 4. mostrar frecuencias de palabras\n 5. Comparar textos\n 6. Salir")
    
        opcion = int(input("Ingrese una opción: "))
    
        if opcion == 1:
            texto = cargar_texto()
        elif opcion == 2:
            analizar_texto(texto)
        elif opcion == 3:
            buscar_patrones()
        elif opcion == 4:
            print("1. Frecuencia de Letras\n 2. Frecuencia de Palabras")
            sub_opcion = int(input("Ingrese una opción: "))
            if sub_opcion == 1:
                frecuencia_letras , total_letras = mostrar_frecuencia_letras(texto)
                print("Frecuencia de letras:")
                for letra, frecuencia in frecuencia_letras.items():
                    print(f"{letra}: {frecuencia}")
                    print(total_letras)
            elif sub_opcion == 2:
                frecuencia_palabras , total_palabras = mostrar_frecuencia_palabras(texto)
                print("Frecuencia de palabras:")
                for palabra, frecuencia in frecuencia_palabras.items():
                    print(f"{palabra}: {frecuencia}")
                print(total_palabras)
        elif opcion == 5:
            comparar_textos()
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
main()