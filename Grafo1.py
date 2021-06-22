
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import pylab
 
#FUNCION PARA LEER EL NOMBRE DE LOS VERTICES DEL GRAFO
#Esta funcion lee un archivo de texto que contiene escrito al grafo y obtiene el nombre de los vertices
#Esta funcion unicamente lee la primera linea del archivo de texto correspondiente al grafo(.txt)
#ya que este debe tener enlistado en su primera linea (y separado por comas) el nombre de los vertices.
#por ejemplo:
#vertice1,vertice2,vertice3,vertice4 
#y asi segun corresponda al grafo.

"""
FUNCION PARA LEER EL NOMBRE DE LOS VERTICES DEL GRAFO
Esta funcion lee un archivo de texto que contiene escrito al grafo y obtiene el nombre de los vertices
Esta funcion unicamente lee la primera linea del archivo de texto correspondiente al grafo(.txt)
ya que este debe tener enlistado en su primera linea (y separado por comas) el nombre de los vertices.
por ejemplo:
vertice1,vertice2,vertice3,vertice4 
y asi segun corresponda al grafo.
"""
def ObtenerVerticesGrafo(nombre):
    lista=[]
    arch = open(nombre, 'r')
    linea = file.readline(arch)
    lista= linea.split(",")
    arch.close()
    lista.pop(len(lista)-1)
    return lista

"""
FUNCION PARA LEER EL NOMBRE DE LOS VERTICES DEL GRAFO
Esta funcion lee un archivo de texto que contiene escrito al grafo y obtiene el nombre de los vertices
Esta funcion unicamente lee la primera linea del archivo de texto correspondiente al grafo(.txt)
ya que este debe tener enlistado en su primera linea (y separado por comas) el nombre de los vertices.
por ejemplo:
vertice1,vertice2,vertice3,vertice4 
y asi segun corresponda al grafo.
"""
def ObtenerAdyacenciaGrafo(nombre):  
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

 
"""
FUNCION PARA CONSTRUIR Y REPRESENTAR AL GRAFO
Esta funcion recibe dos listas: una correspondiente al nombre de lso vertices o nodos y 
la otra correspondiente a las adyacencias del grafo, y usa networkx para construir
la estructura del grafo y representar de manera visual el grafo construido a partir del archivo .txt
"""
def ConstruirGrafo(listaNodos, ADYACENCIA):
    G=nx.Graph()
    G.add_nodes_from(listaNodos)
    
    for i in range(0,len(ADYACENCIA)):
        ady1=ADYACENCIA[i][0]
        ady2=ADYACENCIA[i][1]
        G.add_edge(ady1,ady2)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos ,nodelist=listaNodos,node_color='y',node_size=500, alpha=0.8)
    labels={}

    for i in range(0,len(listaNodos)):
        labels[listaNodos[i]]=listaNodos[i]
   
    nx.draw_networkx_labels(G,pos ,labels,font_size=16)
    nx.draw_networkx_edges(G, pos ,width=1.0,alpha=0.5)
    print "Nodos: ", G.number_of_nodes(), G.nodes()
    print "Enlaces: ", G.number_of_edges(),G.edges()
    plt.axis('off')
    plt.show() 
    return G
 

"""
FUNCION PARA INCIAR LA CONSTRUCCION Y REPRESENTACION DEL GRAFO
se recibe como parametro el nombre del grafo y se llama a las funciones
descritas anteriormenet para crear al grafo.
"""
def GrafoNetworkx(NOMBREGRAFO): 
    Nodos=ObtenerVerticesGrafo(NOMBREGRAFO)
    NodosAdyacentes=ObtenerAdyacenciaGrafo(NOMBREGRAFO)
    grafo=ConstruirGrafo(Nodos, NodosAdyacentes)
    return grafo
 

#comando para probar la funcionalidad de estas funciones
#GrafoNetworkx('Grafo.txt')    

