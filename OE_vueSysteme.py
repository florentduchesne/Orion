# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import math
from helper import Helper as hlp
from OE_vuePerspective import *




class VueSysteme(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planetes={}
        self.systeme=None
        self.maselection=None
        
        self.UA2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomiques       
        print("Diametre: ", self.modele.diametre)
        self.largeur=int(self.modele.diametre*self.UA2pixel)
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        self.labid.bind("<Button>",self.identifierplanetemere)
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau",command=self.creervaisseau)
        self.btncreervaisseau.pack()
        
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir planete",command=self.voirplanete)
        self.btnvuesysteme.pack(side=BOTTOM)
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir galaxie",command=self.voirgalaxie)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
        self.changecadreetat(self.cadreetataction)
    
    def voirplanete(self):
        self.parent.voirplanete(self.maselection)

    def voirgalaxie(self):
        self.parent.voirgalaxie()
            
    def initsysteme(self,i):
        self.systeme=i
        self.affichermodelestatique(i)
    
    def affichermodelestatique(self,i):
        xl=self.largeur/2
        yl=self.hauteur/2
        n=i.etoile.taille*self.UA2pixel/2
        mini=2
        UAmini=4
        self.minimap.config(bg="grey11")
        self.canevas.create_oval(xl-n,yl-n,xl+n,yl+n,fill="yellow",dash=(1,2),width=4,outline="white",
                                 tags=("systeme",i.id,"etoile",str(n),))
        self.minimap.create_oval(100-mini,100-mini,100+mini,100+mini,fill="yellow")
        for p in i.planetes:
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*self.UA2pixel,xl,yl)
            n=p.taille*self.UA2pixel

            if p.proprietaire == "inconnu":
                self.canevas.create_oval(x-n,y-n,x+n,y+n,fill=p.couleur,tags=(i.proprietaire,"planete",p.id,"inconnu", i.id,int(x),int(y)))
            else:
                self.canevas.create_oval(x-n,y-n,x+n,y+n,fill=p.couleur,tags=(i.proprietaire,"planete",p.id,p.proprietaire,i.id,int(x),int(y)))
              
            #self.canevas.create_oval(x-n,y-n,x+n,y+n,fill="red",tags=(i.proprietaire,"planete",p.id,"inconnu",i.id,int(x),int(y)))
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*UAmini,100,100)
            self.minimap.create_oval(x-mini,y-mini,x+mini,y+mini,fill="red",tags=())
        
        # NOTE Il y a un probleme ici je ne parviens pas a centrer l'objet convenablement comme dans la fonction 'identifierplanetemere'
        canl=int(self.canevas.cget("width"))/2
        canh=int(self.canevas.cget("height"))/2
        self.canevas.xview(MOVETO, ((self.largeur/2)-canl)/self.largeur)
        self.canevas.yview(MOVETO, ((self.hauteur/2)-canh)/self.hauteur)
    
    def identifierplanetemere(self,evt): 
        j=self.modele.joueurs[self.parent.nom]
        couleur=j.couleur
        x=j.systemeorigine.x*self.UA2pixel
        y=j.systemeorigine.y*self.UA2pixel
        id=j.systemeorigine.id
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                 tags=(self.parent.nom,"selecteur",id,""))
        xx=x/self.largeur
        yy=y/self.hauteur
        ee=self.canevas.winfo_width()
        ii=self.canevas.winfo_height()
        eex=int(ee)/self.largeur/2
        self.canevas.xview(MOVETO, xx-eex)
        eey=int(ii)/self.hauteur/2
        self.canevas.yview(MOVETO, yy-eey)
                   
    def creerimagefond(self): 
        pass  # on pourrait creer un fond particulier pour un systeme
    
    def afficherdecor(self):
        pass
                
    def creervaisseau(self): 
        if self.maselection:
            self.parent.parent.creervaisseau(self.maselection[5])
            self.maselection=None
            self.canevas.delete("selecteur")
        
    
    
    def creerstation(self):
        print("Creer station EN CONSTRUCTION")
         
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        e=self.UA2pixel
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            for j in i.vaisseauxinterstellaires:
                jx=j.y*100
                jy=j.x*100
                x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                self.canevas.create_line(x,y,x0,y0,fill="yellow",width=3,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                self.canevas.create_line(x0,y0,x1,y1,fill=i.couleur,width=4,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                self.canevas.create_line(x1,y1,x2,y2,fill="red",width=2,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                

            
    def changerproprietaire(self):
        pass
               
    def afficherselection(self):
        if self.maselection!=None:
            e=self.UA2pixel
            joueur=self.modele.joueurs[self.parent.nom]
            if self.maselection[1]=="planete":
                for i in self.systeme.planetes:
                    if i.id == self.maselection[2]:
                        x=int(self.maselection[3])
                        y=int(self.maselection[4])
                        t=20
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),
                                                outline=joueur.couleur,
                                                tags=("select","selecteur"))
            
                for i in joueur.vaisseauxinterstellaires:
                    if i.id == self.maselection[2]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_rectangle((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                    outline=joueur.couleur,
                                                    tags=("select","selecteur"))
      
    def cliquervue(self,evt):
        self.changecadreetat(None)
        
        t=self.canevas.gettags("current")
        if t and t[0]!="current":
            if t[1] == "planete":
                self.maselection=[self.parent.nom,t[1],t[2],t[5],t[6],t[4]]  # prop, type, id; self.canevas.find_withtag(CURRENT)#[0]
                print(t)
                self.montreplaneteselection()
                
            elif t[1]=="vaisseauinterstellaire":
                print("IN VAISSEAUINTERSTELLAIRE",t)
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montrevaisseauxselection()  
                
            # if self.maselection and self.maselection[1]=="vaisseauinterstellaire":
            #  print("IN systeme + select VAISSEAUINTERSTELLAIRE")
            #   self.parent.parent.ciblerdestination(self.maselection[2],t[2])
                
            # ici je veux envoyer un message comme quoi je visite cette planete
            # et me mettre en mode planete sur cette planete, d'une shot
            # ou est-ce que je fais selection seulement pour etre enteriner par un autre bouton
            
            #self.parent.parent.atterrirdestination(nom,idsysteme,idplanete)
        else:
            print("Region inconnue")
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
   
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadreetatmsg)
            
    def montreplaneteselection(self):
        self.changecadreetat(self.cadreetataction)
    
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
        