print("Programa para determinar el numero mas grande de 3 numeros\n")

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
numero3 = int(input("Introduce el tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("El numero mas grande es el primer numero")
elif numero2 > numero1 and numero2 > numero3:
    print("El numero mas grande es el segundo numero")
elif numero3 > numero2 and numero3 > numero1:
    print("El numero mas grande es el tercer numero")
