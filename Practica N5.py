import random

 
#Ejercicio 7
numeroRandom = random.randint(1,500)
print(numeroRandom)
contador = 1
while True:
    try:
        n = int(input("Adivine el valor de un numero entre 1 y 500: "))
        if n == numeroRandom:
            print(f"Advinaste! El numero es: {numeroRandom} y lo itento {contador} veces")
            break 
        elif n > numeroRandom:
            print("El numero que ingresaste es mayor al que buscas.")
            contador = contador + 1
        else:
            print("El numero que ingresaste es menor al que buscas.")
            contador = contador + 1
    except ValueError:
        print("Error, tipo de dato no valido.")

 

#Ejercicio 2

 

def sumaCadena(n,m):
    while True:
        try:
            suma = float(n) + float(m)
            break
        except ValueError:
            print("Alguna de las cadenas no es correcta, vuelva a ingresarlas: ")
            n = str(input("Ingrese la cadena 1: "))
            m = str(input("Ingrese la cadena 2: "))
        except:
            print("Error descconocido.")
    return suma

n = str(input("Ingrese la cadena 1: "))
m = str(input("Ingrese la cadena 2: "))
print(sumaCadena(n,m))

 

#Ejercicio 6
lista = []
errores = 0
n = 0
while n != -1:
    try:
        if errores == 3:
            print("Se alcanzo el limite de errores.")
            break
        n = int(input("Ingrese un valor para la lista: "))
        if n != -1:
            lista.append(n)
    except ValueError:
        print("Error, dato desconocido, por favor vuelva a ingresar.")
        errores = errores + 1
    except:
        print("Error desconocido.")
        errores = errores + 1

print(lista)

 

while True:
    try:
        m = int(input("Ingrese un valor para buscar: "))
        valor = lista.index(m)
        print(valor + 1)
        break
    except ValueError:
        print("Error, ingrese otro valor.")
        

#Ejercicio 1
        
while True:
    try:
        n = int(input("Ingrese un valor entero y mayor que 0: "))
        assert n > 0
        print(n)
        break
    except ValueError:
        print("El tipo de dato no es correcto, debe ser un entero.")
    except AssertionError:
        print("El numero que ingreso es menor que 0.")
    except:
        print("Se desconoce el error.")
    finally:
        print("Verificacion completada.")
        
#Ejercicio 3
     

def numeroMeses():    
    mesesLista = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    error = 0
    devolucion  = []
    while True:
            try:
                n = int(input("Ingrese un numero de mes que desee imprimir: "))
                assert n > 0 and n < 13
            except ValueError:
                print("Error, tipo de dato no valido.")
                error = error + 1
                break
            except AssertionError:
                print("Error, numero de mes no existe.")
                error = error + 1
                break
            except:
                print("Error desconocido.")
                error = error + 1
                break
            finally:
                break
    if error == 0:
        devolucion = mesesLista[n-1]
    return devolucion

print(numeroMeses())
            


#Ejercicio 4
seguir = 0
while True:
    try:
        for i in range(100000):
            print(i)
    except KeyboardInterrupt:
        seguirRespuesta = int(input("\nDesea detenerlo? (1 para si, 0 para no.): "))
        if seguirRespuesta == 1:
            break

import math
#Ejercicio 5

while True:
    try:
        n = int(input("Ingrese un numero entero positivo: "))
        resultado = math.sqrt(n)
        print(resultado)
        assert n >= 0
        break
    except AssertionError:
        print("Error, numero menor que 0.")
    except ValueError:
        print("Error, tipo de dato no valido.")
    except:
        print("Error desconocido.")
    
    





