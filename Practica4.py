print("Calculadora con una sola variable\n")

print("********************")
print("* Menu de opciones *")
print("********************\n")

print("1. Suma\n")
print("2. Resta\n")
print("3. Multiplicación\n")
print("4. División\n")
print("5. División entera\n")
print("6. Exponente\n")
print("7. Modulo o resto\n")

opcion = int(input("Introduce la opcion deseada: "))

if opcion == 1:
    print("Elegiste suma\n")
    #solicitud de numeros para calcular
    
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 + num2

    print("El resultado de la suma es: ", resultado)
elif opcion == 2:
    print("Elegiste resta\n")
    #solicitud de numeros para calcular

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 - num2

    print("El resultado de la resta es: ", resultado)
elif opcion == 3:
    print("Elegiste multiplicación\n")
    #solicitud de numeros para calcular

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 * num2

    print("El resultado de la multiplicación es: ", resultado)
elif opcion == 4:
    print("Elegiste División\n")
    #solicitud de numeros para calcular

    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    resultado = num1 / num2

    print("El resultado de la División es: ", resultado)
elif opcion == 5:
    print("Elegiste División entera\n")
    #solicitud de numeros para calcular

    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    resultado = num1 // num2

    print("El resultado de la División entera es: ", resultado)
elif opcion == 6:
    print("Elegiste Exponente\n")
    #solicitud de numeros para calcular

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    resultado = num1 ** num2

    print("El resultado del Exponente es: ", resultado)
elif opcion == 7:
    print("Elegiste Modulo o resto\n")
    #solicitud de numeros para calcular

    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    resultado = num1 % num2

    print("El resultado del Modulo o resto es: ", resultado)
