from datetime import datetime


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Este dato no puede quedar vacío.")


def pedir_entero(mensaje, minimo=0):
    while True:
        try:
            numero = int(input(mensaje))

            if numero >= minimo:
                return numero

            print(
                f"Ingresa un número mayor o igual a {minimo}."
            )

        except ValueError:
            print("Ingresa un número entero válido.")


def pedir_fecha():
    while True:
        texto = input("Fecha (DD/MM/AAAA): ").strip()

        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y")
            return fecha.strftime("%d/%m/%Y")

        except ValueError:
            print("Fecha no válida. Ejemplo: 09/10/2026.")


def pedir_hora():
    while True:
        texto = input(
            "Hora (HH:MM, formato de 24 horas): "
        ).strip()

        try:
            hora = datetime.strptime(texto, "%H:%M")
            return hora.strftime("%H:%M")

        except ValueError:
            print("Hora no válida. Ejemplo: 09:30.")


def registrar_entrega(entregas):
    print("\n--- REGISTRAR ENTREGA ---")

    guia = pedir_texto("Número de guía: ").upper()
    fecha = pedir_fecha()
    hora = pedir_hora()
    proveedor = pedir_texto("Proveedor: ")
    producto = pedir_texto("Producto: ")

    presentacion = pedir_texto(
        "Presentación o unidad de conteo "
        "(ejemplo: caja de 20 kg): "
    )

    for entrega in entregas:
        misma_guia = (
            entrega["guia"].casefold() == guia.casefold()
        )

        mismo_proveedor = (
            entrega["proveedor"].casefold()
            == proveedor.casefold()
        )

        mismo_producto = (
            entrega["producto"].casefold()
            == producto.casefold()
        )

        misma_presentacion = (
            entrega["presentacion"].casefold()
            == presentacion.casefold()
        )

        if (
            misma_guia
            and mismo_proveedor
            and mismo_producto
            and misma_presentacion
        ):
            print(
                "Ya existe este producto y presentación "
                "para esa guía y proveedor."
            )
            print("No se agregó un registro duplicado.")
            return None

    print("\nUsa la misma unidad para ambas cantidades.")
    print("Por ejemplo, si cuentas cajas, ingresa cajas en ambas.")

    solicitada = pedir_entero(
        "Cantidad solicitada: ",
        minimo=1
    )

    recibida = pedir_entero(
        "Cantidad recibida: ",
        minimo=0
    )

    faltantes = max(solicitada - recibida, 0)
    excedentes = max(recibida - solicitada, 0)

    print(f"\nFaltantes: {faltantes}")
    print(f"Excedentes: {excedentes}")

    observaciones = input("Observaciones: ").strip()

    if not observaciones:
        observaciones = "Sin observaciones"

    responsable = pedir_texto(
        "Responsable o iniciales: "
    ).upper()

    ubicacion = pedir_texto(
        "Ubicación de almacenamiento: "
    )

    entrega = {
        "guia": guia,
        "fecha": fecha,
        "hora": hora,
        "proveedor": proveedor,
        "producto": producto,
        "presentacion": presentacion,
        "solicitada": solicitada,
        "recibida": recibida,
        "faltantes": faltantes,
        "excedentes": excedentes,
        "observaciones": observaciones,
        "responsable": responsable,
        "ubicacion": ubicacion,
    }

    return entrega


def mostrar_entregas(entregas):
    if not entregas:
        print("\nNo hay entregas para mostrar.")
        return

    for numero, entrega in enumerate(entregas, start=1):
        print(f"\n--- REGISTRO {numero} ---")
        print(f"Guía: {entrega['guia']}")
        print(f"Fecha: {entrega['fecha']}")
        print(f"Hora: {entrega['hora']}")
        print(f"Proveedor: {entrega['proveedor']}")
        print(f"Producto: {entrega['producto']}")
        print(f"Presentación: {entrega['presentacion']}")
        print(f"Cantidad solicitada: {entrega['solicitada']}")
        print(f"Cantidad recibida: {entrega['recibida']}")
        print(f"Faltantes: {entrega['faltantes']}")
        print(f"Excedentes: {entrega['excedentes']}")
        print(f"Observaciones: {entrega['observaciones']}")
        print(f"Responsable: {entrega['responsable']}")
        print(f"Ubicación: {entrega['ubicacion']}")


def buscar_entregas(entregas):
    print("\n--- BUSCAR ENTREGA ---")

    criterio = pedir_texto(
        "Escribe una guía, proveedor o producto: "
    ).casefold()

    resultados = []

    for entrega in entregas:
        coincide = any(
            criterio in entrega[campo].casefold()
            for campo in ("guia", "proveedor", "producto")
        )

        if coincide:
            resultados.append(entrega)

    print(
        f"\nCoincidencias encontradas: {len(resultados)}"
    )

    mostrar_entregas(resultados)


def mostrar_resumen(entregas):
    print("\n--- RESUMEN DE RECEPCIONES ---")

    if not entregas:
        print("No hay registros para resumir.")
        return

    con_faltantes = 0
    con_excedentes = 0
    sin_diferencias = 0

    for entrega in entregas:
        if entrega["faltantes"] > 0:
            con_faltantes += 1

        elif entrega["excedentes"] > 0:
            con_excedentes += 1

        else:
            sin_diferencias += 1

    print(f"Registros de productos: {len(entregas)}")
    print(f"Registros con faltantes: {con_faltantes}")
    print(f"Registros con excedentes: {con_excedentes}")
    print(f"Registros sin diferencias: {sin_diferencias}")

    if con_faltantes == 0 and con_excedentes == 0:
        print("\nNo hay diferencias registradas.")
        return

    print("\nDetalle de diferencias:")

    for entrega in entregas:
        if (
            entrega["faltantes"] > 0
            or entrega["excedentes"] > 0
        ):
            print(
                f"- Guía: {entrega['guia']} | "
                f"Producto: {entrega['producto']} | "
                f"Presentación: {entrega['presentacion']} | "
                f"Faltantes: {entrega['faltantes']} | "
                f"Excedentes: {entrega['excedentes']}"
            )