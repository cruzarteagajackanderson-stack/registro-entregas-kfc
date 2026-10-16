import json
from pathlib import Path


ARCHIVO = Path(__file__).resolve().parent / "entregas.json"

CAMPOS_TEXTO = {
    "guia",
    "fecha",
    "hora",
    "proveedor",
    "producto",
    "presentacion",
    "observaciones",
    "responsable",
    "ubicacion",
}

CAMPOS_CANTIDAD = {
    "solicitada",
    "recibida",
    "faltantes",
    "excedentes",
}


def validar_entregas(entregas):
    if not isinstance(entregas, list):
        raise ValueError("El archivo debe contener una lista.")

    campos_obligatorios = CAMPOS_TEXTO | CAMPOS_CANTIDAD

    for entrega in entregas:
        if not isinstance(entrega, dict):
            raise ValueError("Existe un registro no válido.")

        if not campos_obligatorios.issubset(entrega):
            raise ValueError("Existe un registro incompleto.")

        for campo in CAMPOS_TEXTO:
            if not isinstance(entrega[campo], str):
                raise ValueError(
                    f"El campo '{campo}' debe contener texto."
                )

            if not entrega[campo].strip():
                raise ValueError(
                    f"El campo '{campo}' no puede estar vacío."
                )

        for campo in CAMPOS_CANTIDAD:
            cantidad = entrega[campo]

            if type(cantidad) is not int or cantidad < 0:
                raise ValueError(
                    f"La cantidad '{campo}' no es válida."
                )

        if entrega["solicitada"] < 1:
            raise ValueError(
                "La cantidad solicitada debe ser mayor que cero."
            )

        diferencia = entrega["solicitada"] - entrega["recibida"]

        faltantes_esperados = max(diferencia, 0)
        excedentes_esperados = max(-diferencia, 0)

        if entrega["faltantes"] != faltantes_esperados:
            raise ValueError(
                "Los faltantes de un registro no coinciden."
            )

        if entrega["excedentes"] != excedentes_esperados:
            raise ValueError(
                "Los excedentes de un registro no coinciden."
            )


def cargar_entregas():
    if not ARCHIVO.exists():
        return []

    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        entregas = json.load(archivo)

    validar_entregas(entregas)

    return entregas


def guardar_entregas(entregas):
    temporal = ARCHIVO.with_suffix(".tmp")

    try:
        validar_entregas(entregas)

        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(
                entregas,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        temporal.replace(ARCHIVO)

    except (OSError, TypeError, ValueError) as error:
        print(f"No se pudieron guardar los registros: {error}")
        return False

    return True 