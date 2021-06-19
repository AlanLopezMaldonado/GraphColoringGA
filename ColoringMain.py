# -*- coding: cp1252 -*-
#Alan Rodrigo Lopez Maldonado

from Tkinter import *
import Grafo1
import GeneticFunctions
import GrafoSolucion
import os
import tkFileDialog


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
    
# show an "Open" dialog box and return the path to the selected file   
def seleccionararchivo():
    filename = tkFileDialog.askopenfilename(initialdir="/grafosejemplo", title="select a file",filetypes= (("text files", "*.txt"), ("All files", "*.*")) ) 
    #fileselected =  Label(vent1, text = filename, bg="#ffffff" , font=("Arial", 14)).grid(row=4, column=1)
    #myfile=filename
    #print(myfile)
    return filename
    

def acceptt():
    vent1.destroy
    f=StringVar()
    f=myfile
    f=seleccionararchivo()
   
def salir():
    valorop.set('2')
    vent1.destroy
    exit()

def MostrarMenuPrincipal():

    global vent1,myfile,valorop
    #inicializar ventana interfaz grafica
    vent1=Tk()
    vent1.title("Sistema de Coloracion de grafos")
    colorvent1="#4f7ab3"  
    vent1.configure(background=colorvent1)
    vent1.geometry("700x600+0+0")
    #vent1.resizable(0,0)

    #varibles y labels
    myfile = StringVar()
    myfile = 'grafosejemplo\EjemploGrafo1.txt'
    #myfile = 'C:\Users\Alan\Documents\GraphColoringGA\grafosejemplo\Grafo.txt'
    #filename = myfile
    valorop=StringVar()
    #filename=StringVar()

    bienvenida =Label(vent1, text= 'Bienvenido al sistema de coloracion de grafos', bg=colorvent1, font=("Arial", 16)).grid(row=2, column=1)   #.place(x=50, y=20)
    bienvenidainfo1 =Label(vent1, text='Selecciona la opcion correspondiente a lo que deseas realizar: ', bg=colorvent1, font=("Arial", 16) ).grid(row=3, column=1)      #.place(x=50, y=400)
    #fileselected =  Label(vent1, text = myfile, bg="#ffffff", font=("Arial", 16)).grid(row=4, column=1) 
    
    #listbox de opciones 
    listboxgrafos=Listbox(vent1, width=60)
    clave= str(0) + '.  Ejecutar grafo de ejemplo' 
    listboxgrafos.insert(0, clave )
    clave= str(1) + '.  Seleccionar un grafo (.txt)' 
    listboxgrafos.insert(1, clave)
    clave= str(2) + '.  SALIR DEL SISTEMA ' 
    listboxgrafos.insert(2, clave)
    
    listboxgrafos.grid(row=5, column=1)

    #spinbox to select option
    electopcion= Spinbox(vent1, from_= 0, to= 2 ,  textvariable=valorop).grid(row=6, column=1) 

    #buttons
    botonacept=Button(vent1, text="Aceptar", command=vent1.destroy, font=("Arial", 16) ).grid(row=7, column=1)     #.place(x=200, y=500)
    #buttonSelectfile = Button (vent1, text="Seleccionar archivo", command=seleccionararchivo, font=("Arial", 16) ).grid(row=6, column=1)   #.place(x=50, y=550)
    buttonSalir = Button (vent1, text="Salir", command=salir, font=("Arial", 16) ).grid(row=8, column=1)   #.place(x=50, y=550)
    
    
    
    mainloop()

    Opcion = valorop.get()
    print(Opcion)

    if( int(Opcion) == 0):
        print("Ejecutando grafo de ejemplo:")
        RealizarAlgoritmoGenetico(myfile)
    elif (int(Opcion) == 2):
        print("HAS SALIDO SATISFACTORIAMENTE DEL SISTEMA") #implementarlo mejor como un boton
        vent1.destroy
        exit()
    elif (int(Opcion) == 1):
        print("El nombre del grafo es: ")
        NOMBREGRAFO= seleccionararchivo()
        vent1.destroy
        RealizarAlgoritmoGenetico(NOMBREGRAFO)
    else:   
        print("Ha ocurrido un error. Terminando ejecucion del sistema") #implementarlo mejor como un boton
        vent1.destroy




    """
    #listar el nombre de los archivos (de los grafos) encontrados 
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
    """

    #labels y botones de control
    #bienvenidainfo1 =Label(vent1, text='Selecciona el archivo correspondiente al grafo que deseas colorear: ', bg=colorvent1, font=("Arial", 16) ).place(x=50, y=400)
    #electopcion= Spinbox(vent1, from_= 1, to= len(ListadeGrafos)+2 ,  textvariable=valorop).place(x=50, y=500)
    
    #botonacept=Button(vent1, text="Aceptar", command=vent1.destroy, font=("Arial", 14) ).place(x=200, y=500)
    #botonsalir=Button(vent1, text="salir", command= valorop.set('6'), font=("Arial", 14) ).place(x=50, y=550)
    #buttonSalir = Button (vent1, text="Salir", command=vent1.destroy, font=("Arial", 14) ).place(x=50, y=550)
    #buttonfile=  Button(vent1, text="Seleccionar archivo", command=seleccionararchivo(), font=("Arial", 14) ).place(x=500, y=500)
    #filename = seleccionararchivo()
    #vent1.resizable(0,0)
    #vent1. mainloop()

    """
    Opcion = valorop.get()
    print Opcion

    if( int(Opcion) == n+1):
        print "FALTA IMPLEMENTAR EL ALGORITMO PARA CREAR UN NUEVO GRAFO"
    elif (int(Opcion) == n+2):
        print "HAS SALIDO SATISFACTORIAMENTE DEL SISTEMA" #implementarlo mejor como un boton
        vent1.destroy
    else:   
        print "el nombre del grafo es"
        NOMBREGRAFO=filename
        #NOMBRE= ListadeGrafos[ int(Opcion) -1 ]
        #NOMBREGRAFO = str('grafosejemplo/') + NOMBRE + str('.txt')
        print NOMBREGRAFO
        RealizarAlgoritmoGenetico(NOMBREGRAFO)
    """
    

MostrarMenuPrincipal()

