mails = []
clientes = []
urgentes = []
reuniones = []



def guardar_y_analizar_mail():
    """Ingresa el mail, analiza su contenido y almacena la información relevante."""

    contenido = input("Ingrese el mail: ")

    id_mail = len(mails) + 1

    palabras = contenido.lower().split()

    es_urgente = False
    es_reunion = False
    es_cliente = False

    for palabra in palabras:

        if palabra == "remitente:":
            indice_remitente = palabras.index(palabra) + 1
            remitente = palabras[indice_remitente]
                
        if palabra == "asunto:":
            indice_asunto = palabras.index(palabra) + 1
            asunto = palabras[indice_asunto]

        if palabra == "urgente":
            es_urgente = True
            tipo = "urgente"

        elif palabra == "reunión":
            es_reunion = True
            tipo = "reunión"
            
            if "/" in palabra:
                fecha = palabra
            else:
                fecha = ""
            
            if "hora:" in palabras:
                indice_hora = palabras.index("hora:") + 1
                hora = palabras[indice_hora]
            
        elif palabra == "cliente":
            es_cliente = True
            tipo = "cliente"  
        
            if "/" in palabra:
                fecha = palabra
            else:
                fecha = ""
            
            if "producto:" in palabras:
                indice_producto = palabras.index("producto:") + 1
                producto = palabras[indice_producto]
            
            if "precio:" in palabras:
                indice_precio = palabras.index("precio:") + 1
                precio = float(palabras[indice_precio])
            
            if "hora:" in palabras:
                indice_hora = palabras.index("hora:") + 1
                hora = palabras[indice_hora]
            
            cliente = remitente.split("@")[0]  # Extrae el nombre del cliente del remitente

    mail = {
        "id": id_mail,
        "remitente": remitente,
        "asunto": asunto,
        "tipo": tipo,
        "contenido": contenido
    }
    
    mails.append(mail)

    if es_urgente:
        urgente = {
            "id": id_mail,
            "remitente": mail["remitente"],
            "asunto": mail["asunto"],
            "tipo": mail["tipo"],
            "pendiente": True
        }

        urgentes.append(urgente)

    if es_reunion:
        reunion = {
            "id": id_mail,
            "remitente": mail["remitente"],
            "asunto": mail["asunto"],
            "hora": hora,
            "fecha": fecha,
            "empleados": []
        }

        reuniones.append(reunion)

    if es_cliente:
        cliente = {
            "id": id_mail,
            "remitente": mail["remitente"],
            "asunto": mail["asunto"],
            "tipo": mail["tipo"],
            "cliente": cliente,
            "producto": producto,
            "fecha": fecha,
            "precio": precio
        }

        clientes.append(cliente)

    print("\nMail guardado correctamente.")

def almacen_mails():
    print("Función almacén de mails")


def comparar_clientes_productos():
    print("Función comparar clientes y productos")


def ver_urgentes():
    print("Función urgentes")


def ver_reuniones():
    print("Función reuniones")


def ver_pendientes():
    print("Función pendientes")


def administrar_almacenamiento():
    print("Función administrar almacenamiento")


def resumen_general():
    print("Función resumen general")


def main():
    while True:
        print("\n" + "=" * 45)
        print("       SISTEMA DE GESTIÓN DE MAILS")
        print("=" * 45)
        print("1. Guardar y analizar nuevo mail")
        print("2. Almacén de mails")
        print("3. Comparar clientes y productos")
        print("4. Urgente")
        print("5. Reuniones")
        print("6. Pendientes")
        print("7. Administrar almacenamiento")
        print("8. Resumen general")
        print("0. Salir")
        print("=" * 45)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            guardar_y_analizar_mail()
        elif opcion == "2":
            almacen_mails()
        elif opcion == "3":
            comparar_clientes_productos()
        elif opcion == "4":
            ver_urgentes()
        elif opcion == "5":
            ver_reuniones()
        elif opcion == "6":
            ver_pendientes()
        elif opcion == "7":
            administrar_almacenamiento()
        elif opcion == "8":
            resumen_general()
        elif opcion == "0":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


main()