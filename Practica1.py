#titulo del sistema
print("*************************************")
print("*Sistema de control vacacional Rappi*")
print("*************************************\n")
#variables
nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departemento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: "))

#condicionales

if clave_departemento == 1:

    if antiguedad_empleado >=1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 6 dias de vacaciones")
    elif antiguedad_empleado>= 2 and antiguedad_empleado<=6:
        print("El empleado ", nombre_empleado, " tiene derecho a 14 dias de vaciones")
    elif antiguedad_empleado>=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 20 dias de vaciones")
    else:
        print("El empleado ", nombre_empleado, "  aun no tiene derecho a vaciones")

elif clave_departemento == 2:

    if antiguedad_empleado >=1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 7 dias de vacaciones")
    elif antiguedad_empleado>= 2 and antiguedad_empleado<=6:
        print("El empleado ", nombre_empleado, " tiene derecho a 15 dias de vaciones")
    elif antiguedad_empleado>=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 22 dias de vaciones")
    else:
        print("El empleado ", nombre_empleado, "  aun no tiene derecho a vaciones")
    
elif clave_departemento == 3:

    if antiguedad_empleado >=1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 10 dias de vacaciones")
    elif antiguedad_empleado>= 2 and antiguedad_empleado<=6:
        print("El empleado ", nombre_empleado, " tiene derecho a 20 dias de vaciones")
    elif antiguedad_empleado>=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 30 dias de vaciones")
    else:
        print("El empleado ", nombre_empleado, "  aun no tiene derecho a vaciones")
    
else:
    print("La clave del departamento no existe, vuelve a intentarlo")
