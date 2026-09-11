mails = []
clientes = []
urgentes = []
reuniones = []

diccionario_urgente = {
    "urgente": True,
    "urgencia": True,
    "inmediato": True,
    "inmediata": True,
    "prioridad": True
}

diccionario_reunion = {
    "reunión": True,
    "reunion": True,
    "junta": True,
    "encuentro": True,
    "videollamada": True
}
diccionario_cliente = {
    "cliente": True,
    "compra": True,
    "pedido": True,
    "presupuesto": True,
    "cotización": True,
    "cotizacion": True
}
diccionario_hora = {
    "hora": True,
    "horario": True,
    "las": True
}
diccionario_empleados = {
    "empleados": True,
    "con": True,
    "participantes": True,
    "colaboradores": True
}
diccionario_producto = {
    "producto": True,
    "productos": True,
    "artículo": True,
    "articulos": True,
    "mercancía": True
}

mails_ejemplo = [
    {
        "id": 1,
        "remitente": "juan@gmail.com",
        "asunto": "Pedido urgente de productos",
        "tipo": "cliente",
        "contenido": "Remitente: juan@gmail.com \nAsunto: Pedido urgente de productos \n\nHola, \n\nSoy Juan Pérez de la empresa ABC. \n\nNecesitamos 20 unidades de teclado y 10 unidades de mouse. \nEl precio total es de $150000. \n\nNecesitamos recibir el pedido el 15/09/2026. \n\nSaludos."
    },
    {
        "id": 2,
        "remitente": "ana@empresa.com",
        "asunto": "Reunión de equipo",
        "tipo": "reunión",
        "contenido": "Remitente: ana@empresa.com \nAsunto: Reunión de equipo \n\nHola, \n\nNos juntamos mañana a las 10:00 AM con Joaquin y Romero para discutir el proyecto. \n\nSaludos."
    },
    {
        "id": 3,
        "remitente": "soporte@empresa.com",
        "asunto": "Servidor detenido",
        "tipo": "urgente",
        "contenido": "Remitente: soporte@empresa.com \nAsunto: Servidor detenido \n\nEste problema es urgente y necesita atención inmediata. \n\nSaludos."
    }
]


def cargar_mails_ejemplo():
    for mail in mails_ejemplo:
        mails.append(mail.copy())


def ingresar_mail_completo():
    """Permite ingresar un mail de varias líneas y finalizarlo con FIN."""
    print("Ingrese el mail línea por línea. Escriba FIN en una línea nueva para terminar.")
    lineas = []

    while True:
        linea = input()
        if linea == "FIN":
            break
        lineas.append(linea)

    return "\n".join(lineas)



def guardar_y_analizar_mail():
    """Ingresa el mail, analiza su contenido y almacena la información relevante."""

    contenido = ingresar_mail_completo()
    if contenido.strip() == "0":
        return
    if not contenido.strip():
        print("El mail no puede estar vacío. Intente nuevamente.")
        return

    id_mail = len(mails) + 1

    palabras = contenido.lower().split()

    remitente = "No informado"
    asunto = "No informado"
    tipo = "general"
    cliente = "No informado"
    producto = []
    precio = 0
    fecha = "No informada"
    hora = "No informada"
    empleados = []
    es_urgente = False
    es_reunion = False
    es_cliente = False

    for palabra in palabras:

        if palabra == "remitente:":
            indice_remitente = palabras.index(palabra) + 1
            remitente = palabras[indice_remitente]
            cliente = remitente.split("@")[0]  # Extrae el nombre del cliente del remitente
                
        if palabra == "asunto:":
            indice_asunto = palabras.index(palabra) + 1
            asunto = palabras[indice_asunto]

        if palabra in diccionario_urgente and not palabra in diccionario_reunion and not palabra in diccionario_cliente:
            es_urgente = True
            tipo = "urgente"

        if palabra in diccionario_reunion:
            es_reunion = True
            tipo = "reunión"
            
            if "/" in palabra:
                fecha = palabra
            else:
                fecha = ""
            
            if palabra in diccionario_hora:
                indice_hora = palabras.index(palabra) + 1
                hora = palabras[indice_hora]
            
        if palabra in diccionario_cliente:
            es_cliente = True
            tipo = "cliente"  
        
            if "/" in palabra:
                fecha = palabra
            else:
                fecha = ""
            
            if "$" in palabra:
                precio_texto = palabra.replace("$", "").rstrip(".")
                precio = float(precio_texto)

    productos_encontrados = []
    for indice, palabra in enumerate(palabras):
        if (
            palabra.isdigit()
            and indice + 3 < len(palabras)
            and palabras[indice + 1].rstrip(".,") in ("unidad", "unidades")
            and palabras[indice + 2] == "de"
        ):
            producto = palabras[indice + 3].rstrip(".,")
            productos_encontrados.append(producto)

    if productos_encontrados:
        producto = productos_encontrados
    else:
        producto = ["No informado"]

    empleados_encontrados = []
    palabras_que_finalizan_empleados = {
        "para", "sobre", "acerca", "discutir", "tratar", "hablar"
    }

    for indice, palabra in enumerate(palabras):
        if palabra in diccionario_empleados:
            indice_empleado = indice + 1
            while indice_empleado < len(palabras):
                empleado = palabras[indice_empleado].rstrip(".,")
                if empleado in palabras_que_finalizan_empleados:
                    break
                if empleado != "y":
                    empleados_encontrados.append(empleado)
                indice_empleado += 1

    if empleados_encontrados:
        empleados = empleados_encontrados

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
            "urgente": es_urgente,
            "empleados": empleados
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
    """Podes ingresar a todos los mails y ver su contenido"""
    
    for mail in mails:
        print("\n" + "-" * 45)
        print(f"\nID: {mail['id']}")
        print(f"Remitente: {mail['remitente']}")
        print(f"Asunto: {mail['asunto']}")
        print(f"Tipo: {mail['tipo']}")

    opcion = int(input("\nIngrese el ID del mail que desea ver (o '0' para salir): "))
    while opcion != 0:
        mail_seleccionado = None
        for mail in mails:
            if mail['id'] == opcion:
                mail_seleccionado = mail
                break

        if mail_seleccionado:
            print(f"\nContenido del mail ID {mail_seleccionado['id']}:")
            print(mail_seleccionado['contenido'])
        else:
            print("\nID no válido.")

        opcion = int(input("\nIngrese el ID del mail que desea ver (o '0' para salir): "))

def comparar_clientes_productos():
    print("Función comparar clientes y productos")


def ver_urgentes():
    print("Función urgentes")


def ver_reuniones():
    print("--- LISTA DE REUNIONES ---")
    if not reuniones:
        print("No hay reuniones registradas.")
        return

    for reunion in reuniones:
        print("\n" + "-" * 45)
        print(f"ID: {reunion['id']}")
        print(f"Remitente: {reunion['remitente']}")
        print(f"Asunto: {reunion['asunto']}")
        print(f"Hora: {reunion['hora']}")
        print(f"Fecha: {reunion['fecha']}")
        print(f"Urgente: {'Sí' if reunion['urgente'] else 'No'}")
        print(f"Empleados: {', '.join(reunion['empleados']) if reunion['empleados'] else 'No informado'}")
        print(f"Pendiente: {'Sí' if reunion.get('pendiente', False) else 'No'}")
        print("-" * 45)
        
        if reunion.get('pendiente', False):
            respuesta = input("¿Desea marcar esta reunión como atendida? (s/n): ")
            if respuesta.lower() == 's':
                reunion['pendiente'] = False
                print("Reunión marcada como atendida.")

def ver_pendientes():
    print("--- ELEMENTOS PENDIENTES ---")
    
    hay_pendientes = False

    print("\n[ Reuniones Pendientes ]")
    for reunion in reuniones:
        if reunion.get('pendiente', False):
            hay_pendientes = True
            print(f"ID: {reunion['id']} | Asunto: {reunion['asunto']} | Fecha: {reunion['fecha']} {reunion['hora']}")

    print("\n[ Urgencias Pendientes ]")
    for urgente in urgentes:
        if urgente.get('pendiente', False):
            hay_pendientes = True
            print(f"ID: {urgente['id']} | Remitente: {urgente['remitente']} | Asunto: {urgente['asunto']}")

    if not hay_pendientes:
        print("No hay tareas ni reuniones pendientes.")


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

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            guardar_y_analizar_mail()
        elif opcion == 2:
            almacen_mails()
        elif opcion == 3:
            comparar_clientes_productos()
        elif opcion == 4:
            ver_urgentes()
        elif opcion == 5:
            ver_reuniones()
        elif opcion == 6:
            ver_pendientes()
        elif opcion == 7:
            administrar_almacenamiento()
        elif opcion == 8:
            resumen_general()
        elif opcion == 0:
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


cargar_mails_ejemplo()
main()