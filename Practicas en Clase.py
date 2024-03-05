a = int(input("Ingrese un numero: "))
if a > 5:
    print("El numero es mayor a 5")
elif a == 5:
    print("El numero es igual a 5")
else:
    print("El numero es menor a 5")

#Ingresar 3 valores, si A es par, mostrar la suma de B + C, si A es impar, mostrar el producto B * C
    
a = int(input("Ingresa el primer valor: "))
b = int(input("Ingresa el segundo valor: "))
c = int(input("Ingresa el tercer valor: "))
suma = b+c
multiplicacion = b*c
if a % 2 == 0:
    print(suma)
else:
    print(multiplicacion)
    
#Ingresar si dos valores correspondientes a las notas de los dos parciales: Con promedio menor a 4, se recursa
    #Con promedio entre 4 y menos de 7, rinde final
    #Con promedio mayor o igual a 7, promociona
    
parcial1 = int(input("Ingrese la nota del primer parcial: "))
parcial2 = int(input("Ingrese la nota del segundo parcal: "))
promedio = (parcial1+parcial2) / 2

if promedio < 4:
    print("El alumno recursa la materia.")
elif promedio < 7:
    print("El alumno va a final.")
else:
    print("El alumno promociona la matera.")

#Se ingresa por teclado la cantidad de materia prima necesaria para hacer chocotortas.
#Para ello, se ingreso los kilos de galletitas, queso y dulce
#Sabiendo que una chocotorta necesita: 400gr de galletitas, 250gr de queso, 150gr de dulce
#Cuantas chocotortas se pueden hacer con la cantidad ingresada.
cgalle,cqueso,cdulce = 0.4,0.250,0.150
galletita = int(input("Ingrese en kilos la cantidad de galletitas: "))
queso = int(input("Ingrese en kilos la cantidad de queso crema: "))
dulce = int(input("Ingrese en kilos la cantidad de dulce de leche: "))
choco1 = galletita / cgalle
choco2 = queso / cqueso
choco3 = dulce / cdulce
if choco1 < choco2 and choco1 < choco3:
    print("Puedo hacer", int(choco1),"chocotortas")
if choco2 < choco1 and choco2 < choco3:
    print("Puedo hacer", int(choco2), "chocotortas")
if choco3 < choco1 and choco3 < choco2:
    print("Puedo hacer", int(choco3), "chocotortas")


#Ingresar 3 valores, a, b, c, correspondientes, a la longitud de los lados de un triangulo
#Si los valores ingresados forman un triangulo
#Si forman un triangulo, cual es
#Para que una figura sea un triangulo, la suma de dos de sus lados tiene que ser mayor al tercero



