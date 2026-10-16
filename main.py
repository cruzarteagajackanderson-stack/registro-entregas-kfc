from almacenamiento import cargar_entregas, guardar_entregas

from funciones import (
    registrar_entrega,
    mostrar_entregas,
    buscar_entregas,
    mostrar_resumen,
)


def main():
    try:
        entregas = cargar_entregas()

    except (OSError, ValueError) as error:
        print(
            f"No se pudieron cargar los registros: {error}"
        )
        print(
            "El programa se cerrará para proteger los datos."
        )
        print(
            "Revisa entregas.json antes de continuar."
        )
        return

    while True:
        print("\n=== RECEPCIÓN DE MERCADERÍA ===")
        print("Prototipo académico")
        print("1. Registrar entrega")
        print("2. Mostrar entregas")
        print("3. Buscar entrega")
        print("4. Mostrar resumen")
        print("5. Salir")

        opcion = input(
            "Selecciona una opción: "
        ).strip()

        if opcion == "1":
            nueva_entrega = registrar_entrega(entregas)

            if nueva_entrega is not None:
                actualizadas = entregas + [nueva_entrega]

                if guardar_entregas(actualizadas):
                    entregas = actualizadas
                    print(
                        "Entrega guardada en el archivo."
                    )

                else:
                    print(
                        "La entrega no se agregó. "
                        "Intenta nuevamente."
                    )

        elif opcion == "2":
            mostrar_entregas(entregas)

        elif opcion == "3":
            buscar_entregas(entregas)

        elif opcion == "4":
            mostrar_resumen(entregas)

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print(
                "Opción no válida. "
                "Elige un número del 1 al 5."
            )


if __name__ == "__main__":
    main()