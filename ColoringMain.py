# -*- coding: cp1252 -*-
#Alan Rodrigo Lopez Maldonado

from Tkinter import *
import Grafo1
import GeneticFunctions
import GrafoSolucion
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "dos":
        os.system("cls")
    elif os.name == "nt":
        os.system("cls")
    elif os.name == "ce":
        os.system("cls")

def RealizarAlgoritmoGenetico(NOMBREGRAFO):
    Grafo1.GrafoNetworkx(NOMBREGRAFO)
    Solucion= GeneticFunctions.MainFunction(NOMBREGRAFO)
    GrafoSolucion.GrafoNetworkx(NOMBREGRAFO, Solucion)
    raw_input("Press Enter to continue...")
    clear()
    MostrarMenuPrincipal()
    
#funcion incesesaria. solo para lectura de los ejemplos
def ObtenerNombresGrafos():
    lista=[]
    arch = open('grafosejemplo/ListaDeNombresDeGrafos.txt', 'r') #se abre solo para lectura
    text = file.read(arch)
    lista= text.split(",")
    arch.close()
    return lista

    
    
def MostrarMenuPrincipal():

    #ListadeGrafos=[ 'Grafo.txt' ,'Grafo.txt', 'Grafo.txt']
    ListadeGrafos=[]
    ListadeGrafos= ObtenerNombresGrafos()
    print "la lista de nombres de grafos es:"
    print ListadeGrafos

    
    vent1=Tk()
    vent1.title("Sistema de Coloracion de grafos")
    colorvent1="#4f7ab3"  
    vent1.configure(background=colorvent1)
    vent1.geometry("700x600+0+0")
    valorop=StringVar()
    bienvenida =Label(vent1, text= 'Bienvenido. Aqui se muestra la lista de grafos disponibles', bg=colorvent1, font=("Arial", 13)).place(x=50, y=20)

    #se debe mostrar el nombre delos grafos en un cuadro de texto
    #for i in listadeGrafos:
    #   agrega al textbox:  strt(i) + ". " + ListadeGrafos[i]

    listboxgrafos=Listbox(vent1, width=60)
    for i in range(0,len(ListadeGrafos)):
        clave= str(i+1) + '.  ' +  ListadeGrafos[i]
        listboxgrafos.insert(i, clave )
    n=len(ListadeGrafos)
    clave= str(n+1) + '. AGREGAR UN NUEVO GRAFO' 
    listboxgrafos.insert(n+1, clave)
    clave= str(n+2) + '. SALIR DEL SISTEMA ' 
    listboxgrafos.insert(n+2, clave)
    listboxgrafos.place(x=50, y=100)

    bienvenidainfo1 =Label(vent1, text='Selecciona la clave del grafo que deseas colorear: ', bg=colorvent1, font=("Arial", 16) ).place(x=50, y=400)
    electopcion= Spinbox(vent1, from_= 1, to= len(ListadeGrafos)+2 ,  textvariable=valorop).place(x=50, y=500)
    
    botonacept=Button(vent1, text="Aceptar", command=vent1.destroy, font=("Arial", 14) ).place(x=200, y=500)
    #botonsalir=Button(vent1, text="salir", command= valorop.set('6'), font=("Arial", 14) ).place(x=50, y=550)
    
    vent1.resizable(0,0)
    mainloop()

    Opcion = valorop.get()
    print Opcion

    if( int(Opcion) == n+1):
        print "FALTA IMPLEMENTAR EL ALGORITMO PARA CREAR UN NUEVO GRAFO"
    elif (int(Opcion) == n+2):
        print "HAS SALIDO SATISFACTORIAMENTE DEL SISTEMA" #implementarlo mejor como un boton
        vent1.destroy
    else:   
        print "el nombre del grafo es"
        NOMBRE= ListadeGrafos[ int(Opcion) -1 ]
        NOMBREGRAFO = str('grafosejemplo/') + NOMBRE + str('.txt')
        print NOMBREGRAFO
        RealizarAlgoritmoGenetico(NOMBREGRAFO)
    
   


MostrarMenuPrincipal()

