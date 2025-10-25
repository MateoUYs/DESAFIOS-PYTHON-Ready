import random

# Lista de autos con velocidades iniciales aleatorias
autos = [("Auto1", random.randint(50, 100)), ("Auto2", random.randint(50, 100)), ("Auto3", random.randint(50, 100))]

# Duración de la carrera (10 segundos)
duracion = 10

# Simulación de la carrera
for segundo in range(duracion):
    print(f"\nSegundo {segundo + 1}:")
    for nombre, velocidad in autos:
        print(f"{nombre} avanza {velocidad} metros.")

# Calculamos la distancia total de cada auto
distancias = [(nombre, velocidad * duracion) for nombre, velocidad in autos]

# Determinamos el ganador(es)
max_distancia = max(distancia for _, distancia in distancias)
ganadores = [nombre for nombre, distancia in distancias if distancia == max_distancia]

# Mostramos el resultado
print(f"\nResultado al 22/10/2025, 11:44 AM:")
if len(ganadores) > 1:
    print(f"Empate entre: {', '.join(ganadores)} con distancia de {max_distancia} metros.")
else:
    print(f"Ganador: {ganadores[0]} con distancia de {max_distancia} metros.")

    #Usamos random.randint(50, 100) para asignar velocidades aleatorias a tres autos.
#Simulamos 10 segundos, mostrando el avance de cada auto.
#Calculamos la distancia total (velocidad × tiempo) y determinamos el ganador o ganadores en caso de empate.
    #
    #