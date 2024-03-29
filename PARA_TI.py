#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#V2
#Cuando una personsa quiere mucho a otra
#Su corazón se encarga de hacerle saber que
#Es ahí

########################## MAIN ###################################
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import random
from zlib import Z_FIXED
from PIL import Image,ImageTk,ImageSequence



xa1=0
ya1=0
c=0
xa2=0
ya2=0
class Aplicacion():
    def __init__(self):
        self.one = Tk()
        self.one.geometry('700x500')
        self.one.configure(background ='#DD969C')

        self.Bg1=PhotoImage(file="BackGrounds\Bg1.png")
        self.BG=Label(self.one,image=self.Bg1)
        self.BG.place(x=-2,y=-2)

        style1 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        
        self.one.resizable(width=False,height=False)
        self.one.title("PRINCESA")

        
        
        self.next=Button(self.one,text="NEXT",command=self.loqueSeaXD,height = 1,width = 7)
        self.next.place(x=530,y=390)
        self.next.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=20),bg="#5e00a3",fg="White",borderwidth = 5)

        self.one.mainloop()
        self.wind2.mainloop()
        
    def loqueSeaXD(self):
        global c
        global parraFo
        c=c+1
        fontTextHis = tkFont.Font(family="Comic Sans MS", size=12, weight="bold",slant="italic",font=("Segoe Script", 18,'bold'))
        if c==1:
            parraFo="Soy un Fan #1 de tus ojitos\n"
        if c==2:
            parraFo="Pensar en ti antes de dormir se convirtió\nen mi nana que me ayuda a dormir\n"
        if c==3:
            parraFo="Al verte mi corazón se pone muy feliz\n"
        if c==4:
            parraFo="No solo eres todo mi día, eres mi\n24/ 7 días de la semana"
        if(c<=4):
            self.historia=Label(self.one, text=parraFo,fg='black', bg = '#DD969C')
            self.historia.configure(font=fontTextHis)
            self.historia.pack(side=TOP)
        if c==4:
            self.next=Button(self.one,text="NEXT",command=self.Window2,height = 1,width = 7)
            self.next.place(x=530,y=390)
            self.next.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=20),bg="#7A00D3",fg="White",borderwidth = 5)
        
    def Window2(self):
        self.wind2=Tk()
        self.wind2.geometry('700x500')
        #style11 = ttk.Style()
        self.wind2.title("Antes que nada, quiero decirte que:") 
        self.wind2.configure(background='#DD969C')
        self.Bg2=PhotoImage(file="BackGrounds\Bg1.png",master=self.wind2)
        self.BGg2=Label(self.wind2,image=self.Bg2)
        self.BGg2.place(x=-2,y=-2)
        parraFo="Quizás no sea la persona\nperfecta para ti, cometo errores,\ntengo miles de defectos pero\nhago lo posible por enamorarte,\npor hacerte feliz, día a día me\nesfuerzo por darte lo mejor de mi\npara que te sientas bien y que\nseas la persona más feliz del\nmundo junto a mi."
        self.historia2=Label(self.wind2, text=parraFo,fg='black', bg = '#DD969C')
        self.historia2.configure(font=("Segoe Script", 19, 'bold'))
        
        self.historia2.pack(side=TOP)
        #style11.configure('b11',font=(family="Segoe Script",slant="italic",weight="bold",size=20))
        self.next=Button(self.wind2,text="NEXT",command=self.WindowMain,height = 1,width = 7,bg="#7A00D3",fg="White",borderwidth = 5,font=("Segoe Script", 20, 'bold','italic'))
        self.next.place(x=530,y=390)
        
        self.wind2.mainloop()

    def WindowMain(self):
        self.raiz = Tk()
        self.raiz.geometry('850x650')
        self.raiz.configure(background = '#DD969C')
        self.Bg3=PhotoImage(file="BackGrounds\Bg2.png",master=self.raiz)
        self.Bg3 = self.Bg3.zoom(2)
        self.BG3=Label(self.raiz,image=self.Bg3)
        self.BG3.place(x=-210,y=-150)
        self.raiz.config(cursor = "heart")
        style1 = ttk.Style()
        style2 = ttk.Style()
        style3 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        style2.configure('W2.TButton', font =('calibri', 25, 'bold'),foreground = 'blue')
        self.raiz.resizable(width=False,height=False)
        self.raiz.title("PERSEVERANCE")
        
        self.ques=Label(self.raiz, text="¿Quieres ser mi Novia?",fg='#9008F3', bg = '#DD969C')
        self.ques.configure(font=('Segoe Script', 45, 'bold','italic'))

        self.ques.pack(side=TOP)
        self.xa = IntVar(value=1)

        style3.configure('W3.TButton', font =('Arial', 15, 'bold'),foreground = 'black', background = '#DD969C')
        
        self.tinfo = Text(self.raiz,bg='#DD969C', width=60, height=3)      
        self.tinfo.pack(side=BOTTOM)      
        self.binfo = Button(self.raiz, text='SI', command=self.MedijoQueSI)
        self.binfo.configure(font=("Segoe Script", 20, 'bold','italic'),height = 1,width = 5,bg="#7A00D3",fg="White",borderwidth = 3)                    
        self.binfo.pack(side=LEFT)      
        self.bsalir = Button(self.raiz, text='NO', command=self.nada)
        self.bsalir.configure(font=("Segoe Script", 20, 'bold','italic'),height = 1,width = 5,bg="#7A00D3",fg="White",borderwidth = 3) 
        self.bsalir.pack(side=RIGHT)
        self.bsalir.bind("<Enter>",self.enter)
        self.raiz.mainloop()
        
    def salir(self):
        self.raiz.destroy()
        self.wind2.destroy()
        self.one.destroy()
        
    def MedijoQueSI(self):
        top = Toplevel() 
        top.geometry("380x500") 

        self.Bg4=PhotoImage(file="BackGrounds\Bg3.png",master=top)
        #self.Bg3 = self.Bg3.zoom(2)
        #self.Bg4 = self.Bg4.subsample(1)
        self.BG4=Label(top,image=self.Bg4)

        self.BG4.place(x=-5,y=-5)

        top.title("¡SI!")
        #l2 = Label(top, text = "Sabia que dirias que si mi princesa ( <3 ) TE QUIERO ∞", font =('Brush Script MT', 17, 'bold'))
        #l2.pack()
        bsalir2 = Button(top, text='SALIR', command=self.salir)
        bsalir2.configure(font=("Segoe Script", 20, 'bold','italic'),height = 1,width = 5,bg="#7A00D3",fg="White",borderwidth = 3) 
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
                x2=int(random.randrange(0,500,2))
                y2=int(random.randrange(0,310,1))
                print("se hace uso")
            xa2=x2
            ya2=y2

        if(x<7):
            self.bsalir.place(x=x2+25,y=y2)
        if(x>=7):
            x1=int(random.randrange(0,500,99))
            y1=int(random.randrange(0,380,77))
            while(abs(x1-xa1)<=70 or abs(y1-ya1)<=70):
                x1=int(random.randrange(0,500,3))
                y1=int(random.randrange(0,380,2))
                print("se hace uso")
            print("X1 -> ",x1)
            print("Y1 -> ",y1)
            self.bsalir.place(x=x1,y=y1)
            xa1=x1
            ya1=y1
        self.verinfo()
        
    def verinfo(self):
        self.tinfo.delete("1.0", END)
        self.tinfo.config(font =('Arial', 11, 'bold'),foreground = 'black', background = '#DD969C')
        x = self.xa.get()
        if(x==2):
            texto_info = "Queee........"
        elif(x==3):
            texto_info = "¡Como que no!"
        elif(x==4):
            texto_info = "Juuum... ¡Noooo! Dime que si…. (voz dramática)"
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