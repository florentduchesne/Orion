# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import random
from helper import Helper as hlp
from OE_vuePerspective import Perspective
from OE_objetsVaisseaux import VaisseauMere
import math



class VueGalaxie(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.maselection=None
        self.mesSelections=[]
        self.commande = None
        self.chatEcrireLesNomsDesJoueurs()

        self.initX = 0
        self.initY = 0
        self.couleurBG1 = "#222831"
        self.couleurBG2 = "#393E46"
        self.couleurBouton = "#0092ca"
        self.couleurBoutonDesactive = "#50a2c1"
        
        self.labid.config(bg=self.modele.joueurs[self.parent.parent.monnom].couleur, foreground="black")
        
        self.AL2pixel=self.modele.diametre*2
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
        for x in range(0,361):
            im = Image.open("./images/vaisseauMereGalaxie.png")
            self.images[("mere"+str(x))] = ImageTk.PhotoImage(im.rotate(-x))    
        
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
        self.minimap.delete("meremini")
        self.afficherselection()        
        e=self.AL2pixel
        for i in mod.pulsars:
            t=i.taille
            self.canevas.create_oval((i.x*e)-t,(i.y*e)-t,(i.x*e)+t,(i.y*e)+t,fill="orchid3",dash=(1,1),
                                                 outline="maroon1",width=2,
                                     tags=("inconnu","pulsar",i.id))
            
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            if i.nouveauMessageChatTxt != None:
                self.nouveauMessageChat(i.nouveauMessageChatTxt)
                i.nouveauMessageChatTxt = None
            for j in i.objetgalaxie:
                if isinstance(j, VaisseauMere):
                    jx=j.x*e
                    jy=j.y*e
                    x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                    x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                    x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                    x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                    angle = int(math.degrees(j.angleinverse))                    
                    tag =("mere"+str(angle))
                    im=self.parent.modes["galaxie"].images[tag]
                    self.parent.modes["galaxie"].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"mere") )
                    minix = (x *200) / self.largeur 
                    miniy = (y *200) / self.largeur 
                    self.parent.modes["galaxie"].minimap.create_rectangle(minix-2, miniy-2, minix+2, miniy+2, fill = i.couleur, tags=("meremini"))
        
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
        e=self.AL2pixel
        joueur=self.modele.joueurs[self.parent.nom]
        self.canevas.delete("selecteur")
        if self.maselection!=None:
            if self.maselection[1]=="systeme":
                x=float(self.maselection[3])
                y=float(self.maselection[4])
                t=12
                self.canevas.create_oval((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                         outline=joueur.couleur,
                                         tags=("select","selecteur"))                   
        if len(self.mesSelections)!=0:
            for v in self.mesSelections:                    
                for i in joueur.vaisseauxinterstellaires:
                    if i.id == v[2]:
                        x=i.x
                        y=i.y
                        t=25
                        if(x != None and y != None) :
                            self.canevas.create_rectangle((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                        outline=joueur.couleur,
                                                        tags=("select","selecteur"))
            
    def maintenirGauche(self, evt):
        joueur=self.modele.joueurs[self.parent.nom]
        self.mesSelections.clear() 
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)                 
        self.canevas.delete("selectionner")       
        self.canevas.create_rectangle(self.initX,self.initY,x,y,dash=(2,2),outline=joueur.couleur,tags=("selectionner"))
        pluspetitx = hlp.valeurminimal(self.initX,x)
        plusgrandx = hlp.valeurmaximal(self.initX,x)
        pluspetity = hlp.valeurminimal(self.initY,y)
        plusgrandy = hlp.valeurmaximal(self.initY,y)
        for vj in joueur.vaisseauxinterstellaires:
                if(vj.dansGalaxie):
                    vaisseauX = vj.x*self.AL2pixel
                    vaisseauY = vj.y*self.AL2pixel
                    if vaisseauX >= pluspetitx and vaisseauX <= plusgrandx and vaisseauY >= pluspetity and vaisseauY <= plusgrandy:                    
                        self.mesSelections.append((self.parent.nom,"vaisseauinterstellaire",vj.id))
        if len(self.mesSelections)!= 0:
            self.montrevaisseauxselection()

    
    def cliquerGauche(self,evt):
        joueur=self.modele.joueurs[self.parent.nom]
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
                    self.montresystemeselection()
                elif t[1] == "vaisseauinterstellaire":
                    self.mesSelections.append((self.parent.nom,t[1],t[2]))
                    self.montrevaisseauxselection()                  
                
            
    def cliquerDroite(self, evt):
        t=self.canevas.gettags("current")
        self.canevas.delete("selectionner")  
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        xy=(x/self.AL2pixel,y/self.AL2pixel) 
        xy2=evt.x,evt.y       
        if len(self.mesSelections) != 0:
            for v in self.mesSelections:
                xy = (xy[0],xy[1])
                if len(t) != 0:
                    if t[0] != "current": 
                        if t[1] == "systeme":
                            systeme=[self.parent.nom,t[1],t[2],t[3],t[4]]
                            self.parent.parent.ciblerdestination(v[2],systeme[2],None,xy)
                        elif t[1] == "vaisseauinterstellaire":
                            vaisseau=[self.parent.nom,t[1],t[2],xy2]
                            self.parent.parent.ciblerdestination(v[2],vaisseau[2],None,xy)
                    else:
                        self.parent.parent.ciblerEspace(v[2],0,xy) # Le 0 represente le id su systeme mais dans le code CiblerEspace on n'utilise pas le param
        
        
            
    def cliquerCentre(self, evt):
        joueur=self.modele.joueurs[self.parent.nom]
        self.canevas.delete("selectionner") 
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
        #self.parent.parent.voyageSystem(self.maselection[0],self.maselection[2])
       