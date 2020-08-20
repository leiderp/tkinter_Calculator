#-------------------------------
#Fuente: https://github.com/programacion-desde-cero/Ejemplos/blob/master/calculadora_tkinter.py curso Youtube.
#Creaci髇 de archivo ejecutable con comando: pyinstaller --onefile --windowed calculadora.py
#--------------------------------
from tkinter import Tk,Text,Button,END,re

class Interfaz:
    def __init__(self, ventana):
        #Inicializar la ventana con un titulo
        self.ventana = ventana
        self.ventana.title("Calculadora")

        #Agregar un caja de texto paa que sea la pantalla de la calculadora
        #sky blue - snow
        self.pantalla = Text(ventana,state="disabled",width=40,height=3,background="sky blue",foreground="black",font=("Helvetica",15))

        #Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        #Inicializar la operaci贸n mostrada en pantalla como string vacio
        self.operacion = ""

        #Crear los botones de la calculadora
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u"\u232B",escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u"\u00F7")
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*")
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=",escribir=False,ancho=20,alto=2)

        #Ubicar los botones
        botones = [boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17]
        contador = 0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        #Ubicar el ultimo boton al final
                botones[16].grid(row=5,column=0,columnspan=4)
    def crearBoton(self,valor,escribir=True,ancho=9,alto=1):
        return Button(self.ventana,text=valor,width=ancho,height=alto,font=("Helvetica",15),command=lambda:self.click(valor,escribir))

    #controla el evento disparado al hacer click en un bot贸n.
    def click(self,texto,escribir):
        #SI el parametro escribir es True, entonces el parametro texto se debe mostrar en pantalla, si es false no.
        if not escribir:
            #Calcular si hay una operacion a ser evaluada y si el usuario presion贸 '='
            if texto=="=" and self.operacion!="":
                #Reemplazar el valor unicode de la divisi贸n por el operador divisi贸n '/'
                self.operacion=re.sub(u"\u00F7","/",self.operacion)
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            #Si se presion贸 el boton de borrado, limpiar la pantalla
            elif texto==u"\u232B":
                self.operacion=""
                self.limpiarPantalla()
        #Mostrar texto
        else:
            self.operacion+=str(texto)
            self.mostrarEnPantalla(texto)

    #Limpia la pantalla de la calculadora
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0",END)
        self.pantalla.configure(state="disabled")


    #Muestra en la pantalla la operacion y el resultado
    def mostrarEnPantalla(self,valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state="disabled")

ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
