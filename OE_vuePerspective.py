# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import tkinter.ttk as ttk

class Perspective(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent.cadrejeu)
        self.parent=parent
        self.modele=None
        self.cadreetatactif=None
        self.images={}
        self.couleurBG1 = "#222831"
        self.couleurBG2 = "#393E46"
        self.couleurBouton = "#0092ca"
        self.couleurBoutonDesactive = "#50a2c1"
        
        
        self.cadrevue=Frame(self,width=500,height=500, bg=self.couleurBG1) #500x500
        self.cadrevue.pack(side=LEFT,expand=1,fill=BOTH)
        
        self.cadreinfo=Frame(self,width=200,height=200,bg=self.couleurBG2)
        self.cadreinfo.pack(side=LEFT,fill=Y)
        self.cadreinfo.pack_propagate(0)
        
        
        self.cadreetat=Frame(self.cadreinfo,width=1400,height=600,bg=self.couleurBG1)
        self.cadreetat.pack()
        
        
        self.cadrevoyage=Frame(self.cadreetat,width=1400,height=600,bg=self.couleurBG2)
        
        #self.cadrevoyage.pack()
        
        self.scrollX=Scrollbar(self.cadrevue,orient=HORIZONTAL)
        self.scrollY=Scrollbar(self.cadrevue)
        
        
        
        self.canevas=Canvas(self.cadrevue,width=1400,height=800,bg=self.couleurBG1,
                             xscrollcommand=self.scrollX.set,
                             yscrollcommand=self.scrollY.set)
       
        
        self.canevas.bind("<Button>",self.cliquerGauche)
        self.canevas.bind("<Button-3>",self.cliquerDroite)
        self.canevas.bind("<Button-2>",self.cliquerCentre)
        self.canevas.bind("<B1-Motion>",self.maintenirGauche)
        self.scrollX.config(command=self.canevas.xview)
        self.scrollY.config(command=self.canevas.yview)
        self.canevas.grid(column=0,row=0,sticky=N+E+W+S)
        self.cadrevue.columnconfigure(0,weight=1)
        self.cadrevue.rowconfigure(0,weight=1)
        self.scrollX.grid(column=0,row=1,sticky=E+W)
        self.scrollY.grid(column=1,row=0,sticky=N+S)
        
        self.labid=Label(self.cadreinfo,text=self.parent.nom)
        self.labid.pack()
        
        ##############Changer Perspective###########
        self.cadrePerspective=Frame(self.cadreetat,width=200,height=200,bg=self.couleurBG2)
        self.btnvuegalaxie=Button(self.cadrePerspective,text="Voir galaxie", bg=self.couleurBoutonDesactive, state=DISABLED)#command=self.voirgalaxie
        self.btnvuegalaxie.pack()
        self.btnvuesysteme=Button(self.cadrePerspective,text="Voir systeme", bg=self.couleurBoutonDesactive, state=DISABLED)
        self.btnvuesysteme.pack()
        self.btnvueplanete=Button(self.cadrePerspective,text="Voir planete", bg=self.couleurBoutonDesactive, state=DISABLED)#command=self.voirplanete
        self.btnvueplanete.pack()
        self.cadrePerspective.pack(side=TOP)
        
        
        ##############Menu Principale##############
        self.cadreetataction=Frame(self.cadreetat,width=200,height=200,bg=self.couleurBG2)
        
        
        ##############Sous-menu##############
        self.cadreVaisseau=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        self.cadreBatiment=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        self.cadreManufacture=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        self.cadreInfrastructure=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        self.cadreVehicule=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        self.cadreDefense=Frame(self.cadreetat, width=200, height=200,bg =self.couleurBG2)
        
        self.cadreAmeliorationBatiments=Frame(self.cadreetat, width=200, height=200, bg=self.couleurBG2)##CADRE QUI NOUS PERMET D'AMELIORER LES BATIMENTS
        self.cadreAmeliorationVehicule=Frame(self.cadreetat, width=200, height=200, bg=self.couleurBG2)##CADRE QUI NOUS PERMET D'AMELIORER LES VÉHICULES
        
        self.cadreetatmsg=Frame(self.cadreetat,width=200,height=200,bg=self.couleurBG2)
        
        self.cadreminimap=Frame(self.cadreinfo,width=200,height=200,bg=self.couleurBG2)
        self.cadreminimap.pack(side=BOTTOM)
        self.minimap=Canvas(self.cadreminimap,width=200,height=200,bg=self.couleurBG2)
        self.minimap.bind("<Button>",self.cliquerminimap)
        self.minimap.pack()
        
        #Chat
        self.cadreChatEntete=Frame(self.cadreinfo,width=200,height=30,bg="DodgerBlue4")
        self.cadreChat=Frame(self.cadreinfo,width=200,height=200,bg="DodgerBlue4")
        self.labelChat=Label(self.cadreChatEntete,bg="SkyBlue1", text="Destinataire: ")
        self.comboboxListeChat=ttk.Combobox(self.cadreChatEntete)

        
        self.listeChat=Listbox(self.cadreChat, height=15, bg="SkyBlue1")
        self.listeChat.config(width=300)
        self.listeChat.yview()
        self.entryChat = Entry(self.cadreChat, width=30)
        self.entryChat.bind("<Return>", self.envoyeMessage)
        
        self.cadreChat.pack(side=BOTTOM)
        self.cadreChatEntete.pack(side=BOTTOM)
        self.labelChat.pack(side=LEFT)
        self.comboboxListeChat.pack(side=LEFT)
        self.listeChat.pack()
        self.entryChat.pack()
        
    def cliquervue(self,evt):
        pass
    
    def cliquervue2(self,evt):
        pass
    
    def cliquerGauche(self,evt):
        pass
    
    def cliquerDroite(self,evt):
        pass
    
    def cliquerminimap(self,evt):
        pass
    
    def cliquerCentre(self,evt):
        pass
    
    def maintenirGauche(self,evt):
        pass
    
    def changecadreetat(self,cadre):
        if self.cadreetatactif:
            self.cadreetatactif.pack_forget()
            self.cadreetatactif=None
        if cadre:
            self.cadreetatactif=cadre
            self.cadreetatactif.pack()
            
    def nouveauMessageChat(self, txt):
        if self.parent.nom == txt[0]:
            self.listeChat.insert(0, "*"+txt[1])
            self.modele.joueurs[self.parent.nom].listMessageChat.append("*"+txt[1])
        elif txt[0] == "Tous":
            self.listeChat.insert(0, txt[1])
            self.modele.joueurs[self.parent.nom].listMessageChat.append(txt[1])
            print(self.modele.joueurs[self.parent.nom].listMessageChat)
        
    def envoyeMessage(self, evt):
        txt=self.entryChat.get()
        aQui=self.comboboxListeChat.get()
        if txt:
            if aQui != "Tous":
                self.listeChat.insert(0, "To "+aQui+": "+txt)
                self.modele.joueurs[self.parent.nom].listMessageChat.append("To "+aQui+": "+txt)
            self.entryChat.delete(0, END)
            self.parent.parent.nouveauMessageChat([aQui,txt])
 
    def chatEcrireLesNomsDesJoueurs(self):
        h=0
        listeJoueur=["Tous"]
        for i in self.modele.joueurscles:
            h+=1
            listeJoueur.append(i)
        self.comboboxListeChat['values'] = listeJoueur
        self.comboboxListeChat.current(0)
        
    def remplirChatBoxChangementVue(self):
        if self.modele != None:
            if self.modele.joueurs[self.parent.nom] != None:
                for message in self.modele.joueurs[self.parent.nom].listMessageChat:
                    self.listeChat.insert(0, message)
         