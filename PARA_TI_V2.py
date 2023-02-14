#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################## MAIN 6Meses###################################

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import random
from zlib import Z_FIXED
from PIL import Image,ImageTk,ImageSequence
import time
import cv2
sizeMain='1024x720'
sizeW1='800x600'
sizeW2='700x500'

class Aplicacion():
    def __init__(self):
        self.top = Tk()
        self.top.geometry("380x500") 

        self.Bg4=PhotoImage(file="BackGrounds\Bg3.png",master=self.top)
        #self.Bg3 = self.Bg3.zoom(2)
        #self.Bg4 = self.Bg4.subsample(1)
        self.BG4=Label(self.top,image=self.Bg4)

        self.BG4.place(x=-5,y=-5)

        self.top.title("¡SI!")
        #l2 = Label(top, text = "Sabia que dirias que si mi princesa ( <3 ) TE QUIERO ∞", font =('Brush Script MT', 17, 'bold'))
        #l2.pack()
        bsalir2 = Button(self.top, text='CONTINUAR', command=self.F1)
        bsalir2.configure(font=("Segoe Script", 20, 'bold','italic'),height = 1,width = 25,bg="#7A00D3",fg="White",borderwidth = 3) 
        bsalir2.pack(side=BOTTOM)


        self.image = PhotoImage(file='BackGrounds/1.png')
        self.image = self.image.subsample(6, 6)
        self.canvas = Canvas(self.top, width=270, height=250,background="#DD969C")
        
        self.canvas.create_image(130,120, image=self.image)
        self.canvas.place(x=60,y=150)
        #self.canvas.move(self.image_id, 245, 100)

        self.top.mainloop()

    def F1(self):
       
        imagen1 = cv2.imread('BackGrounds/F1.jpg')
        imagen1 = cv2.resize(imagen1, (300,250))
        imagen2 = cv2.imread('BackGrounds/F2.jpg')
        imagen2 = cv2.resize(imagen2, (300,250))
        imagen3 = cv2.imread('BackGrounds/F3.jpg')
        imagen3 = cv2.resize(imagen3, (300,250))
        imagen4 = cv2.imread('BackGrounds/muah.jpg')
        imagen4 = cv2.resize(imagen4, (300,250))

        concat_horizontal = cv2.hconcat([imagen1,imagen2,imagen3,imagen4])
        cv2.imshow('Mi princesa',concat_horizontal)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.meses()
    def F2(self):
        imagen=cv2.imread('BackGrounds/FelizSanvalentin.png')
        cv2.imshow('FELIZ DIA DE SAN VALENTÍN',imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.one.destroy()
        self.top.destroy()
    def meses(self):
        global xlide
        self.one = Toplevel()
        self.one.geometry(sizeW2)
        self.one.configure(background ='#DD969C')

        self.Bg1=PhotoImage(file="BackGrounds\Bg1.png")
        self.BG=Label(self.one,image=self.Bg1)
        self.BG.place(x=-2,y=-2)

        style1 = ttk.Style()
        style1.configure('W.TButton', font =('calibri', 15, 'bold'),foreground = 'red')
        
        self.one.resizable(width=False,height=False)
        self.one.title("MI PRINCESA")
        self.one.configure(background ='#DD969C')
        self.BgMeses=PhotoImage(file="BackGrounds\Mgs.png")
        photo = PhotoImage(file = r"BackGrounds\Mgs.png")
        photoimage = photo.subsample(2, 3)
        #elf.fontTextHis = tkFont.Font(family="Comic Sans MS", size=8, weight="bold",slant="italic",font=("Segoe Script", 10,'bold'))
        #self.m1=Label(self.one,text="",fg='black',bg="black",font=self.fontTextHis).place(x=91,y=35)
        photom1 = PhotoImage(file = r"BackGrounds\m1.png")
        photoX1 = photom1.subsample(3, 4)
        #mg1x=Label(self.one,height = 120,width = 110,image = photoX1,compound = CENTER, background="#DD969C")
        self.fontTextMeses = tkFont.Font(family="Comic Sans MS", size=15, weight="normal",slant="roman",font=("Brush Script MT", 22,'bold'),compound=CENTER)
        mg1x=Label(self.one,text="Nuestras\nvidas\nse unieron",fg='white',bg="#DD969C",font=self.fontTextMeses,compound=CENTER)
        mg1x.place(x=90,y=35)

        self.fontTextMeses2 = tkFont.Font(family="Comic Sans MS", size=15, weight="normal",slant="roman",font=("Brush Script MT", 22,'bold'),compound=CENTER)
        mg2x=Label(self.one,text="La vida\nme mostró\nuna angelita",fg='white',bg="#DD969C",font=self.fontTextMeses2,compound=CENTER)
        mg2x.place(x=410,y=35)

        self.fontTextMeses3 = tkFont.Font(family="Comic Sans MS", size=15, weight="normal",slant="roman",font=("Brush Script MT", 18,'bold'),compound=CENTER)
        mg3x=Label(self.one,text="El amor\nentró\nen mi\ncorazón",fg='white',bg="#DD969C",font=self.fontTextMeses3,compound=CENTER)
        mg3x.place(x=10,y=190)

        self.fontTextMeses4 = tkFont.Font(family="Comic Sans MS", size=15, weight="normal",slant="roman",font=("Brush Script MT", 22,'bold'),compound=CENTER)
        mg4x=Label(self.one,text="Cada día\nte amaba más\ny más",fg='white',bg="#DD969C",font=self.fontTextMeses4,compound=CENTER)
        mg4x.place(x=250,y=190)

        self.fontTextMeses5 = tkFont.Font(family="Comic Sans MS", size=16, weight="normal",slant="roman",font=("Brush Script MT", 17,'bold'),compound=CENTER)
        mg5x=Label(self.one,text="Comprendí que\nno hay mejor lugar que\nestar a tu ladito",fg='white',bg="#DD969C",font=self.fontTextMeses5,compound=CENTER)
        mg5x.place(x=490,y=190)

        self.fontTextMeses6 = tkFont.Font(family="Comic Sans MS", size=15, weight="normal",slant="roman",font=("Brush Script MT", 24,'bold'),compound=CENTER)
        mg6x=Label(self.one,text="Eres los mejor\nque me ha pasado\nen la vida",fg='white',bg="#DD969C",font=self.fontTextMeses6,compound=CENTER)
        mg6x.place(x=10,y=340)

        self.mg1=Button(self.one,height = 110,width = 190,command=self.Mgs1,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg1.place(x=90,y=35)
        
        self.mg2=Button(self.one,height = 110,width = 190,command=self.Mgs2,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg2.place(x=410,y=35)

        self.mg3=Button(self.one,height = 110,width = 190,command=self.Mgs3,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg3.place(x=10,y=190)
        
        self.mg4=Button(self.one,height = 110,width = 190,command=self.Mgs4,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg4.place(x=250,y=190)

        self.mg5=Button(self.one,height = 110,width = 190,command=self.Mgs5,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg5.place(x=490,y=190)

        self.mg6=Button(self.one,height = 110,width = 190,command=self.Mgs6,image = photoimage,compound = CENTER,background="#DD969C",borderwidth = 5)
        self.mg6.place(x=10,y=340)
        
      
        self.next=Button(self.one,text="NEXT",height = 1,width = 7, command=self.F2)
        self.next.place(x=530,y=390)
        self.next.configure(font=tkFont.Font(family="Segoe Script",slant="italic",weight="bold",size=20),bg="#5e00a3",fg="White",borderwidth = 5)
        self.one.update()
        self.one.mainloop()
        #self.wind2.mainloop()

    def Mgs1(self):
        for xd in range(90,200,2):
            self.mg1.place(x=xd,y=35)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)
        self.one.update_idletasks()
        for xd in range(200,90,-2):
            self.mg1.place(x=xd,y=35)
            self.one.update_idletasks()
            self.one.update()


    def Mgs2(self):
        for xd in range(410,550,2):
            self.mg2.place(x=xd,y=35)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)
        self.one.update_idletasks()
        for xd in range(550,410,-2):
            self.mg2.place(x=xd,y=35)
            self.one.update_idletasks()
            self.one.update()
        

    def Mgs3(self):
        for xd in range(10,100,2):
            self.mg3.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)
        for xd in range(100,10,-2):
            self.mg3.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()
            

    def Mgs4(self):
        
        for xd in range(250,405,2):
            self.mg4.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)
          

        for xd in range(405,250,-2):
            self.mg4.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()
         
            
        

    def Mgs5(self):
        for xd in range(490,690,2):
            self.mg5.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)

        for xd in range(690,490,-2):
            self.mg5.place(x=xd,y=190)
            self.one.update_idletasks()
            self.one.update()

    def Mgs6(self):
        for xd in range(10,230,2):
            self.mg6.place(x=xd,y=340)
            self.one.update_idletasks()
            self.one.update()
            time.sleep(0.00000001)
        self.one.update_idletasks()
        time.sleep(3)


        for xd in range(230,10,-2):
            self.mg6.place(x=xd,y=340)
            self.one.update_idletasks()
            self.one.update()
        

    #def MedijoQueSI(self):
        


def main():
    mi_app = Aplicacion()

    return 0
if __name__ == '__main__':
    main()
