print("Sistema para calcular el promedio de un alumno")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

matematicas = int(input(nombre+ " ¿Cual es tu calificacion en matematicas?: "))
quimica = int(input(nombre +" ¿Cual es tu calificacion en quimica?: "))
biologia = int(input(nombre + " ¿Cual es tu calificacion en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3


if promedio >= 6:
    print('Felicidades ' + nombre + '"aprobaste" con un promedio de: ',round(promedio))
else:
    print('Lo sentimos ' + nombre + ' has "reprobado" con un promedio de: ',round(promedio))
print("Fin.")

