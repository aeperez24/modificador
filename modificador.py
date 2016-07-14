# hecho por andres Perez (syzo)
#14/07/2016
#!/usr/bin/python
import os
import sys
def LecturaArchivo(x):

    archvio=open(x,'r')
    salida=archvio.read()
    archvio.close()
    return salida

def EscrituraArchivo(nombreArchivo,contenido):
    fout=open(nombreArchivo,'w')
    fout.write(contenido)

def modifica(ruta,candenaBuscar,cadenaRemplazadora):
    lect=LecturaArchivo(ruta)
    salida=lect.replace(candenaBuscar,cadenaRemplazadora)
    EscrituraArchivo(ruta,salida)

def busqueda(prefix,sufix):
    search=os.popen("find "+prefix+" -iname '*."+sufix+"' -readable")
    contenido=search.read()
    listaResultante=contenido.split('\n')
    return listaResultante

if(len(sys.argv)==5):
    os.system("clear")
    print("ruta de la raiz \t:\t"+sys.argv[1])
    print("sufijo es \t\t:\t"+sys.argv[2])
    print("cadena a sustituir es \t:\t"+sys.argv[3])
    print("cadena sustituta es \t:\t"+sys.argv[4])
    nb=raw_input("presione 1 para continuar o cualquier otra tecla para abortar\n")

    if(nb=="1"):
        var=0
        print "modificando:"
        lineas=busqueda(sys.argv[1],sys.argv[2])
        while (var<len(lineas)-1):
            print(lineas[var])
            modifica(lineas[var],sys.argv[3],sys.argv[4])
            var=var+1;
        print("finalizado")
        print("archivos modificados\t:\t"+str(var))
    else:
        print("abortado")

else:
    print("syntaxis debe ser : python modificador.py ruta_de_la_raiz sufijo candea_a_sustituir cadena_sustitura")
