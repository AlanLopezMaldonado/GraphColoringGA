
import os, sys
import networkx as nx
import matplotlib.pyplot as plt
import pylab



def ObtenerVerticesGrafo(nombre):
    lista=[]
    arch = open(nombre, 'r')
    linea = file.readline(arch)
    lista= linea.split(",")
    arch.close()
    lista.pop(len(lista)-1)
    return lista



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




def ConstruirGrafo(listaNodos, ADYACENCIA):
    G=nx.Graph()
    G.add_nodes_from(listaNodos)
    
    for i in range(0,len(ADYACENCIA)):
        ady1=ADYACENCIA[i][0]
        ady2=ADYACENCIA[i][1]
        G.add_edge(ady1,ady2)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos ,nodelist=listaNodos,node_color='w',node_size=500, alpha=0.8)
    labels={}

    for i in range(0,len(listaNodos)):
        labels[listaNodos[i]]=listaNodos[i]
   
    nx.draw_networkx_labels(G,pos ,labels,font_size=16)
    nx.draw_networkx_edges(G, pos ,width=1.0,alpha=0.5)
    print "Nodos: ", G.number_of_nodes(), G.nodes()
    print "Enlaces: ", G.number_of_edges(),G.edges()
    plt.axis('off')
    plt.show() 
    



def GrafoNetworkx(NOMBREGRAFO): 
    Nodos=ObtenerVerticesGrafo(NOMBREGRAFO)
    NodosAdyacentes=ObtenerAdyacenciaGrafo(NOMBREGRAFO)
    print Nodos
    print NodosAdyacentes
    ConstruirGrafo(Nodos, NodosAdyacentes)
    


#GrafoNetworkx('Grafo.txt')

