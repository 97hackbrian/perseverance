#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##########################MAIN###################################
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import random
from zlib import Z_FIXED
xa1=0
ya1=0
c=0

xa2=0
ya2=0

#x1=int(random.randint(0,500))
#y1=int(random.randint(0,600))
# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 
class Aplicacion():
    
    
    
    
    
    
    def __init__(self):

    
        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto 
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es 
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        self.one = Tk()
        self.one.geometry('700x500')
        self.one.configure(background = 'pink')
        style1 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        self.one.resizable(width=False,height=False)
        self.one.title("PRINCESA")
        #fontTextHis = tkFont.Font(family="Comic Sans MS", size=14, weight="bold",slant="italic")
        #parraFo="La historia cuenta que.... \n Una vez dos personas se se vieron sin imaginarse que algún día \n llegarian a estar juntos......"
        #self.historia=Label(self.one, text=parraFo,fg='black', bg = 'pink')
        #self.historia.configure(font=fontTextHis)
        #self.historia.pack(side=TOP)
        self.next=Button(self.one,text="next",command=self.loqueSeaXD)
        self.next.place(x=350,y=400)
        #self.binfo.focus_set()
        
        self.one.mainloop()
        self.wind2.mainloop()
        
    
        
    def loqueSeaXD(self):
        global c
        global parraFo
        c=c+1
        fontTextHis = tkFont.Font(family="Comic Sans MS", size=14, weight="bold",slant="italic")
        if c==1:
            parraFo="1a"
            
        if c==2:
            parraFo="2b"
            
        if c==3:
            parraFo="3c"
            
        if c==4:
            parraFo="4d"
        
        if(c<=4):
            self.historia=Label(self.one, text=parraFo,fg='black', bg = 'pink')
            self.historia.configure(font=fontTextHis)
            self.historia.pack(side=TOP)
        if c==4:
            self.next=Button(self.one,text="next",command=self.Window2)
            self.next.place(x=350,y=400)
        
        

        
    def Window2(self):
        self.wind2=Tk()
        self.wind2.geometry('700x500')
        self.wind2.configure(background='pink')
        fontTextHis = tkFont.Font(family="Comic Sans MS", size=14, weight="bold",slant="italic")
        
        parraFo="hola"
        self.historia2=Label(self.wind2, text=parraFo,fg='black', bg = 'pink')
        self.historia2.configure(font=fontTextHis)
        self.historia2.pack(side=TOP)
        
        
        self.next=Button(self.wind2,text="next2",command=self.WindowMain)
        self.next.place(x=350,y=400)
        self.wind2.mainloop()

    def WindowMain(self):
        self.raiz = Tk()
        self.raiz.geometry('600x400')
        self.raiz.configure(background = 'pink')
        style1 = ttk.Style()
        style2 = ttk.Style()
        style3 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        style2.configure('W2.TButton', font =('calibri', 15, 'bold'),foreground = 'blue')
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        self.raiz.resizable(width=False,height=False)
        self.raiz.title("PERSEVERANCE")



        self.ques=Label(self.raiz, text="¿Quieres ser mi Novia?", font=("Bradley Hand ITC", 30, 'bold'),fg='blue', bg = 'pink')
        self.ques.pack(side=TOP)
        self.xa = IntVar(value=1)#VALOR DE VARIBLE AUXILIAR PARA EL BOTON
        #self.posx= IntVar(value=x1)
        #self.posy= IntVar(value=y1)
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:

        style3.configure('W3.TButton', font =('Arial', 15, 'bold'),foreground = 'black', background = 'pink')
        
        self.tinfo = Text(self.raiz,bg='pink', width=60, height=3)#40 10 
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=BOTTOM)
        
        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.binfo = ttk.Button(self.raiz, text='SI', style='W2.TButton', command=self.createNewWindow)
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        self.binfo.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='NO',style = 'W.TButton', command=self.nada)

        #self.bsalir.grid(row = 2, column = 2, sticky = W)

        #self.bsalir.configure(self.raiz, bg = "blue")
        #self.bsalir.pack()
                                  #command=self.raiz.destroy)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
        self.bsalir.pack(side=RIGHT)
        self.bsalir.bind("<Enter>",self.enter)
        self.raiz.mainloop()

    def salir(self):
        self.raiz.destroy()
        self.wind2.destroy()
        self.one.destroy()

      
    def createNewWindow(self):
        top = Toplevel() 
        top.geometry("650x230") 
        top.title("¡SI!") 
        l2 = Label(top, text = "Sabia que dirias que si mi princesa ( <3 ) TE QUIERO ∞", font =('Brush Script MT', 17, 'bold'))
        #ttk().self.l2.config(font =('Arial', 11, 'bold'),foreground = 'black', background = 'pink')
        
        l2.pack()
        bsalir2 = ttk.Button(top, text='SALIR', command=self.salir)
                                  #command=self.raiz.destroy)
        bsalir2.pack(side=BOTTOM)
        top.mainloop() 
    
    

    def nada(self):
        print("nada")

        
    def enter(self, *args):
        
        global xa1
        global ya1

        global xa2
        global ya2
        x = self.xa.get()
        self.xa.set(x+1)
        print("C -> ",x)
        if(x<7):
            x2=int(random.randrange(0,500,11))
            y2=int(random.randrange(0,310,7))
            if(abs(x2-xa2)<=50 and abs(y2-ya2)<=50):
                x2=int(random.randrange(0,500,2))#7#
                y2=int(random.randrange(0,310,1))#5#
                print("se hace uso")
            xa2=x2
            ya2=y2
        #if(x==1):
            #x2=int(random.randrange(380,500,7))
            #y2=int(random.randrange(200,380,7))
            #self.bsalir.place(x=x2,y=y2)
        #if(x==2):
            ##x2=int(random.randrange(380,500,7))
            ##y2=int(random.randrange(200,380,5))
            #self.bsalir.place(x=x2+20,y=y2)
        if(x<7):
            ##x2=int(random.randrange(380,500,3))
            ##y2=int(random.randrange(200,380,3))
            self.bsalir.place(x=x2+25,y=y2)
        if(x>=7):
            x1=int(random.randrange(0,500,99))
            y1=int(random.randrange(0,380,77))
            while(abs(x1-xa1)<=70 or abs(y1-ya1)<=70):
                x1=int(random.randrange(0,500,3))#7#
                y1=int(random.randrange(0,380,2))#5#
                print("se hace uso")
            print("X1 -> ",x1)
            print("Y1 -> ",y1)
            self.bsalir.place(x=x1,y=y1)
             #self.xa.set(1)
            xa1=x1
            ya1=y1
        self.verinfo()

        
    def verinfo(self):    
        # Borra el contenido que tenga en un momento dado
        # la caja de texto
        
        self.tinfo.delete("1.0", END)
        self.tinfo.config(font =('Arial', 11, 'bold'),foreground = 'black', background = 'pink')
        x = self.xa.get()
        if(x==2):
            texto_info = "queee........"
        elif(x==3):
            texto_info = "¡Como que no!"
        elif(x==4):
            texto_info = "Juuum... ¡MALVADA!"
        elif(x==5):
            texto_info = "jajajaja no puedes.."
        elif(x==6):
            texto_info = "jajajaa como que no XD"
        elif(x==7):
            texto_info = "jajajaa sigue intentandoo -te pasas - Muah! - Te quiero mucho - Muah!"
        elif(x>=8):
            texto_info = "¿No puedes decir no?  jajajajjajajjajajajajajajjajajajaa  <3 "    
        
        self.tinfo.insert("1.0", texto_info)

def main():
    mi_app = Aplicacion()
    
    
    return 0

if __name__ == '__main__':
    main()
