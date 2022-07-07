#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Cuando una personsa quiere mucho a otra
#Su corazón se encarga de hacerle saber que
#Es ahí
########################## MAIN ###################################
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
class Aplicacion():
    def __init__(self):
        self.one = Tk()
        self.one.geometry('700x500')
        self.one.configure(background = 'pink')
        style1 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        
        self.one.resizable(width=False,height=False)
        self.one.title("PRINCESA")

        self.next=Button(self.one,text="next",command=self.loqueSeaXD)
        self.next.place(x=350,y=400)

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
        parraFo="Quizás no sea la persona\nperfecta para ti, cometo errores,\ntengo miles de defectos; pero.\nhago lo posible por enamorarte,\npor hacerte feliz, día a día me\nesfuerzo por darte lo mejor de mi\npara que te sientas bien y que\nseas la persona más feliz del\nmundo junto a mi."
        self.historia2=Label(self.wind2, text=parraFo,fg='black', bg = 'pink')
        self.historia2.configure(font=('Comic Sans MS', 16, 'bold'))
        self.historia2.pack(side=TOP)
        self.next=Button(self.wind2,text="next22",command=self.WindowMain)
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
        self.raiz.resizable(width=False,height=False)
        self.raiz.title("PERSEVERANCE")
        self.ques=Label(self.raiz, text="¿Quieres ser mi Novia?", font=("Bradley Hand ITC", 30, 'bold'),fg='blue', bg = 'pink')
        self.ques.pack(side=TOP)
        self.xa = IntVar(value=1)

        style3.configure('W3.TButton', font =('Arial', 15, 'bold'),foreground = 'black', background = 'pink')
        
        self.tinfo = Text(self.raiz,bg='pink', width=60, height=3)      
        self.tinfo.pack(side=BOTTOM)      
        self.binfo = ttk.Button(self.raiz, text='SI', style='W2.TButton', command=self.createNewWindow)                    
        self.binfo.pack(side=LEFT)      
        self.bsalir = ttk.Button(self.raiz, text='NO',style = 'W.TButton', command=self.nada)
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
        l2.pack()
        bsalir2 = ttk.Button(top, text='SALIR', command=self.salir)
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

        if(x<7):
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
            xa1=x1
            ya1=y1
        self.verinfo()
        
    def verinfo(self):
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
            texto_info = "¿No puedes decir no?  jajajajajajajajajajajajajajajaa  <3 "
        self.tinfo.insert("2.0", texto_info)
        
def main():
    mi_app = Aplicacion()

    return 0
if __name__ == '__main__':
    main()