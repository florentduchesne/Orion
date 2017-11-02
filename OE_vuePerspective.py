# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk

class Perspective(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent.cadrejeu)
        self.parent=parent
        self.modele=None
        self.cadreetatactif=None
        self.images={}
        
        self.cadrevue=Frame(self,width=500,height=500, bg="lightgreen") #500x500
        self.cadrevue.pack(side=LEFT,expand=1,fill=BOTH)
        
        self.cadreinfo=Frame(self,width=200,height=200,bg="darkgrey")
        self.cadreinfo.pack(side=LEFT,fill=Y)
        self.cadreinfo.pack_propagate(0)
        
        self.cadreetat=Frame(self.cadreinfo,width=1400,height=600,bg="grey20")
        self.cadreetat.pack()
        
        self.cadrevoyage=Frame(self.cadreetat,width=1400,height=600,bg="grey20")
        #self.cadrevoyage.pack()
        
        self.scrollX=Scrollbar(self.cadrevue,orient=HORIZONTAL)
        self.scrollY=Scrollbar(self.cadrevue)
        self.canevas=Canvas(self.cadrevue,width=1400,height=800,bg="grey11",
                             xscrollcommand=self.scrollX.set,
                             yscrollcommand=self.scrollY.set)
        
        self.canevas.bind("<Button>",self.cliquervue)
        self.canevas.bind("<Button-3>",self.cliquervue2)
        self.scrollX.config(command=self.canevas.xview)
        self.scrollY.config(command=self.canevas.yview)
        self.canevas.grid(column=0,row=0,sticky=N+E+W+S)
        self.cadrevue.columnconfigure(0,weight=1)
        self.cadrevue.rowconfigure(0,weight=1)
        self.scrollX.grid(column=0,row=1,sticky=E+W)
        self.scrollY.grid(column=1,row=0,sticky=N+S)
        
        self.labid=Label(self.cadreinfo,text=self.parent.nom)
        self.labid.pack()
        
        ##############Menu Principale##############
        self.cadreetataction=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        ##############Sous-menu##############
        self.cadreVaisseau=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        self.cadreBatiment=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        self.cadreManufacture=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        self.cadreInfrastructure=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        self.cadreVehicule=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        self.cadreDefense=Frame(self.cadreetat, width=200, height=200,bg ="grey20")
        
        self.cadreAmeliorationBatiments=Frame(self.cadreetat, width=200, height=200, bg="grey20")##CADRE QUI NOUS PERMET D'AMELIORER LES BATIMENTS
        
        self.cadreetatmsg=Frame(self.cadreetat,width=200,height=200,bg="grey20")
        
        self.cadreminimap=Frame(self.cadreinfo,width=200,height=200,bg="grey20")
        self.cadreminimap.pack(side=BOTTOM)
        self.minimap=Canvas(self.cadreminimap,width=200,height=200,bg="grey11")
        self.minimap.bind("<Button>",self.cliquerminimap)
        self.minimap.pack()
        
    def cliquervue(self,evt):
        pass
    
    def cliquervue2(self,evt):
        pass
    
    def cliquerminimap(self,evt):
        pass
    
    def changecadreetat(self,cadre):
        if self.cadreetatactif:
            self.cadreetatactif.pack_forget()
            self.cadreetatactif=None
        if cadre:
            self.cadreetatactif=cadre
            self.cadreetatactif.pack()
 
        
         