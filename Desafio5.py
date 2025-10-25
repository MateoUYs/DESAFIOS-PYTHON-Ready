# Función para agregar un estudiante a la lista
def agregar_estudiante(lista_estudiantes, nombre):
    lista_estudiantes.append(nombre)
    print(f"Estudiante {nombre} agregado exitosamente.")

# Función para eliminar un estudiante de la lista
def eliminar_estudiante(lista_estudiantes, nombre):
    if nombre in lista_estudiantes:
        lista_estudiantes.remove(nombre)
        print(f"Estudiante {nombre} eliminado exitosamente.")
    else:
        print(f"Error: El estudiante {nombre} no está en la lista.")

# Función para mostrar la lista de estudiantes
def mostrar_lista(lista_estudiantes):
    if len(lista_estudiantes) == 0:
        print("La lista de estudiantes está vacía.")
    else:
        print("Lista de estudiantes:", lista_estudiantes)

# Programa principal
def main():
    # Inicializamos una lista vacía para almacenar estudiantes
    estudiantes = []
    
    # Ejemplo de uso del sistema
    while True:
        print("\nOpciones: 1) Agregar, 2) Eliminar, 3) Mostrar, 4) Salir")
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            nombre = input("Ingresa el nombre del estudiante: ")
            agregar_estudiante(estudiantes, nombre)
        elif opcion == "2":
            nombre = input("Ingresa el nombre del estudiante a eliminar: ")
            eliminar_estudiante(estudiantes, nombre)
        elif opcion == "3":
            mostrar_lista(estudiantes)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutamos el programa
if __name__ == "__main__":
    main()