# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import random
from helper import Helper as hlp
from OE_vuePerspective import Perspective
from OE_objetsVaisseaux import Vaisseau



class VueGalaxie(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.maselection=None
        self.mesSelections=[]
        self.commande = None
        
        self.couleurBG1 = "#222831"
        self.couleurBG2 = "#393E46"
        self.couleurBouton = "#0092ca"
        self.couleurBoutonDesactive = "#50a2c1"
        
        
        self.AL2pixel=100
        print("Diametre: ", self.modele.diametre)
        self.largeur=int(self.modele.diametre*self.AL2pixel)
        self.hauteur=self.largeur
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        #############################
  
        self.btnvuesysteme.configure(bg=self.couleurBoutonDesactive, command=self.voirsysteme, state=DISABLED)
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
        
        
        self.btnVoyage=Button(self.cadrevoyage,text ="Voyage dans systeme", bg=self.couleurBouton,command =self.voyageSystem)
        self.btnVoyage.pack()
    
    
    def voirsysteme(self,systeme=None):
        if systeme==None:
            if self.maselection and self.maselection[0]==self.parent.nom and self.maselection[1]=="systeme":
                sid=self.maselection[2]
                # for i in self.modele.joueurs[self.parent.nom].systemesvisites:
                for i in self.modele.systemes:
                    if i.id==sid:
                        s=i
                        print(s.planetes)
                        break
                
                self.btnvuesysteme.configure(bg=self.couleurBoutonDesactive, command=self.voirsysteme, state=DISABLED)
                self.parent.parent.visitersysteme(sid)
                self.parent.voirsysteme(s) #normalement devrait pas planter
        else:                
            sid=systeme.id
            for i in self.modele.joueurs[self.parent.nom].systemesvisites:
                if i.id==sid:
                    s=i
                    break
            # NOTE passer par le serveur est-il requis ????????????
            self.parent.parent.visitersysteme(sid)
            self.parent.voirsysteme(s) #normalement devrait pas planter
            
    def chargeimages(self):
       # im = Image.open("./images/chasseurhautgauche.png")
        #self.images["chasseur"] = ImageTk.PhotoImage(im)
        pass
        
    def afficherdecor(self):
        self.creerimagefond()
        self.affichermodelestatique()

    def creerimagefond(self): #NOTE - au lieu de la creer a chaque fois on aurait pu utiliser une meme image de fond cree avec PIL
        imgfondpil = Image.new("RGBA", (self.largeur,self.hauteur),"black")
        draw = ImageDraw.Draw(imgfondpil) 
        for i in range(self.largeur*2):
            x=random.randrange(self.largeur)
            y=random.randrange(self.hauteur)
            #draw.ellipse((x,y,x+1,y+1), fill="white")
            draw.ellipse((x,y,x+0.1,y+0.11), fill="white")
        self.images["fond"] = ImageTk.PhotoImage(imgfondpil)
        self.canevas.create_image(self.largeur/2,self.hauteur/2,image=self.images["fond"])
            
    def affichermodelestatique(self): 
        mini=self.largeur/200
        e=self.AL2pixel
        me=200/self.modele.diametre
        for i in self.modele.systemes:
            t=i.etoile.taille*3
            if t<3:
                t=3
            self.canevas.create_oval((i.x*e)-t,(i.y*e)-t,(i.x*e)+t,(i.y*e)+t,fill="grey80",
                                     tags=("inconnu","systeme",i.id,str(i.x),str(i.y)))
            # NOTE pour voir les id des objets systeme, decommentez la ligne suivantes
            #self.canevas.create_text((i.x*e)-t,(i.y*e)-(t*2),text=str(i.id),fill="white")
            
        for i in self.modele.joueurscles:
            couleur=self.modele.joueurs[i].couleur
            m=2
            for j in self.modele.joueurs[i].systemesvisites:
                s=self.canevas.find_withtag(j.id)
                self.canevas.addtag_withtag(i, s)
                self.canevas.itemconfig(s,fill=couleur)
                self.minimap.config(bg="grey11")
                self.minimap.create_oval((j.x*me)-m,(j.y*me)-m,(j.x*me)+m,(j.y*me)+m,fill=couleur)
                
    # ************************ FIN DE LA SECTION D'AMORCE DE LA PARTIE
                
    def identifierplanetemere(self,evt): 
        j=self.modele.joueurs[self.parent.nom]
        couleur=j.couleur
        x=j.systemeorigine.x*self.AL2pixel
        y=j.systemeorigine.y*self.AL2pixel
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

        
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.canevas.delete("pulsar")
        self.afficherselection()
        
        e=self.AL2pixel
        for i in mod.pulsars:
            t=i.taille
            self.canevas.create_oval((i.x*e)-t,(i.y*e)-t,(i.x*e)+t,(i.y*e)+t,fill="orchid3",dash=(1,1),
                                                 outline="maroon1",width=2,
                                     tags=("inconnu","pulsar",i.id))
            
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            for j in i.objetgalaxie:
                
                if (isinstance(j, Vaisseau)):
                    jx=j.x*e
                    jy=j.y*e
                    x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                    x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                    x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                    x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                    self.canevas.create_line(x,y,x0,y0,fill="yellow",width=3,
                                             tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",))
                    self.canevas.create_line(x0,y0,x1,y1,fill=i.couleur,width=4,
                                             tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y))
                    self.canevas.create_line(x1,y1,x2,y2,fill="red",width=2,
                                             tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
        
    def changerproprietaire(self,prop,couleur,systeme):
        #lp=self.canevas.find_withtag(systeme.id) 
        self.canevas.addtag_withtag(prop,systeme.id)
        
    def changerproprietaire1(self,prop,couleur,systeme): 
        id=str(systeme.id)
        lp=self.canevas.find_withtag(id)
        self.canevas.itemconfig(lp[0],fill=couleur)
        t=(prop,"systeme",id,"systemevisite",str(len(systeme.planetes)),systeme.etoile.type)
        self.canevas.itemconfig(lp[0],tags=t)
               
    def afficherselection(self):
        self.canevas.delete("selecteur")
        if self.maselection!=None:
            joueur=self.modele.joueurs[self.parent.nom]
            
            e=self.AL2pixel
            if self.maselection[1]=="systeme":
                for i in joueur.systemesvisites:
                    if i.id == self.maselection[2]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_oval((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                 outline=joueur.couleur,
                                                 tags=("select","selecteur"))
            elif self.maselection[1]=="vaisseauinterstellaire":
                for i in joueur.vaisseauxinterstellaires:
                    if i.id == self.maselection[2]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_rectangle((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                      outline=joueur.couleur,
                                                      tags=("select","selecteur"))
      
    def cliquer(self,evt):
        self.changecadreetat(None)
        t=self.canevas.gettags("current")
        self.btnvuesysteme.configure(bg=self.couleurBoutonDesactive, command=self.voirsysteme, state=DISABLED)
        if t and t[0]!="current":    
            if t[1]=="vaisseauinterstellaire":
                print("IN VAISSEAUINTERSTELLAIRE",t)
                self.maselection=[self.parent.nom,t[1],t[2]]
                self.montrevaisseauxselection()
            
            elif t[1]=="systeme":
                self.btnvuesysteme.configure(bg=self.couleurBouton, command=self.voirsysteme, state=NORMAL)
                print("IN SYSTEME",t)
                if self.maselection and self.maselection[1]=="vaisseauinterstellaire":
                    print("IN systeme + select VAISSEAUINTERSTELLAIRE")
                    if self.commande=="voyageSystem":
                        election=None
                        self.lbselectecible.pack_forget()
                        self.canevas.delete("selecteur")
                else:
                    print("IN systeme  PAS SELECTION")
                    self.maselection=[self.parent.nom,t[1],t[2]]
                    self.montresystemeselection()

            else:
                print("Objet inconnu")
        else:
            print("Region inconnue")
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
    
    def cliquerGauche(self,evt):
        self.canevas.delete("selectionner")  
        self.btnvuesysteme.configure(bg=self.couleurBoutonDesactive, command=self.voirsysteme, state=DISABLED) 
        self.maselection = None
        self.mesSelections.clear()        
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        self.initX = x
        self.initY = y
        xy2=evt.x,evt.y
        t=self.canevas.gettags("current")
        #liste de tuples 1: le type de la selection(systeme, vaisseau), 2: le id de la selection
        if len(t) != 0:
            if t[0] != "current":
                if t[1] == "systeme":
                    self.btnvuesysteme.configure(bg=self.couleurBouton, command=self.voirsysteme, state=NORMAL)
                    self.maselection=[self.parent.nom,t[1],t[2],t[3],t[4]]
                    print(self.maselection)
                    self.montresystemeselection()
                elif t[1] == "vaisseauinterstellaire":
                    self.mesSelections.append((self.parent.nom,t[1],t[2]))
                    self.montrevaisseauxselection()
                    print(self.mesSelections)
            
    def cliquerDroite(self, evt):
        t=self.canevas.gettags("current")
        self.canevas.delete("selectionner")  
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        xy=(x/100,y/100) 
        xy2=evt.x,evt.y       
        if len(self.mesSelections) != 0:
            for v in self.mesSelections:
                print(v)
                xy = (xy[0],xy[1])
                if len(t) != 0:
                    if t[0] != "current": 
                        if t[1] == "systeme":
                            systeme=[self.parent.nom,t[1],t[2],t[3],t[4]]
                            self.parent.parent.ciblerdestination(v[2],systeme[2],None,xy)
                        elif t[1] == "vaisseauinterstellaire":
                            vaisseau=[self.parent.nom,t[1],t[2],xy2]
                            print(vaisseau)
                            print(v)
                            self.parent.parent.ciblerdestination(v[2],vaisseau[2],None,xy)
                else:
                    self.parent.parent.ciblerEspace(v[2],self.systeme.id,xy)
            
    def cliquerCentre(self, evt):
        joueur=self.modele.joueurs[self.parent.nom]
        xy2=evt.x,evt.y
        t=self.canevas.gettags("current")
        if len(t) != 0:
            if t[0] != "current":
                if t[1] == "systeme":
                    self.maselection=[self.parent.nom,t[1],t[2],t[3],t[4]]  
                    if len(self.mesSelections) != 0:            
                        if self.commande=="voyageSystem":                            
                            for v in self.mesSelections:      
                                for jv in joueur.vaisseauxinterstellaires:
                                    if jv.id == v[2]:
                                        print("Clique Centre Vaisseau")
                                        print("Selection" + str(self.maselection))
                                        print("MesSelections" + str(v))
                                        jv.dansGalaxie = False
                                        jv.cible =None
                                        self.parent.parent.voyageSystem(self.maselection[2],v[2])
                                        self.lbselectecible.pack_forget()
                                        self.canevas.delete("selecteur")
                
    
    def montresystemeselection(self):
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
        
        
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadrevoyage)
    
    def voyageSystem(self):
        self.commande="voyageSystem"
       # self.parent.parent.voyageSystem(self.maselection[0],self.maselection[2])