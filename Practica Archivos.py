def GenerarNombresPaises():
    nombres = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 4/nombres.txt","rt",encoding="utf-8")
    italia = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 4/nombresItalia.txt","wt",encoding="utf-8")
    armenia = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 4/nombresArmenia.txt","wt",encoding="utf-8")
    espana = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 4/nombresEspana.txt","wt",encoding="utf-8")   
    nombresTexto = nombres.readlines()
    for i in range(len(nombresTexto)):
        nombre = nombresTexto[i]
        separados = nombre.split()
        separados = separados[0]
        separados = str(separados)
        preguntarHasta = len(separados) - 4
        if "ini" in separados[preguntarHasta::]:
            italia.write(nombre)
        elif "ian" in separados[preguntarHasta::]:
            armenia.write(nombre)
        elif "ez" in separados[preguntarHasta::]:
            espana.write(nombre)
    nombres.close()
    italia.close()
    armenia.close()
    espana.close()
    
def EliminarComentarios():
    try:
        codigo = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 1/codigo.txt","rt")
        codigoEditar = open("C:/Users/Administrator/Desktop/archivos/Ejercicio 1/codigo.txt","at")
        codigo = codigo.readlines()
        for c in range(len(codigo)):
            linea = codigo[c]
            linea = linea.split()
            linea = linea[0]
            linea = linea[0]
            if linea == "#":
                codigoEditar.write("")
            else:
                codigoEditar.write(codigo[c])
            
    except:
        print("hola")
            
            
EliminarComentarios()            
            
            
            
            