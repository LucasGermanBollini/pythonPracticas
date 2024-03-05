
#Principio del programa1
print("Mi nombre es Lucas Bollini")
print()
print("Estoy cursando Lic. En Sistemas")
#Fin del programa1


nombre = input("Ingrese su nombre: ")
print("Su nombre es:", nombre)
numero1 = int((input("Ingrese su edad: ")))
numero2 = 5 + numero1
print(numero2)


#Suma de dos numeros
a = int(input("Ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
suma = a + b
print("La suma de", a, "y", b, " es de", suma)


#Superficie de cuadrado/rectangulo
l1 = int(input("Ingrese el valor del primer lado: "))
l2 = int(input("Ingrese el valor del segundo lado: "))
print("La superficie tiene un valor de:", l1 * l2)

#Cambio de variable
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))
print("A tiene el valor de:", a , "y B tiene el valor de:", b)
c = a
a = b
b = c
print("Ahora A tiene el valor de:", a , "y B tiene el valor de:", b)