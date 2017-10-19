# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
from helper import Helper as hlp
from OE_vuePerspective import *
import OE_objetsBatiments

class VuePlanete(Perspective):
    def __init__(self,parent,syste,plane):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planete=plane
        self.systeme=syste
        self.infrastructures={}
        self.maselection=None
        self.macommande=None
        
        self.KM2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomique       
        self.largeur=int(self.modele.diametre*self.KM2pixel)
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="green")
        
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Mine",command=self.creermine)
        self.btncreervaisseau.pack()
        
        self.btncreertank=Button(self.cadreetataction,text="Creer Tank",command=self.creervehiculetank)
        self.btncreertank.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Manufacture",command=self.creermanufacture)
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir System",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.changecadreetat(self.cadreetataction)
    
    def creermine(self):
        self.macommande="mine"
        
    def creervehiculetank(self):
        self.macommande="vehiculetank"
        
    def creervehiculecommerce(self):
        self.macommande="vehiculecommerce"
        
    def creervehiculeavion(self):
        self.macommande="vehiculeavion"
    
    def creermanufacture(self):
        pass
    
    def voirsysteme(self):
        for i in self.modele.joueurs[self.parent.nom].systemesvisites:
            if i.id==self.systeme:
                self.parent.voirsysteme(i)
            
    def initplanete(self,sys,plane):
        s=None
        p=None
        for i in self.modele.joueurs[self.parent.nom].systemesvisites:
            if i.id==sys:
                s=i
                for j in i.planetes:
                    if j.id==plane:
                        p=j
                        break
        self.systemeid=sys
        self.planeteid=plane
        self.affichermodelestatique(s,p)
    
    def affichermodelestatique(self,s,p):
        self.chargeimages()
        xl=self.largeur/2
        yl=self.hauteur/2
        mini=2
        UAmini=4
        self.minimap.config(bg="green")
         #Dessin des tuiles de pelouse sur la surface de la map.
        for rows in p.tuiles:
            for t in rows:
                self.canevas.create_image(t.y,t.x,image=self.images[t.image], tags=(t.x,t.y,"tuile"))
        """
        x = 0
        y = 0
        for i in range(0,int((self.hauteur/50) +1)):
            for j in range(0,int((self.largeur /50)+1)):
                self.canevas.create_image(x,y,image=self.images["gazon"])   
                x+=50
            y+=50
            x=0
        """  
        scrollBarX = 0
        scrollBarY = 0
        #Dessin des infrastructues de la planete.
        for i in p.infrastructures:
            if isinstance(i, OE_objetsBatiments.Ville):
                scrollBarX = i.x
                scrollBarY = i.y
                self.canevas.create_image(i.x,i.y,image=self.images["ville"])               
                minix = (i.x *200) / self.largeur
                miniy = (i.y *200) / self.hauteur
                
                self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="grey11")
            
        #self.canevas.create_image(p.posXatterrissage,p.posYatterrissage,image=self.images["ville"])
        #Centre sur la ville principal.
        canl=int(scrollBarX-400)/self.largeur
        canh=int(scrollBarY-400)/self.hauteur
        
        self.canevas.xview(MOVETO,canl)
        self.canevas.yview(MOVETO, canh)
        
        #minix = (p.posXatterrissage *200) / self.largeur
        #miniy = (p.posYatterrissage *200) / self.hauteur
        #self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="grey11") 
    def chargeimages(self):
        im = Image.open("./images/ville_100.png")
        self.images["ville"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/mine_100.png")
        self.images["mine"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/gazon100x100.png")
        self.images["gazon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/eau100x100.png")
        self.images["eau"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/tankhaut.png")
        self.images["vehiculetank"] = ImageTk.PhotoImage(im)
        
		
    def afficherdecor(self):
        pass
                
    def creervaisseau(self):
        pass
    
    def creerstation(self):
        print("Creer station EN CONSTRUCTION")
         
    def afficherpartie(self,mod):
        pass
            
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        pass
      
    def cliquervue(self,evt):
        t=self.canevas.gettags("current")
        print("print t")
        print(t)
        if t and t[0]!="current":
            if t[0]==self.parent.nom:
                pass
            elif t[1]=="systeme":
                pass
            elif t[2]=="tuile":
                if self.macommande == "mine":
                    x=int(t[1])
                    y=int(t[0])
                    print('position de la mine x = {0}, y = {1}'.format(t[0],t[1]))
                    self.parent.parent.creermine(self.parent.nom,self.systemeid,self.planeteid,x,y)
                    minix = (x *200) / self.largeur
                    miniy = (y *200) / self.hauteur
                    self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="red")
                    self.macommande=None
                elif self.macommande == "vehiculetank":
                    x=self.canevas.canvasx(evt.x)
                    y=self.canevas.canvasy(evt.y)
                    self.parent.parent.creervehiculetank(self.parent.nom,self.systemeid,self.planeteid,x,y)
                    minix = (x *200) / self.largeur
                    miniy = (y *200) / self.hauteur
                    self.minimap.create_rectangle(minix-2,miniy-2,minix+2,miniy+2,fill="red")
                    self.macommande=None
                   
                elif self.macommande == "vehiculecommerce":
                    self.macommande=None
                    pass
                elif self.macommande == "vehiculeavion":
                    self.macommande=None
                    pass
            elif t[2] == "vehiculetank":
                pass
            
    def montresystemeselection(self):
        self.changecadreetat(self.cadreetataction)
        
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadreetatmsg)
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
    
    def cliquerminimap(self,evt):
        x=evt.x
        y=evt.y
        xn=self.largeur/int(self.minimap.winfo_width())
        yn=self.hauteur/int(self.minimap.winfo_height())
        
        ee=self.canevas.winfo_width()
        ii=self.canevas.winfo_height()
        eex=int(ee)/self.largeur/2
        eey=int(ii)/self.hauteur/2
        
        self.canevas.xview(MOVETO, (x*xn/self.largeur)-eex)
        self.canevas.yview(MOVETO, (y*yn/self.hauteur)-eey)
        
