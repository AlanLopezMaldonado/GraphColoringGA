# -*- coding: cp1252 -*-
#Alan Rodrigo Lopez Maldonado
import random
import math


def Generar_Cromosomas(M, N,NC):
    Cromosoma =[]
    GeneracionListaADN= []
    for j in range (0,M):
        for i in range (0,N):
            Cromosoma.append(random.randrange(NC))   #Al cromosoma se agregan "genes" de manera aleatoria
        GeneracionListaADN.append(Cromosoma)   #luego el cromosoma, se anexa a al ADN (generacion de individuos)
        Cromosoma =[]  #lel cromosoma se vacia, para volver a llenarse
    return GeneracionListaADN  #se retorna el ADN que contiene a los cromosomas


def MostrarComparacion(cromosoma ,N, VERTICES, ADYACENCIA):
    i=0
    diccionario={}
    for i in range(0,N): #de cero hasta el numero de vertices
        #print i
        diccionario[VERTICES[i]]= cromosoma[i]    
    #luego se recorre la lista de vertices adyacentes "ADYACENCIA" y se verifica si los valores correspondientes del diccionario son iguales
    j=0
    for j in  range(0,len(ADYACENCIA)):
        colorvertice1=diccionario[ADYACENCIA[j][0]]
        print "---------"
        print ADYACENCIA[j][0]
        print colorvertice1
        colorvertice2=diccionario[ADYACENCIA[j][1]]
        print ADYACENCIA[j][1]
        print colorvertice2
        print "---------"
        if( colorvertice1 == colorvertice2):
            print "los colores son iguales. hay colision"
            


def mostrarSolucionColores(cromosoma, N, VERTICES, COLORES ):
    i=0
    diccionarioSolucion={}
    for i in range(0,N): #de cero hasta el numero de vertices
        diccionarioSolucion[VERTICES[i]]= cromosoma[i]
    for j in range(0,N):
        color= COLORES[ diccionarioSolucion[VERTICES[j]]  ]
        print( str(VERTICES[j]) + " = " + str(color)  )
        


def Fitness(cromosoma, N,VERTICES, ADYACENCIA):
    fit=0
    ##primero se crea un diccionario para relacionar los vertices con sus colores
    i=0
    diccionario={}
    for i in range(0,N): #de cero hasta el numero de vertices
        diccionario[VERTICES[i]]= cromosoma[i]    
    #luego se recorre la lista "ADYACENCIA" y se verifica si los valores
    #correspondientes del diccionario son iguales
    j=0
    for j in  range(0,len(ADYACENCIA)):
        colorvertice1=diccionario[ADYACENCIA[j][0]]
        colorvertice2=diccionario[ADYACENCIA[j][1]]
        if( colorvertice1 == colorvertice2):
            fit=fit+1        
    return fit


def Torneo(ven,N,VERTICES, ADYACENCIA):
    crom1= ven[0]
    crom2= ven[1]
    crom3= ven[2]
    ListaFitness=[ Fitness(crom1,N,VERTICES, ADYACENCIA),Fitness(crom2,N,VERTICES, ADYACENCIA), Fitness(crom3,N,VERTICES, ADYACENCIA) ]
    indice_ganador = ListaFitness.index( min(ListaFitness)) #se obtiene el indice correspondiente al cromosoma con el menor fitnes.
    crom_winner = ven[indice_ganador]   #se obtiene el cromosoma que correspnde al indice ganador
    return crom_winner


  
def Seleccion(listaGeneracion, M ,N,VERTICES, ADYACENCIA):
    Generacionseleccionada=[]   
    contador=0
    while(contador != M):       #Se realizan M iteraciones para poder obtenr una generacion con M poblaciones
        ventana=[]
        crom1=listaGeneracion[contador%M]
        crom2=listaGeneracion[(contador+1)%M]
        crom3=listaGeneracion[(contador+2)%M]
        ventana=[crom1, crom2, crom3]                 
        crom_mejorFitness = Torneo(ventana,  N,VERTICES, ADYACENCIA)  #  !!SE REALIZA EL TORNEO!!  #la poblacion ganadora se agrega a la GeneracionSeleccionada
        Generacionseleccionada.append(crom_mejorFitness)  #se va llenando una lista que contiene a las poblaciones ganadoras del torneo
        contador= contador +1

    return Generacionseleccionada



"""def mutar(gen):
    genmutado= abs(gen- (NC-1))
    return  genmutado
"""

def Mutacion(cromosoma, NC):
    index=0 
    for gen in cromosoma:
        Pm=random.randrange(100)
        if(Pm <= 20): #probabilidad del 0.2
            cromosoma[index] = abs(gen- (NC-1))
        index=index+1  
    return cromosoma #retorna el cromosoma con los genes mutados   




def Cruzamiento(parent1, parent2, NC):
    punto_de_corte= 4
    mitad_parent1 =[]
    mitad_parent2 =[]
    Pc=random.randrange(100)
    if(Pc <= 70): #probabilidad del 0.7
        mitad_parent1=  parent1[punto_de_corte : ]
        mitad_parent2=  parent2[punto_de_corte : ]
        parent1= parent1[: punto_de_corte]
        parent2= parent2[: punto_de_corte]
        for elemento in mitad_parent2:
            parent1.append(elemento)
        for elemento in mitad_parent1:
            parent2.append(elemento)
        hijo1= Mutacion(parent1,NC)
        hijo2= Mutacion(parent2,NC)
    
        return [hijo1, hijo2]
    else:
        hijo1= Mutacion(parent1,NC)
        hijo2= Mutacion(parent2,NC)
        
        return[hijo1, hijo2]



  
def Genetic_Algorithm(generacionrecibida, numgeneraciones,M, N, NC, MAXIMO, VERTICES, ADYACENCIA, COLORES):
    
    GeneracionSeleccionada = Seleccion(generacionrecibida,M ,N,VERTICES, ADYACENCIA)
    numgeneraciones+=1  #al ejecutar el algoritmo se obtiene una nueva generacion 1, 2, 3...
    contador=0
    while(contador < M ):
        listahijos=[]  #lista de hijos producto del cruzamiento de 2 cromosomas (contine a los 2 cromosomas hijos)
        listahijos= Cruzamiento(GeneracionSeleccionada[contador%M],   GeneracionSeleccionada[(contador+1)%M]  ,NC )
        #se sustituyen los cromosomas originales, por los cromosomas hijos correspondientes
        GeneracionSeleccionada[contador%M] = listahijos[0]
        GeneracionSeleccionada[(contador+1)%M] =listahijos[1]
        contador=contador+2  #avanza de dos en dos porque los cromosomas se cruzan en  pares
    bandera= 0
    for cromosoma in GeneracionSeleccionada:
        if (Fitness(cromosoma, N,VERTICES, ADYACENCIA)==0 ): #si no hay colisiones, entonces la matriz es solucion y se muestra
            print "\n\n ��� SE HA ENCONTRADO UNA SOLUCION !!! \n"
            print "El numero de iteraciones es: "
            print numgeneraciones
            print cromosoma
            mostrarSolucionColores(cromosoma, N, VERTICES, COLORES )
            #MostrarComparacion(cromosoma, N, VERTICES, ADYACENCIA)
            bandera = 1
            return cromosoma 
            break
        else:
            bandera=0
    
    if( numgeneraciones >=MAXIMO):
        print " SE HA LLEGADO AL NUMERO MAXIMO DE ITERACIONES:  " + str(MAXIMO)
        print "!!! NO SE HA PODIDO COLOREAR EL GRAFO CORRECTAMENTE !!!"
        print "Es posible que se requieran mas colores o bien, vuelva a correr el programa"
        print "\n\n"
        return GeneracionSeleccionada[1]
        
    if (bandera==0  and numgeneraciones <= MAXIMO):
        print "La generacion no cuenta con la solucion. Realizar nuevamente Genetic_Algorithm"
        GeneracionADNhija= GeneracionSeleccionada
        GeneracionSeleccionada=[]
        return Genetic_Algorithm(GeneracionADNhija, numgeneraciones,M, N, NC, MAXIMO, VERTICES, ADYACENCIA, COLORES ) 
              


#-----------------------------------------------------------------------------------------------------------------
def ObtenerListadeColores():
    lista=[]
    arch = open('Colores.txt', 'r')
    text = file.read(arch)
    lista= text.split(",")
    arch.close()
    return lista

def ObtenerVerticesGrafo(nombre):
    lista=[]
    arch = open(nombre, 'r')
    linea = file.readline(arch)
    lista= linea.split(",")
    arch.close()
    lista.pop(len(lista)-1)
    return lista

    
def ObtenerAdyacenciaGrafo(nombre):  #Crea unaclista con los pares de vertices adyacentes  [a,b] a y b son adyacentes
    lista=[]
    pardevertices=[]
    arch = open(nombre, 'r')

    linea1 = file.readline(arch)
    for linea in arch:    
        pardevertices= linea.split(",")
        pardevertices.pop(len(pardevertices)-1)
        lista.append(pardevertices)
        
    arch.close()  
    return lista
###-----------------------------------------------------------------------------------------------------------------




def MainFunction(NOMBREGRAFO):
    
    ADYACENCIA=[]
    COLORES=[]
    VERTICES=[]

    print NOMBREGRAFO
    
    #VERTICES=['a', 'b','c','d','e','f']
    VERTICES=ObtenerVerticesGrafo(NOMBREGRAFO)
    print VERTICES

    #ADYACENCIA =[['a','b'], ['d','e'], ['e','f'], ['f','a'] ,['f','b'] ,['a','c'] ,['a','d']  ]###SE DEBE RECIBIR EL GRAFO (LISTA DE ADYACENCIA)
    NodosAdyacentes=ObtenerAdyacenciaGrafo(NOMBREGRAFO)
    print NodosAdyacentes
    ADYACENCIA=NodosAdyacentes
    print ADYACENCIA
    
    #COLORES=['Azul', 'rojo', 'amarillo' ,'blanco' ]
    COLORES=ObtenerListadeColores()
    
    #aqui obtener la lista de colores que seran muchos... y usar el NC (numero cromatico) 
    #para determinar cuantos colores se agarraran y crear una lista con ese numero de colores
    #pero ojo que cuando se aumente el nc  en el algoritmo genetico, se tendra que nuevamente agrandar 
    #la lista de colores. eso es importante para que funcione bien
    
    print COLORES


    if( (NOMBREGRAFO == 'grafosejemplo/EjemploMapaLatinoamerica.txt') or (NOMBREGRAFO=='grafosejemplo/EjemploMapaUSA.txt')):
        M=100
        MAXIMO=300
    else:
        M=30  #tamanio de la muestra (numero de individuos de cada generacion)
        MAXIMO=50 #numero maximo de iteraciones
        
    N=len(VERTICES) #Numero de vertices  
    NC=len(COLORES) #numero de colores  

    NumerodeGeneraciones=0 #inicialmente se tiene una generacion 0 llenada con numeros aleatorios
    Cromosoma =[]
    GeneracionListaADN= []

    GeneracionADN= Generar_Cromosomas(M, N,NC)
    #print "\n-------------------\n"
    #for crom in GeneracionADN:
    #    print crom
    #print "\n-------------------\n\n"
      
    return Genetic_Algorithm(GeneracionADN, NumerodeGeneraciones,M, N, NC, MAXIMO, VERTICES, ADYACENCIA, COLORES) ###!!!!


#NOMBREGRAFO='Grafo.txt'
#MainFunction(NOMBREGRAFO)

