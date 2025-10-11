# Definición de la función que inicializa el inventario del cajero.
def inventario_inicial():
    return {1000: 10, 500: 10, 200: 10, 100: 10, 50: 10}


# Definición de la función principal que ejecuta el algoritmo del cajero.
def cajero_automatico():
    # Inicializa el inventario llamando a la función auxiliar.
    inventario = inventario_inicial()

    # Define las denominaciones disponibles. Es crucial que estén ordenadas.
    denominaciones = [1000, 500, 200, 100, 50]

    print("\n" + "=" * 30)
    print("CAJERO AUTOMÁTICO")
    print("=" * 30)

    # Muestra el estado inicial del inventario al usuario.
    print("Inventario inicial:")
    for n in denominaciones:
        print(f"Billetes de a {n}: {inventario[n]} billetes")

    print("\n" + "-" * 30)

    # --- Solicitud y Validación de la Cantidad a Retirar ---
    entrada_valida = False
    cantidad_solicitada = 0

    # Bucle para solicitar la cantidad hasta que la entrada sea válida.
    while not entrada_valida:
        entrada_usuario = input("Ingrese la cantidad a dispensar (0 para salir): ")

        # Uso de try-except para manejar errores si el usuario no ingresa un número.
        try:
            cantidad_solicitada = int(entrada_usuario)

            # 1. Validación de salida
            if cantidad_solicitada == 0:
                print("Saliendo del cajero. ¡Hasta luego!")
                return  # Termina la ejecución de la función.

            # 2. Validación de números negativos
            elif cantidad_solicitada < 0:
                print("La cantidad no puede ser negativa.")

            # 3. Validación de múltiplo de la denominación mínima (50)
            elif cantidad_solicitada % 50 != 0:
                print("La cantidad solicitada debe ser múltiplo de 50")

            # Si todas las validaciones pasan, la entrada es válida.
            else:
                entrada_valida = True

        # Captura el error si el usuario ingresa texto en lugar de un número.
        except ValueError:
            print("Debe ingresar una cantidad en números.")

    # Diccionario para registrar cuántos billetes se entregarán de cada denominación.
    billetes_a_entregar = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0}

    # El monto restante se usa como contador para rastrear lo que falta por dispensar.
    monto_restante = cantidad_solicitada
    cantidad_original = cantidad_solicitada

    # Itera sobre las denominaciones de mayor a menor.
    for denominacion in denominaciones:
        # Cantidad de billetes disponibles para la denominación actual.
        cantidad_disponible = inventario[denominacion]

        # Calcula la cantidad IDEAL de billetes que necesitamos usando división entera.
        cantidad_total_ideal = monto_restante // denominacion

        # Lógica para elegir la menor cantidad (entre lo ideal y lo disponible).
        if cantidad_total_ideal >= cantidad_disponible:
            # Opción 1: Si se necesitan más de los que hay, usamos todos los disponibles.
            billetes_a_entregar[denominacion] = cantidad_disponible
            # Actualiza el monto restante con el valor total de los billetes disponibles.
            monto_restante -= cantidad_disponible * denominacion
        else:
            # Opción 2: Si hay suficientes, solo usamos la cantidad ideal necesaria.
            billetes_a_entregar[denominacion] = cantidad_total_ideal
            # Actualiza el monto restante con el valor de los billetes entregados.
            monto_restante -= cantidad_total_ideal * denominacion

    # Si el monto_restante es 0, la dispensación fue exitosa y exacta.
    if monto_restante == 0:
        print(f"\n¡Dispensación Exitosa!")
        print(f"Dispensando la cantidad {cantidad_original} pesos.")

        # Muestra los billetes entregados y actualiza el inventario real.
        for denominacion in denominaciones:
            b_entregados = billetes_a_entregar[denominacion]
            if b_entregados > 0:
                print(f"Billetes de a {denominacion}: {b_entregados} billetes")
                # Actualiza el inventario restando la cantidad entregada.
                inventario[denominacion] -= b_entregados

        # Muestra el estado final del inventario.
        print("\nInventario actualizado:")
        for n in denominaciones:
            print(f"Billetes de a {n}: {inventario[n]} billetes")

    # Si monto_restante > 0, no se pudo completar el monto con la combinación actual.
    else:
        # Se cumple la condición: "no dispensará ningún billete".
        print(
            f"Lo sentimos, no se puede dispensar la cantidad solicitada {cantidad_original} pesos en este momento."
        )
        print(
            "La combinación de billetes actual no permite entregar esa cantidad de forma exacta."
        )
        print(f"Faltó cubrir: ${monto_restante}")


# Llamada a la función principal para iniciar el programa.
cajero_automatico()
