#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#V2
#Cuando una personsa quiere mucho a otra
#Su corazón se encarga de hacerle saber que
#Es ahí
'''
########################## MAIN 6Meses###################################
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import random
from zlib import Z_FIXED
from PIL import Image,ImageTk,ImageSequence
import time


xa1=0
ya1=0
c=0
xa2=0
ya2=0

sizeMain='1024x720'
sizeW1='800x600'
sizeW2='700x500'
xlide=0
def on_enter(e):
    e.widget.config(text=e.widget.cget('text').upper())

def on_leave(e):
    e.widget.config(text=e.widget.cget('text').capitalize())
class Aplicacion():
    
    def __init__(self):
        global xlide
        self.one = Tk()
        self.one.geometry(sizeW2)
        self.one.configure(background ='#DD969C')

        self.Bg1=PhotoImage(file="BackGrounds\Bg1.png")
        self.BG=Label(self.one,image=self.Bg1)
        self.BG.place(x=-2,y=-2)

        style1 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        
        self.one.resizable(width=False,height=False)
        self.one.title("MI PRINCESA")
        
        self.BgMeses=PhotoImage(file="BackGrounds\Mgs.png")
        photo = PhotoImage(file = r"BackGrounds\Mgs.png")
        photoimage = photo.subsample(2, 3)
        self.fontTextHis = tkFont.Font(family="Comic Sans MS", size=8, weight="bold",slant="italic",font=("Segoe Script", 10,'bold'))
        self.m1=Label(self.one,text="",fg='black',bg="white",font=self.fontTextHis).place(x=91,y=35)
        

        self.mg1=Button(self.one,height = 110,width = 190,command=self.Mgs1,image = photoimage,compound = CENTER)
        self.mg1.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg1.place(x=90,y=35)
        
        self.mg2=Button(self.one,height = 110,width = 190,command=self.Mgs2,image = photoimage,compound = CENTER)
        self.mg2.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg2.place(x=410,y=35)
        
        self.mg3=Button(self.one,height = 110,width = 190,command=self.Mgs3,image = photoimage,compound = CENTER)
        self.mg3.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg3.place(x=10,y=190)
        
        self.mg4=Button(self.one,height = 110,width = 190,command=self.Mgs4,image = photoimage,compound = CENTER)
        self.mg4.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg4.place(x=250,y=190)

        self.mg5=Button(self.one,height = 110,width = 190,command=self.Mgs5,image = photoimage,compound = CENTER)
        self.mg5.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg5.place(x=490,y=190)

        self.mg6=Button(self.one,height = 110,width = 190,command=self.Mgs6,image = photoimage,compound = CENTER)
        self.mg6.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=1),bg="#DD969C",fg="#DD969C",borderwidth = 5)
        self.mg6.place(x=10,y=340)
        
        
        ##self.mg1.pack(expand=True)
        ##self.mg1.bind('<Enter>', self.Mgs1)
        ##self.mg1.bind('<Leave>', lambda e: e.widget.config(bg='white'))

       

        self.next=Button(self.one,text="NEXT",command=self.loqueSeaXD,height = 1,width = 7)
        self.next.place(x=530,y=390)
        self.next.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=20),bg="#5e00a3",fg="White",borderwidth = 5)


        self.one.mainloop()
        self.wind2.mainloop()
    
    def Mgs1(self):
        fontTextHis = tkFont.Font(family="Comic Sans MS", size=12, weight="bold",slant="italic",font=("Segoe Script", 18,'bold'))
        global xlide
        for xd in range(90,200,1):
            xlide=xd
            
            self.mg1.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg1.place(x=xd,y=35)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        #self.men1=Label(self.one,text="Un nuevo inicio",fg='black',bg="white").place(x=90,y=35)
        #self.men1.configure(font=fontTextHis)
        self.fontTextHis = tkFont.Font(family="Comic Sans MS", size=8, weight="bold",slant="italic",font=("Segoe Script", 10,'bold'))
        self.m1=Label(self.one,text="Un nuevo inicio",fg='black',bg="white",font=self.fontTextHis).place(x=91,y=35)
        self.one.update_idletasks()
        time.sleep(3)
        self.m1=Label(self.one,text="",fg='black',bg="black",font=self.fontTextHis).place(x=91,y=35)
        self.one.update_idletasks()
        for xd in range(200,90,-1):
            xlide=xd
            self.mg1.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg1.place(x=xd,y=35)
            #time.sleep(0.000000001)
            print(xd)
            m1=Label(self.one,text="",fg='black',bg="black",font=self.fontTextHis).place(x=91,y=35)
            self.one.update_idletasks()    

    def Mgs2(self):
        global xlide
        for xd in range(410,500,1):
            xlide=xd
            self.mg2.place(x=xd,y=35)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        time.sleep(3)

        for xd in range(500,410,-1):
            xlide=xd
            self.mg2.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg2.place(x=xd,y=35)
            #time.sleep(0.000000001)
            print(xd)
            self.one.update_idletasks()    
        

    def Mgs3(self):
        global xlide
        for xd in range(10,100,1):
            xlide=xd
            self.mg3.place(x=xd,y=190)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        time.sleep(3)

        for xd in range(100,10,-1):
            xlide=xd
            self.mg3.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg3.place(x=xd,y=190)
            #time.sleep(0.000000001)
            print(xd)
            self.one.update_idletasks()    

    def Mgs4(self):
        global xlide
        for xd in range(250,340,1):
            xlide=xd
            self.mg4.place(x=xd,y=190)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        time.sleep(3)

        for xd in range(340,250,-1):
            xlide=xd
            self.mg4.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg4.place(x=xd,y=190)
            #time.sleep(0.000000001)
            print(xd)
            self.one.update_idletasks()    
        

    def Mgs5(self):
        global xlide
        for xd in range(490,580,1):
            xlide=xd
            self.mg5.place(x=xd,y=190)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        time.sleep(3)

        for xd in range(580,490,-1):
            xlide=xd
            self.mg5.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg5.place(x=xd,y=190)
            #time.sleep(0.000000001)
            print(xd)
            self.one.update_idletasks()    

    def Mgs6(self):
        global xlide
        for xd in range(10,100,1):
            xlide=xd
            self.mg6.place(x=xd,y=340)
            
            

            print(xd)
            self.one.update_idletasks()
            time.sleep(0.0000001)
        ##self.wind2.update_idletasks()
            ##self.one.mainloop()
        time.sleep(3)

        for xd in range(100,10,-1):
            xlide=xd
            self.mg6.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=15),bg="#DD969C",fg="#DD969C",borderwidth = 5)
            self.mg6.place(x=xd,y=340)
            #time.sleep(0.000000001)
            print(xd)
            self.one.update_idletasks()    
        
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
        self.wind2.geometry(sizeW2)
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
        self.raiz.geometry(sizeMain)
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
        top.geometry(sizeW1) 

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