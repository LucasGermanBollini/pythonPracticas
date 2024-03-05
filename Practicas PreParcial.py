v = [2,7,5,1,6]

desordenada = 0
while desordenada == 0:
    desordenada = 1
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            aux = v[i]
            v[i] = v[i+1]
            v[i+1] = aux
            desordenada = 0
print(v)

import random

lista = []
def listaSinRepetidos(n):
    for i in range(0,n,1):
        m = random.randint(0,100)
        lista.append(m)
        repetidos = 0
        j = 0
        if len(lista) >= 2:
            while repetidos == 0 and j < len(lista) - 1:
                if lista[j] == lista[j+1]:
                    del lista[j]
                    repetidos = 1
                else:
                    j = j + 1
    return lista

n = int(input("Valor: "))
print(listaSinRepetidos(n))

def busquedabinaria(v,dato):
    izq= 0
    der = len(v) - 1
    pos= -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos= centro
        elif v[centro] < dato:
            izq= centro + 1
        else:
            der = centro - 1 
    return pos

m = [15,25,62,43,92,10]
n = [12,26,70,59,100,200,300]

def ordenar(v):
    desordenada = 0
    while desordenada == 0:
        desordenada = 1
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenada = 0
    return v

print(ordenar(m))
print(ordenar(n))

nuevaLista = []
j = 0
largo = len(m) + len(n)
while len(nuevaLista) < largo:
    if m == []:
        nuevaLista.append(n[j])
        j = j + 1
    if n == []:
        nuevaLista.append(m[j])
        j = j + 1
    if n != [] and m != []:
        if m[j] < n[j]:
            nuevaLista.append(m[j])
            del m[j]
        elif m[j] > n[j]:
            nuevaLista.append(n[j])
            del n[j]
        else:
            nuevaLista.append(m[j])
            del m[j]
        
print(nuevaLista)

#Ejercicio 4
import random

def cuantasVecesAparece(n):
    v = []
    j = 0
    contador = 0
    while len(v) < 10:
        v.append(random.randint(1,10))
    print(v)
    while j < len(v):
        if v[j] == n:
            contador = contador + 1
            j = j + 1
        else:
            j = j + 1
    print(contador)

n = int(input("Ingrese un valor a buscar en una lista con 10 numeros al azar: "))
cuantasVecesAparece(n)

#Ejercicio 5
def invertida(lista):
    v = []
    largo = len(lista)
    j = len(lista) - 1
    while len(v) < largo:
        v.append(lista[j])
        j = j - 1
    print(v)
    
l = [1,2,3,4,5,6,7,8,23,2,1,2]
invertida(l)

#Ejercicio 12

lista = [10,20,30,40,50,70,90,100]
def insertar(lista,n):
    j = 0
    largo = len(lista)
    while len(lista) - 1 < largo:
        if n <= lista[j]:
            lista.insert(j,n)
        elif n >= lista[j] and n <= lista[j+1]:
            lista.insert(j+1, n)
        elif n > lista[len(lista) - 1]:
            lista.insert(len(lista), n)
        else:
            j = j + 1
    return lista

print(insertar(lista,25))

#Ejercicio 6

def buscarElemento(lista,n):
    j = 0
    v = []
    while j < len(lista):
        if lista[j] == n:
            v.append(j + 1)
            j = j + 1
        else:
            j = j + 1
    return v


import random
a = []
b = []
n = int(input("Ingrese la cantidad de numeros que desea en cada lista: "))
for i in range(0,n,1):
    a.append(random.randint(0,100))
for i in range(0,n,1):
    b.append(random.randint(0,100))

def concatenacion(a,b):
    v = []
    j = 0
    while j < len(a):
        if a[j] % 2 == 0:
            v.append(a[j])
        if b[j] % 2 != 0:
            v.append(b[j])
        j = j + 1
    return v

def concatenacion2(a,b):
    v = []
    j = 0
    while j < len(a):
        if a[j] % 2 != 0:
            v.append(a[j])
        if b[j] % 2 == 0:
            v.append(b[j])
        j = j + 1
    return v

def intercalado(a,b):
    v = []
    for i in range(0, len(a) ,1):
        v.append(a[i])
        v.append(b[i])
    return v

print(a)
print(b)
print(concatenacion(a,b))
print(concatenacion2(a,b))
print(intercalado(a,b))

#Ejercicio 10
a = []
b = []
for i in range(0,10,1):
    a.append(random.randint(0,10))
for i in range(0,10,1):
    b.append(random.randint(0,10))
print(a)
print(b)
j = 0
i = 0

def ordenamiento(v):
    desordenado = True
    while desordenado == True:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v

print(ordenamiento([2,3,5,1,2,4,6,1]))
            
def binaria(v,dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        elif v[centro]<dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

print(binaria(ordenamiento([2,3,5,1,2,4,6,1]),5))
    

def orden(v):
    desordenado = True
    while desordenado == True:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v

print(orden([2,65,1,3,5,7]))

def bina(v,dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos
            
print(bina([1,2,3,4,5],2))            

def ordenar(v):
    desordenado = True
    while desordenado == True:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v

print(ordenar([1,2,35,7,3]))

def binario(v,dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

print(binario(ordenar([1,2,35,7,3]),3))


#vector = lista unidimensional de elementos de la biblioteca NumPy
#listas = Conjunto de elementos en python, flexibles por lo que se pueden modificar
#las variables pueden contener: minusculas, mayusculas, digitos y guion bajo, nunca pueden empezar con numero, tampoco
#pueden ser palabras reservadas\

def ordenar(v):
    desordenado = True
    while desordenado == True:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True                
    return v

b = [2,3,5,6,7,1]
print(ordenar(b))

def binario(v,dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        if v[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

print(binario(ordenar(b),3))

def ordenar(v):
    desordenado = True
    while desordenado == True:
        desordenado = False
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v

v = [2,3,5,6,7,1]

print(ordenar(v))

def binario(v,dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        if v[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

