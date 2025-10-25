import pandas as pd # Importa la librería pandas para manejo de datos estructurados (DataFrames).

# Se cargan los archivos
def cargar_datos(ruta, tipo): # Define una función para cargar datos desde un archivo (ruta) y un tipo ('excel' o 'csv').
    if tipo == 'excel':
        return pd.read_excel(ruta) # Carga el archivo como un DataFrame si el tipo es 'excel'.
    elif tipo == 'csv':
        return pd.read_csv(ruta) # Carga el archivo como un DataFrame si el tipo es 'csv'.
    else:
        # Lanza un error si el tipo de archivo no está soportado.
        raise ValueError("Tipo de archivo no soportado. Use 'excel' o 'csv'.")

# Obtener las preguntas usando métodos de pandas
def obtenerDatos(datos): # Define una función para extraer la lista de preguntas.
    preguntas = datos['Pregunta'].values # Selecciona la columna 'Pregunta' y extrae sus valores como un array de NumPy.
    return preguntas # Devuelve el array con las etiquetas de las preguntas.

# Crear diccionario de respuestas correctas y calificar
def calificar_examen(preguntas, df_estudiantes, df_correctas): # Función principal de calificación.
    
    clave_respuestas = {} # Inicializa un diccionario vacío para almacenar la clave de respuestas.
    for i in range(df_correctas.shape[0]): # Itera sobre cada fila del DataFrame de respuestas correctas.
        # Extraemos pregunta y respuesta de la fila actual.
        pregunta = df_correctas['Pregunta'].iloc[i] # Accede a la columna 'Pregunta' en la fila 'i'.
        respuesta = df_correctas['Respuesta'].iloc[i] # Accede a la columna 'Respuesta' en la fila 'i'.
        # Almacenamos la pregunta como clave y la respuesta como valor en el diccionario.
        clave_respuestas[pregunta] = respuesta
        

    # Calcular puntuación para cada estudiante
    df_estudiantes['Puntuación'] = 0 # Agrega una nueva columna 'Puntuación' e inicializa todos los valores a 0.
    for p in preguntas: # Itera sobre cada pregunta.
        respuesta_correcta = clave_respuestas[p] # Obtiene la respuesta correcta para la pregunta actual.
        # Compara las respuestas de los estudiantes con la respuesta correcta y suma 1 por cada acierto.
        df_estudiantes['Puntuación'] = df_estudiantes['Puntuación'].add(
            # Crea una Serie booleana (True si acierta, False si no)
            (df_estudiantes[p] == respuesta_correcta).astype(int) 
            # Convierte True/False a 1/0 y lo suma a la puntuación acumulada.
        )

    # Mostrar detalle completo de respuestas
    df_detalle = df_estudiantes.copy() # Crea una copia del DataFrame de estudiantes para generar el informe detallado.
    print("\n--- INFORME DETALLADO DE RESPUESTAS ---")
    for p in preguntas: # Itera nuevamente sobre cada pregunta.
        # Marca errores añadiendo 'X' donde no coinciden con la clave
        df_detalle[p] = df_detalle[p].where(
            df_detalle[p] == clave_respuestas[p], # Condición: si la respuesta del estudiante es correcta.
            df_detalle[p] + 'X' # Si es incorrecta, concatena 'X' a la respuesta del estudiante.
        )
    
    # Ordena el DataFrame por puntuación (mayor a menor) para facilitar el análisis
    df_detalle = df_detalle.sort_values('Puntuación', ascending=False) # Ordena el informe por la puntuación de forma descendente.
    print("Leyenda: RespuestaX = Incorrecta")
    print(df_detalle.to_string(index=False)) # Imprime el DataFrame detallado sin el índice.
    
    # Mostrar resultados resumidos (solo nombre y puntuación)
    print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")
    # Selecciona solo las columnas 'Nombre' y 'Puntuación', las ordena y las imprime.
    print(df_estudiantes[['Nombre', 'Puntuación']].sort_values('Puntuación', ascending=False).to_string(index=False))
    
    # Guardar resultados
    df_estudiantes.to_csv("resultados_examen.csv", index=False) # Guarda el DataFrame de resultados en un archivo CSV.
    print("\nResultados guardados en 'resultados_examen.csv'")


# Función principal para ejecutar el flujo 
def main(): # Define la función principal del programa.
    print("Calificación de exámenes iniciada.")
    
    try: # Inicia un bloque try-except para manejar posibles errores de carga de archivos.
        # Carga las respuestas de los estudiantes desde un CSV.
        df_estudiantes = cargar_datos("../archivos/respuestas_estudiantes.csv", 'csv') 
        # Carga las respuestas correctas desde un Excel.
        df_correctas = cargar_datos("../archivos/respuestas_correctas.xlsx", 'excel') 
    except ValueError as e:
        print(f"Error al cargar datos: {e}") # Maneja errores si el tipo de archivo no es válido.
        return
    except FileNotFoundError:
        print("Error: Uno o más archivos no fueron encontrados.") # Maneja errores si no se encuentran los archivos.
        return


    preguntas = obtenerDatos(df_correctas) # Obtiene la lista de preguntas del DataFrame de respuestas correctas.
    calificar_examen(preguntas, df_estudiantes, df_correctas) # Llama a la función de calificación.
    
    print("Calificación de exámenes completada.") # Confirma la finalización.

main() # Llama a la función principal para iniciar el script.