# Simulación de una base de datos de usuarios
def usuarios_dase_de_datos():
    usuarios = [
        {"id": 1, "type": "admin", "username": "fatima", "password": "fatima123"},
        {"id": 2, "type": "estudiante", "username": "veronica", "password": "vero123"},
        {"id": 3, "type": "estudiante", "username": "diana", "password": "diana123"},
    ]
    return usuarios


# funcion principal de login
def principal():
    print("=== Sistema de Inicio de Sesión ===")
    # Definir el número máximo de intentos
    intentos = 3
    print("total de intentos permitidos: {intentos}")
    # Bucle de intentos
    while intentos > 0:
        # Solicitar credenciales al usuario
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        # Verificar credenciales
        for usuario in usuarios_dase_de_datos():

            if usuario["username"] == username and usuario["password"] == password:
                print(f"Bienvenido, {username}!")
                print(f"ID de Usuario: {usuario['id']}")
                print(f"Tipo de Usuario: {usuario['type']}")
                return
        # Credenciales incorrectas    
        intentos -= 1
        print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")
        # Si se acaban los intentos, bloquear el acceso
        if intentos == 0:
            print("Has excedido el número de intentos. Acceso bloqueado.")
            return


principal()
