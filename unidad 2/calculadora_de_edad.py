# importar datetime para manejo de fechas
from datetime import datetime

# Fecha actual
FECHA_ACTUAL = datetime.now().date()


def calcular_edad_ingresada(fecha_nac):
    edad = FECHA_ACTUAL.year - fecha_nac.year

    # Se valida si ya cumplió años en la fecha de captura o aún no
    if (FECHA_ACTUAL.month, FECHA_ACTUAL.day) < (fecha_nac.month, fecha_nac.day):
        edad -= 1
        print(f"La fecha de nacimiento es: {fecha_nac}. Aún no ha cumplido años.")
    else:
        print(f"La fecha de nacimiento es: {fecha_nac}. Ya ha cumplido años.")

    print(f"La edad del cliente es: {edad} años.")
    return False  # Entrada válida, salir del bucle


# Función para validar la entrada de la fecha de nacimiento
def validar_entrada(fecha_str):
    if not fecha_str:
        print("No se puede dejar en blanco.")
        return True

    try:
        # Se valida que el formato sea DD-MM-AAAA y la fecha existe
        # La función strptime automáticamente valida días y meses válidos
        fecha_nac = datetime.strptime(fecha_str, "%d-%m-%Y").date()
        # Se valida que el año de nacimiento es mayor de 1900
        if fecha_nac.year <= 1900:
            print("El año de nacimiento debe ser posterior a 1900.")
            return True

        # Se valida que la fecha de nacimiento no puede ser despues de la fecha de hoy
        if fecha_nac > FECHA_ACTUAL:
            print("La fecha de nacimiento no puede ser posterior a la fecha actual.")
            return True

        # Cálculo de la edad
        return calcular_edad_ingresada(fecha_nac)
        # Resta del año actual menos el año de nacimiento

    except ValueError as e:
        # Captura errores de formato o fechas inválidas.
        if "El dia está fuera de rango para el mes" in str(e):
            print("El día ingresado no es válido para ese mes. Revise los días (1-31).")
            return True
        else:
            print("Formato de fecha inválido. Asegúrese de usar DD-MM-AAAA.")
            return True


# Función principal para calcular la edad
def calcular_edad():
    print(f"\n--- Calculadora de Edad ---")
    continuar = True
    while continuar:
        # Se pide la fecha de nacimiento
        fecha_nac_str = input("Ingrese la fecha de nacimiento (DD-MM-AAAA): ").strip()
        continuar = validar_entrada(fecha_nac_str)
    print("--- Fin de la Calculadora de Edad ---\n")


# Ejecución del ejercicio
calcular_edad()
