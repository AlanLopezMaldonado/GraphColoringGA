import tkinter as tk
import Grafo1
import GeneticFunctions
import GrafoSolucion
import os
import tkFileDialog


class Test():
    def __init__(self):
        #Variables definidas
        color="#4f7ab3" 
        
        #cofigure tk window root
        self.root = tk.Tk()
        #self.root.geometry("200x80")
        self.root.title("Sistema de Coloracion de grafos") 
        self.root.configure(background=color)
        self.root.geometry("600x200+0+0")
        self.root.resizable(0,0)

        #se declara una variable correspondiente al nombre del grafo
        self.nombregrafo = tk.StringVar()
        self.nombregrafo.set("grafosejemplo\EjemploGrafo1.txt")

        #labels and buttons
        self.labelname = tk.Label(self.root,
                              textvariable=self.nombregrafo)
        self.buttonchange = tk.Button(self.root,
                                text="Seleccionar Grafo",
                                command=self.seleccionarGrafo)
        self.button = tk.Button(self.root,
                                text="Colorear grafo de ejemplo",
                                command=self.ejecutarGrafoEjemplo)
        self.buttonsalir = tk.Button(self.root,
                                text="Salir",
                                command=self.root.destroy)
        self.buttonColorear = tk.Button(self.root,
                                text="Colorear Grafo", bg="green",
                                command=self.aceptar)
        self.label = tk.Label(self.root,bg="red", font=("Arial", 10),
                              text="Por favor cierra las ventanas para continuar la ejecucion del programa")

        #packing elements in root
        self.button.pack()
        self.buttonchange.pack()
        self.buttonColorear.pack()
        self.buttonsalir.pack()
        self.labelname.pack()
        self.root.mainloop()

    #functions
    def clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "dos":
            os.system("cls")
        elif os.name == "nt":
            os.system("cls")
        elif os.name == "ce":
            os.system("cls")


    def ejecutarGrafoEjemplo(self):
        filename='grafosejemplo\Grafo.txt'
        #print(self.labelname["text"])  
        #print("el grafo ejemplo es: " + self.nombregrafo.get())   
        print("el grafo ejemplo es: " + filename)  
        
        #self.root.destroy
        self.label.pack()
        self.buttonchange["state"] = "disabled"
        self.button["state"] = "disabled"
        self.buttonColorear["state"] = "disabled"

        Grafo1.GrafoNetworkx(filename)
        Solucion,valor= GeneticFunctions.MainFunction(filename)
        GrafoSolucion.GrafoNetworkx(filename, Solucion,valor)
        print("ELVALOR DE LA BANDERA ES " + str(valor) )
        raw_input("Press Enter to continue...")
        self.clear()
        Test()


    def seleccionarGrafo(self):
        #filename="grafosejemplo\Grafo.txt"
        filename= tkFileDialog.askopenfilename(initialdir="/grafosejemplo", title="select a file",filetypes= (("text files", "*.txt"), ("All files", "*.*")) ) 
        self.nombregrafo.set(filename)
        self.labelname.pack_forget()
        self.labelname.destroy
        self.labelname = tk.Label(self.root,textvariable=self.nombregrafo)
        self.labelname.pack()
        #print(self.labelname["text"]) 
        #print(self.nombregrafo.get()) 
        """
        print(filename)
        Grafo1.GrafoNetworkx(filename)
        Solucion= GeneticFunctions.MainFunction(filename)
        GrafoSolucion.GrafoNetworkx(filename, Solucion)
        raw_input("Press Enter to continue...")
        self.clear()
        Test()
        """


    def aceptar(self):
        print("has presionado el boton de aceptar\n")
        print(self.nombregrafo.get()) 
        filename=""+self.nombregrafo.get()
        print(filename)
        #ajustando interfaz grafica
        self.label.pack()    #se agrega un label que indica cerrar ventanas y se desabilitan los botones
        self.buttonchange["state"] = "disabled"
        self.button["state"] = "disabled"
        self.buttonColorear["state"] = "disabled"

        Grafo1.GrafoNetworkx(filename)
        Solucion,valor= GeneticFunctions.MainFunction(filename)
        GrafoSolucion.GrafoNetworkx(filename, Solucion,valor)
        print("ELVALOR DE LA BANDERA ES " + str(valor) )
        raw_input("Press Enter to continue...")
        self.clear()
        Test()

app=Test()