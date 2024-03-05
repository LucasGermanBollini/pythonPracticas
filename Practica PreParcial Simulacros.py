#Simulacro Parcial
#Ejercicio 1

objetivoDeposito = int(input("Ingrese la cantidad que desea ahorrar: "))
ahorros = 0
cantidadDeposito = 0
mayorMonto = 0
posicionMayor = 0
menorMonto = 0
posicionMenor= 0

while objetivoDeposito < 80000 or objetivoDeposito > 100000:
    objetivoDeposito = int(input("Cantidad no valida, ingrese un monto entre $80000 y $100000: "))
    

while ahorros <= objetivoDeposito:
    dinero = int(input("Ingrese su deposito entre 5000 y 10000: "))
    if dinero >= 5000 and dinero <= 10000:
        ahorros = ahorros + dinero
        cantidadDeposito = cantidadDeposito + 1
        if cantidadDeposito == 1:
            menorMonto = dinero
        if dinero > mayorMonto:
            mayorMonto = dinero
            posicionMayor = cantidadDeposito
        if dinero < menorMonto:
            menorMonto = dinero
            posicionMenor = cantidadDeposito
            
    else:
     print("Error, cantidad no valida.")

print("La cantidad total de ahorros es de:",ahorros)
print("La cantidad de depositos efectuados es de:",cantidadDeposito)
print("El promedio de los depositos realizados es de:", ahorros / cantidadDeposito)
print("El monto mas alto fue de:",mayorMonto,", y fue el deposito numero:",posicionMayor)
print("El monto mas bajo fue de:",menorMonto,", y fue el deposito numero:",posicionMenor)

    