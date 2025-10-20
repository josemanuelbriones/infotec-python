# Usamos un diccionario de diccionarios para almacenar los datos:
# { 'matricula': { 'nombre': 'Nombre', 'materias': { 'Materia1': 8.5, 'Materia2': 5.0 } } }
DATOS_ALUMNOS = {}
# Función para validar entrada no vacía
def validar_entrada_vacia(prompt):
    # Pide una entrada y valida que no esté vacía.
    while True:
        entrada = input(prompt).strip()
        if entrada:
            return entrada
        else:
            print("No se puede dejar la información en blanco o campos vacíos.")
# Función para validar número entero positivo
def validar_numero_entero(prompt):
    # Pide y valida que la entrada sea un número entero positivo.
    while True:
        try:
            num = int(validar_entrada_vacia(prompt))
            if num > 0:
                return num
            else:
                print("Ingrese un número positivo mayor a cero.")
        except ValueError:
            print("Ingrese un número entero válido.")
# Función para validar calificación flotante
def validar_calificacion(prompt):
    # Pide y valida que la entrada sea un número flotante válido.
    while True:
        try:
            calificacion = float(validar_entrada_vacia(prompt))
            return calificacion
        except ValueError:
            print("Ingrese una calificación numérica válida.")


def sistema_evaluacion():
    
    print("\n--- Sistema de Evaluación ---")
    
    #Se pide el número de alumnos y materias
    num_alumnos = validar_numero_entero("Ingrese el número de alumnos a evaluar: ")
    num_materias = validar_numero_entero("Ingrese el número de materias por alumno: ")

    # Bucle principal para ingresar datos de cada alumno
    for i in range(1, num_alumnos + 1):
        print(f"\n--- Datos del Alumno {i} ---")
        
        # Se Pide nombre y matrícula
        nombre_alumno = validar_entrada_vacia(f"Nombre del alumno {i}: ")
        
        # Usamos la matrícula como clave única, se valida que no esté vacía
        while True:
            matricula = validar_entrada_vacia(f"Matrícula de {nombre_alumno}: ")
            if matricula not in DATOS_ALUMNOS:
                break
            else:
                print("Error: La matrícula ya existe. Ingrese una matrícula única.")
        
        # Inicializar el registro del alumno
        DATOS_ALUMNOS[matricula] = {
            'nombre': nombre_alumno,
            'materias': {},
            'estado_general': '' # Se determinará al final
        }

        # Bucle para ingresar las calificaciones de las materias
        print("\n--- Calificaciones ---")
        for j in range(1, num_materias + 1):
            nombre_materia = validar_entrada_vacia(f"Nombre de la Materia {j}: ")
            calificacion = validar_calificacion(f"Calificación de {nombre_materia} (0-10): ")
            
            # Almacena la calificación
            DATOS_ALUMNOS[matricula]['materias'][nombre_materia] = calificacion

    # Se evalua y se muestran los resultados
    print("\n" + "="*50)
    print("         REPORTE DE EVALUACIÓN FINAL")
    print("="*50)
    
    # Se recorre a todos los alumnos
    for matricula, datos in DATOS_ALUMNOS.items():
        nombre = datos['nombre']
        materias = datos['materias']
        
        print(f"\nAlumno: {nombre} (Matrícula: {matricula})")
        
        materias_reprobadas = 0
        suma_calificaciones = 0
        
        print("Materias:")
        for nombre_materia, calificacion in materias.items():
            suma_calificaciones += calificacion
            
            estado = "Aprobado" if calificacion > 6 else "Reprobado"
            
            if estado == "Reprobado":
                materias_reprobadas += 1
            
            print(f"  - {nombre_materia}: {calificacion:.2f} -> {estado}")
            
        # Determinar el estado general del alumno
        promedio = suma_calificaciones / num_materias
        datos['promedio'] = promedio
        
        if materias_reprobadas == 0:
            datos['estado_general'] = "APROBADO"
        else:
            datos['estado_general'] = f"REPROBADO ({materias_reprobadas} materia(s))"
            
        print(f"Promedio: {promedio:.2f} | Estado General: {datos['estado_general']}")
        print("-" * 20)

    # Mostrar resumen de alumnos Aprobados y Reprobados
    aprobados = [datos['nombre'] for datos in DATOS_ALUMNOS.values() if datos['estado_general'] == "APROBADO"]
    reprobados = [datos['nombre'] for datos in DATOS_ALUMNOS.values() if datos['estado_general'].startswith("REPROBADO")]

    print("\n--- Resumen General ---")
    print(f"Alumnos Aprobados: {len(aprobados)} ({', '.join(aprobados) if aprobados else 'Ninguno'})")
    print(f"Alumnos Reprobados: {len(reprobados)} ({', '.join(reprobados) if reprobados else 'Ninguno'})")
    print("--- Fin del Sistema de Evaluación ---\n")

# Ejecución del ejercicio
sistema_evaluacion()