# -*- coding: utf-8 -*-
"""CifradoCesar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NKyQNCRNLEf_iAmgZwNmPxZh_gsJhw7O
"""

#Función que abre y lee  cada linea del archivo "textoCifrado", regresando como resultado el archivo.
def cargaCifrado():
    archivo = open('textoCifrado.txt', 'r')
    renglon = archivo.readline()
    archivo.close()
    return renglon

def cifraCesar(llave, cad):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for c in cad:
        if (c in alfabeto):
            pos = alfabeto.find(c)
            cifrado = cifrado + alfabeto [((pos+llave) %26)]
        else:
            cifrado + c
    return cifrado 

#Se carga el archivo que se utilizara para descifrar y enseguida se manda cerrar con un split que sireve para separar las palabras de la cadena.
def cargadic():
    arch = open("words.txt", "r")
    texto = arch.readline()
    arch.close()
    dic1 = texto.split()
    return dic1
 
#Se crea la función para descifrar y en caso de que sea incorrecto se manda otra orden
def descifradoCesar(cad, llave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    descifrado = ""
    for c in cad: 
        if (c in alfabeto):
            pos = alfabeto.find(c)
            descifrado = descifrado + alfabeto [((pos-llave) %26)]
        else: 
            descifrado = descifrado + c 
    return descifrado

#Se crea la funcion para encontrar la
def getAciertos(texto, dic):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    aciertos = " "
    lista = texto.split()
    for e in lista:
        if (e in dic):
            aciertos += str(1)
        return aciertos

#Funcion que devuelve el valor de la mejor llave.
def mejorLlave(texto):
    maxAciertos = ""
    mejorKey = ""
    dic = cargadic()
    cifrado = texto.split()
    for e in cifrado:
        for x in range (26):
            prueba = descifradoCesar(e, x)
            puntaje = getAciertos(prueba, dic)
            if (puntaje > maxAciertos):
                maxAciertos = puntaje
                mejorKey = x
    return mejorKey

#Funcion que sirve para descifrar el codigo con la mejor llave
def cesarFinal(texto):
    key = mejorLlave(texto)
    print(key)
    print(descifradoCesar(texto, key))

ej = cargaCifrado()
cesarFinal(ej)
