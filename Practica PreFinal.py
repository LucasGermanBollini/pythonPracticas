import math

def ejercicio1():
    try:
        numero = int(input())
        if numero < 0:
            print("Dato invalido.")
            ejercicio1()
    except ValueError:
        print("Dato invalido.")
        return ejercicio1()
    else:
        return "Validado"
        
def ejercicio2():
    try:
        c1 = input()
        c2 = input()
        c1 = int(c1)
        c2 = int(c2)
    except ValueError:
        print("-1")
        return ejercicio2()
    else:
        r = c1 + c2
        return r
        
def ejercicio3(inicio=0):
    try:
        for i in range(inicio,1000):
            print(i)
    except KeyboardInterrupt:
        r = input(f"\nDetenerse?")
        if r == "0":
            ejercicio3(i)
        else:
            print(f"Detendio en {i}")
 
def ejercicio4():
    try:
        n=int(input())
        n = math.sqrt(n)
    except ValueError:
        return ejercicio4()
    else:
        return n
    

def ejercicio5():
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    try:
        n=int(input())
        n = n - 1
        if n < 0:
            n = 13
        r=meses[n]
    except IndexError:
        print([])
        return ejercicio5()
    else:
        return r
    
def ejercicio6():
    f = 0
    while f < 3:
        try:
            n = 0
            l=[]
            while n != -1:         
                n=int(input())
                l.append(n)
            b = int(input())
            r = l.index(b)
            return r 
        except ValueError:
            b = int(input())
            r = l.index(b)
            f = f+1
        
print(ejercicio6())
        