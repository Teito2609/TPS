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
        "contenido": "Remitente: ana@empresa.com \nAsunto: Reunión de equipo \n\nHola, \n\nNos juntamos el dia 17/10/25 a las 10:00 AM con Joaquin y Romero para discutir el proyecto. \n\nSaludos."
    },
    {
        "id": 3,
        "remitente": "soporte@empresa.com",
        "asunto": "Servidor detenido",
        "tipo": "urgente",
        "contenido": "Remitente: soporte@empresa.com \nAsunto: Servidor detenido \n\nEste problema es urgente y necesita atención inmediata. \n\nSaludos."
    },
    {
        "id": 4,
        "remitente": "maria@comercio.com",
        "asunto": "Solicitud de presupuesto",
        "tipo": "cliente",
        "contenido": "Remitente: maria@comercio.com \nAsunto: Solicitud de presupuesto \n\nNecesitamos 5 unidades de monitor. \nEl precio total es de $500000. \n\nSaludos."
    },
    {
        "id": 5,
        "remitente": "lucas@empresa.com",
        "asunto": "Reunion con el equipo",
        "tipo": "reunion",
        "contenido": "Remitente: lucas@empresa.com \nAsunto: Reunion con el equipo \n\nTenemos una reunion el dia 22/09/2026 a las 14:00 con Carla y Diego para revisar el proyecto. \n\nSaludos."
    },
    {
        "id": 6,
        "remitente": "alertas@empresa.com",
        "asunto": "Falla critica del sistema",
        "tipo": "urgente",
        "contenido": "Remitente: alertas@empresa.com \nAsunto: Falla critica del sistema \n\nEl sistema presenta una falla urgente y requiere atencion inmediata. \n\nSaludos."
    }
]


def cargar_mails_ejemplo():
    for mail in mails_ejemplo:
        guardar_y_analizar_mail(mail["contenido"])


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



def guardar_y_analizar_mail(contenido=None):
    """Ingresa el mail, analiza su contenido y almacena la información relevante."""

    if contenido is None:
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
    while True:
        print("\n--- Comparar Clientes y Productos ---")
        print("1. Comparar clientes")
        print("2. Comparar productos")
        print("3. Productos más solicitados")
        print("4. Clientes más frecuentes")
        print("0. Salir")
        
        opcion = input("Elija una opción: ")

        if opcion == "0":
            break

        elif opcion == "1":
            if len(clientes) == 0:
                print("No hay clientes guardados.")
            else:

                print("\nLista de clientes disponibles:")
                for c in clientes:
                    print(f"ID: {c['id']} - Cliente: {c['cliente']} - Precio: ${c['precio']}")

                ids_ingresados = input("\nIngrese los IDs a comparar separados por coma: ")
                lista_ids = ids_ingresados.split(",")

                print("\nResultado de la comparación:")
                for id in lista_ids:
                    id_limpio = id.strip()
                    if id_limpio.isdigit():
                        id_num = int(id_limpio)
                        encontrado = False
                        for c in clientes:
                            if c["id"] == id_num:
                                print(f"ID: {c['id']} | Cliente: {c['cliente']} | Productos: {c['producto']} | Total: ${c['precio']} | Fecha: {c['fecha']}")
                                encontrado = True
                                break
                        if not encontrado:
                            print(f"ID {id_num}: No encontrado.")

        elif opcion == "2":
            if len(clientes) == 0:
                print("No hay pedidos guardados.")
            else:

                prod_ingresados = input("Ingrese los productos a comparar separados por coma: ")
                lista_productos = prod_ingresados.split(",")

                print("\nResultado:")
                for p in lista_productos:
                    nombre = p.strip().lower()
                    pedidos = 0
                    ingresos = 0
                    for c in clientes:
                        productos_cliente = [item.lower() for item in c["producto"]]
                        if nombre in productos_cliente:
                            pedidos += 1
                            ingresos += c["precio"]
                    print(f"Producto: {nombre} | Pedidos: {pedidos} | Ingresos totales: ${ingresos}")

        elif opcion == "3":
            if len(clientes) == 0:
                print("No hay pedidos guardados.")
                continue

            productos_unicos = []
            for c in clientes:
                for p in c["producto"]:
                    nombre = p.lower()
                    if nombre != "no informado" and nombre not in productos_unicos:
                        productos_unicos.append(nombre)

            resumen = []
            for p in productos_unicos:
                cantidad = 0
                ingresos = 0
                for c in clientes:
                    productos_cliente = [item.lower() for item in c["producto"]]
                    if p in productos_cliente:
                        cantidad += 1
                        ingresos += c["precio"]
                resumen.append({"producto": p, "cantidad": cantidad, "ingresos": ingresos})

            for i in range(len(resumen) - 1):
                for k in range(i + 1, len(resumen)):
                    if resumen[k]["cantidad"] > resumen[i]["cantidad"]:
                        aux = resumen[i]
                        resumen[i] = resumen[k]
                        resumen[k] = aux

            print("\nProductos más solicitados:")
            for item in resumen:
                print(f"Producto: {item['producto']} | Cantidad: {item['cantidad']} | Ingresos: ${item['ingresos']}")

        elif opcion == "4":
            if len(clientes) == 0:
                print("No hay clientes guardados.")
                continue
            conteo_clientes = []
            for c in clientes:
                nombre = c["cliente"]
                encontrado = False
                for item in conteo_clientes:
                    if item["cliente"] == nombre:
                        item["compras"] += 1
                        encontrado = True
                        break
                if not encontrado:
                    conteo_clientes.append({"cliente": nombre, "compras": 1})

            for i in range(len(conteo_clientes) - 1):
                for k in range(i + 1, len(conteo_clientes)):
                    if conteo_clientes[k]["compras"] > conteo_clientes[i]["compras"]:
                        aux = conteo_clientes[i]
                        conteo_clientes[i] = conteo_clientes[k]
                        conteo_clientes[k] = aux

            print("\nClientes más frecuentes:")
            for item in conteo_clientes:
                print(f"Cliente: {item['cliente']} | Compras: {item['compras']}")

        else:
            print("Opción inválida. Intente de nuevo.")

        opcion = input(f"\n1. Comparar clientes\n2. Comparar productos\n3.Productos mas solicitados \n4. Clientes mas frecuentes\n0. Salir\n")
    

def ver_urgentes():
    salir = " "
    while salir != "":
        print("--- LISTA DE URGENTES ---")
        if not urgentes:
            print("No hay urgencias registradas.")

        for urgente in urgentes:
            print("\n" + "-" * 45)
            print(f"ID: {urgente['id']}")
            print(f"Remitente: {urgente['remitente']}")
            print(f"Asunto: {urgente['asunto']}")
            print(f"Pendiente: {'Sí' if urgente.get('pendiente', False) else 'No'}")
            print("-" * 45)

            if urgente.get('pendiente', False):
                respuesta = input("¿Desea marcar esta urgencia como atendida? (s/n): ")
                if respuesta.lower() == 's':
                    urgente['pendiente'] = False
                    print("Urgencia marcada como atendida.")

        salir = input("\nPresione enter para salir: ")
        while salir != "":
            salir = input("Entrada inválida. Presione enter para salir: ")


def ver_reuniones():
    
    salir = " "
    while salir != "":
        
        print("--- LISTA DE REUNIONES ---")
        if reuniones == []:
            print("No hay reuniones registradas.")

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

        salir = input("\nPresione enter para salir: ")
        while salir != "":
            salir = input("Entrada inválida. Presione enter para salir: ")

def ver_pendientes():
    
    salir = " "
    while salir != "":
        print("--- LISTA DE PENDIENTES ---")
        if not urgentes and not reuniones:
            print("No hay tareas ni reuniones pendientes.")

        hay_pendientes = False

        print("\n[ Reuniones Pendientes ]")
        for reunion in reuniones:
            if reunion.get('pendiente', False):
                hay_pendientes = True
                print(f"ID: {reunion['id']} | Asunto: {reunion['asunto']} | Fecha: {reunion['fecha']} {reunion['hora']}")
                respuesta = input("¿Desea marcar esta reunión como atendida? (s/n): ")
                if respuesta.lower() == 's':
                    reunion['pendiente'] = False
                    print("Reunión marcada como atendida.")

        print("\n[ Urgencias Pendientes ]")
        for urgente in urgentes:
            if urgente.get('pendiente', False):
                hay_pendientes = True
                print(f"ID: {urgente['id']} | Remitente: {urgente['remitente']} | Asunto: {urgente['asunto']}")
                respuesta = input("¿Desea marcar esta urgencia como atendida? (s/n): ")
                if respuesta.lower() == 's':
                    urgente['pendiente'] = False
                    print("Urgencia marcada como atendida.")

        if not hay_pendientes:
            print("No hay tareas ni reuniones pendientes.")

        salir = input("\nPresione enter para salir: ")
        while salir != "":
            salir = input("Entrada inválida. Presione enter para salir: ")

def administrar_almacenamiento():
    """Menú para administrar el almacenamiento de los mails e información extraída."""
    
    while True:
        print("\n" + "═" * 8 + " ADMINISTRAR ALMACENAMIENTO " + "═" * 8)
        print("1. Eliminar mail")
        print("2. Eliminar información de un mail")
        print("3. Eliminar mail + información")
        print("4. Eliminar mails antiguos")
        print("5. Ver espacio / cantidad de información")
        print("6. Volver")

        opcion = int(input("\n¿Qué desea hacer?: "))

        # Opciones de eliminación individual (1, 2, 3)
        if opcion == 1 or opcion == 2 or opcion == 3:
            id_ingresado = input("Ingrese ID: ")
            
            # Validamos estrictamente si lo ingresado son solo dígitos numéricos
            if not id_ingresado.isdigit():
                print("\nID no válido. Debe ingresar un número entero.")
                continue
                
            id_buscar = int(id_ingresado)

            # Verificamos si el mail existe antes de continuar
            mail_existe = False
            for mail in mails:
                if mail["id"] == id_buscar:
                    mail_existe = True
                    break

            if not mail_existe and (opcion == 1 or opcion == 3):
                print(f"\nNo se encontró ningún mail con el ID {id_buscar}.")
                continue

            # Advertencia de seguridad
            print("\n⚠ ADVERTENCIA")
            print(f"Está a punto de eliminar el mail ID {id_buscar}.")
            if opcion == 2 or opcion == 3:
                print("Esta acción puede eliminar información extraída asociada al correo.")
            
            confirmacion = input("\n¿Está seguro?\n1. Sí\n2. No\nSeleccione: ")

            if confirmacion == "1":
                # 1. Eliminar solamente el mail original
                if opcion == 1 or opcion == 3:
                    for mail in mails:
                        if mail["id"] == id_buscar:
                            mails.remove(mail)
                            break
                            
                # 2. Eliminar solamente la información
                if opcion == 2 or opcion == 3:
                    # Buscamos y eliminamos en urgentes
                    for u in urgentes:
                        if u["id"] == id_buscar:
                            urgentes.remove(u)
                            break
                    # Buscamos y eliminamos en reuniones
                    for r in reuniones:
                        if r["id"] == id_buscar:
                            reuniones.remove(r)
                            break
                    # Buscamos y eliminamos en clientes
                    for c in clientes:
                        if c["id"] == id_buscar:
                            clientes.remove(c)
                            break
                            
                print("\n¡Operación completada con éxito!")
            else:
                print("\nOperación cancelada.")

        # Opción 4: Eliminar mails antiguos
        elif opcion == 4:
            limite_ingresado = input("Eliminar correos con ID menor a: ")
            
            if not limite_ingresado.isdigit():
                print("\nID límite no válido. Debe ingresar un número entero.")
                continue
                
            limite = int(limite_ingresado)
            
            print("\n⚠ ADVERTENCIA")
            print(f"Se eliminarán de forma definitiva TODOS los correos e información con ID menor a {limite}.")
            confirmacion = input("\n¿Está seguro?\n1. Sí\n2. No\nSeleccione: ")
            
            if confirmacion == "1":
                # Utilizamos un bucle while con pop() para eliminar elementos de forma segura
                i = 0
                while i < len(mails):
                    if mails[i]["id"] < limite:
                        mails.pop(i)
                    else:
                        i = i + 1
                
                # Repetimos la limpieza para las listas de información
                for lista_info in [urgentes, reuniones, clientes]:
                    j = 0
                    while j < len(lista_info):
                        if lista_info[j]["id"] < limite:
                            lista_info.pop(j)
                        else:
                            j = j + 1
                            
                print(f"\nLimpieza completada. Correos antiguos eliminados.")
            else:
                print("\nOperación cancelada.")

        # Opción 5: Ver espacio / cantidad
        elif opcion == 5:
            print("\n" + "-" * 45)
            print("ESTADO DEL ALMACENAMIENTO")
            print("-" * 45)
            print(f"Total de correos guardados: {len(mails)}")
            print(f"Correos marcados como urgentes: {len(urgentes)}")
            print(f"Reuniones programadas: {len(reuniones)}")
            print(f"Consultas de clientes: {len(clientes)}")

        # Opción 6: Volver
        elif opcion == 6:
            break
            
        else:
            print("\nOpción inválida. Intente nuevamente.")


def resumen_general():
    """Genera un panel de control con estadísticas generales de los mails."""
    
    total_recibidos = len(mails)
    pedidos = 0
    reclamos = 0
    cotizaciones = 0
    
    for mail in mails:
        # Unimos asunto y contenido para buscar palabras clave en minúscula
        texto = (mail["asunto"] + " " + mail["contenido"]).lower()
        if "pedido" in texto or "compra" in texto:
            pedidos += 1
        if "reclamo" in texto or "problema" in texto or "queja" in texto:
            reclamos += 1
        if "cotización" in texto or "cotizacion" in texto or "presupuesto" in texto:
            cotizaciones += 1
            
    total_urgentes = len(urgentes)
    
    # Pendientes: contamos cuántos urgentes tienen su estado "pendiente" en True
    total_pendientes = 0
    for u in urgentes:
        if u["pendiente"] == True:
            total_pendientes += 1
            
    total_reuniones = len(reuniones)
    
    # 2. Cliente con mayor compra (Uso de listas paralelas e index)
    nombres_c = []
    compras_c = []
    for c in clientes:
        nombre = c["cliente"]
        precio = c["precio"]
        
        # Si el cliente ya está en la lista, le sumamos el precio
        if nombre in nombres_c:
            idx = nombres_c.index(nombre)
            compras_c[idx] += precio
        else:
            # Si no está, lo agregamos como nuevo
            nombres_c.append(nombre)
            compras_c.append(precio)
            
    mejor_cliente = "No hay datos"
    if len(nombres_c) > 0:
        max_compra = max(compras_c)
        idx_max = compras_c.index(max_compra)
        mejor_cliente = nombres_c[idx_max]
        
    # 3. Producto más solicitado
    nombres_p = []
    cant_p = []
    for c in clientes:
        prod = c["producto"]
        if prod != "No informado":
            if prod in nombres_p:
                idx = nombres_p.index(prod)
                cant_p[idx] += 1
            else:
                nombres_p.append(prod)
                cant_p.append(1)
                
    producto_top = "No hay datos"
    if len(nombres_p) > 0:
        max_cant = max(cant_p)
        idx_max = cant_p.index(max_cant)
        producto_top = nombres_p[idx_max]
        
    # 4. Cliente con más reclamos
    nombres_r = []
    cant_r = []
    for mail in mails:
        texto = (mail["asunto"] + " " + mail["contenido"]).lower()
        if "reclamo" in texto or "problema" in texto or "queja" in texto:
            # Extraemos el nombre antes del @
            remitente = mail["remitente"].split("@")[0]
            if remitente in nombres_r:
                idx = nombres_r.index(remitente)
                cant_r[idx] += 1
            else:
                nombres_r.append(remitente)
                cant_r.append(1)
                
    cliente_reclamos = "No hay datos"
    if len(nombres_r) > 0:
        max_r = max(cant_r)
        idx_max = cant_r.index(max_r)
        cliente_reclamos = nombres_r[idx_max]
        
    # 5. Próxima reunión
    prox_reunion = "No hay reuniones programadas"
    if len(reuniones) > 0:
        r = reuniones[0] # Tomamos la primera de la lista
        fecha_str = r["fecha"] if r["fecha"] else "fecha a confirmar"
        hora_str = r["hora"] if r["hora"] else "hora a confirmar"
        prox_reunion = f"{fecha_str} a las {hora_str}"

    # 6. Imprimir el panel usando f-strings para alinear a la derecha
    print("\n" + "═" * 8 + " RESUMEN GENERAL " + "═" * 8)
    print(f"\nMAILS RECIBIDOS: {total_recibidos:>14}")
    
    print("\n" + f"PEDIDOS: {pedidos:>22}")
    print(f"RECLAMOS: {reclamos:>21}")
    print(f"COTIZACIONES: {cotizaciones:>17}")
    
    print("\n" + f"🚨 URGENTES: {total_urgentes:>17}")
    print(f"📋 PENDIENTES: {total_pendientes:>15}")
    print(f"📅 PRÓXIMAS REUNIONES: {total_reuniones:>7}")
    
    print("\n" + "-" * 32)
    print("CLIENTE CON MAYOR COMPRA:")
    print(mejor_cliente.title()) 
    
    print("\nPRODUCTO MÁS SOLICITADO:")
    print(producto_top.capitalize())
    
    print("\nCLIENTE CON MÁS RECLAMOS:")
    print(cliente_reclamos.title())
    print("-" * 32)
    
    print(f"⚠ Hay {total_urgentes} asuntos urgentes")
    print(f"⚠ Hay {total_pendientes} tareas pendientes")
    print(f"📅 Próxima reunión: {prox_reunion}")


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