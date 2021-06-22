
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import pylab

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


def ConstruirGrafo(listaNodos, ADYACENCIA, Solucion, listacolores,valor):
  
    """print listaNodos
    print ADYACENCIA
    print Solucion
    print listacolores
    """
    
    diccionarioSolucion={}
    for i in range(0,len(listaNodos)):
        diccionarioSolucion[listaNodos[i]]= Solucion[i]

    diccionarioColores={}
    for i in range(0,len(listacolores)): #de cero hasta el numero de colores
        diccionarioColores[i] = listacolores[i]
    
    print "DICCIONARIO:  "
    print(diccionarioSolucion)
    print diccionarioColores

    ListaNodosColoreados=[]
    for i in range(0,len(listacolores)):   #un ciclo for para agrupar los nodos por color:   [ [nodos color1], [...] , [...] ,[...] ]
        #print "siguiente color: "
        #print listacolores[i]
        #print diccionarioColores[i]
        GrupoNodos=[]   #es la lista que guarda los nodos con colores en comun                   
        for k in range(0, len(listaNodos)):  #ciclo for para recorrer la Solucion y agrupar en colores
            
            #print diccionarioSolucion[listaNodos[k]]
            ColorNodo= diccionarioColores[ diccionarioSolucion[listaNodos[k]] ]
            #print ColorNodo
            if(  ColorNodo == listacolores[i]  ):
                GrupoNodos.append(listaNodos[k])
                
        #print GrupoNodos
        ListaNodosColoreados.append(GrupoNodos)
        
    print ListaNodosColoreados
    print "---------------------"
    
    ##---------------------------------------------------------------------------------------
    G=nx.Graph()
    G.add_nodes_from(listaNodos)
    
    for i in range(0,len(ADYACENCIA)):
        ady1=ADYACENCIA[i][0]
        ady2=ADYACENCIA[i][1]
        G.add_edge(ady1,ady2)

    pos = nx.spring_layout(G)
    for i in range(0, len(listacolores)):
        nx.draw_networkx_nodes(G,pos ,nodelist=ListaNodosColoreados[i],node_color= listacolores[i] ,node_size=500, alpha=0.8)

    labels={}
    for i in range(0,len(listaNodos)):
        labels[listaNodos[i]]=listaNodos[i]
   
    nx.draw_networkx_labels(G,pos ,labels,font_size=16)
    nx.draw_networkx_edges(G, pos ,width=1.0,alpha=0.5)

    print "Nodos: ", G.number_of_nodes(), G.nodes()
    print "Enlaces: ", G.number_of_edges(),G.edges()

    if(valor==1):
        resultado= "El grafo se ha coloreado CORRECTAMENTE"
    else:
        resultado= "El grafo NO ha podido colorearse correctamente !!!"
    plt.title(resultado)
    plt.axis('off')
    plt.show() 
    


def GrafoNetworkx(NOMBREGRAFO, Solucion, valor): ##recibir como parametro NOMBREGRAFO
    #NOMBREGRAFO='Grafo.txt'  ###esto se debe enviar a la funcion GrafoNetworkx
    Nodos=ObtenerVerticesGrafo(NOMBREGRAFO)
    NodosAdyacentes=ObtenerAdyacenciaGrafo(NOMBREGRAFO)
    Colors= ObtenerListadeColores()
    #print Nodos
    #print NodosAdyacentes
    ConstruirGrafo(Nodos, NodosAdyacentes, Solucion, Colors,valor)

    
#Solucion=[2,3,0,1,2,0]
#GrafoNetworkx('Grafo.txt', Solucion)


