# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import math
from helper import Helper as hlp
from OE_vuePerspective import *
from OE_objetsVaisseaux import VaisseauChaseur, VaisseauColonisation


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
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau",command=self.AfficherChoixVaisseau)
        self.btncreervaisseau.pack()
        
        ##############Base##############
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        self.btncreerstation.pack()
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir planete",command=self.voirplanete)
        self.btnvuesysteme.pack(side=BOTTOM)
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir galaxie",command=self.voirgalaxie)
        self.btnvuesysteme.pack(side=BOTTOM)
        
        ##############Vaisseaux##############
        self.btnChasseur=Button(self.cadreVaisseau,text="Vaisseau Chasseur",command = lambda : self.creervaisseau("chasseur"))
        self.btnChasseur.pack(side=TOP)
        self.btnCommerce=Button(self.cadreVaisseau,text="Vaisseau Commerce",command = self.creervaisseau2("commerce"))
        self.btnCommerce.pack(side=TOP)
        self.btnBombarde=Button(self.cadreVaisseau,text="Vaisseau Bombarde",command = self.creervaisseau2("bombarde"))
        self.btnBombarde.pack(side=TOP)
        self.btnColonisation=Button(self.cadreVaisseau,text="Vaisseau Colonisation",command = lambda : self.creervaisseau("colonisateur"))
        self.btnColonisation.pack(side=TOP)
        self.btnTank=Button(self.cadreVaisseau,text="Vaisseau Tank",command = self.creervaisseau2("tank"))
        self.btnTank.pack(side=TOP)
        self.btnMere=Button(self.cadreVaisseau,text="Vaisseau Mere",command = self.creervaisseau2("mere"))
        self.btnMere.pack(side=TOP)
        self.btnLaser=Button(self.cadreVaisseau,text="Vaisseau Laser",command = self.creervaisseau2("laser"))
        self.btnLaser.pack(side=TOP)
        self.btnNova=Button(self.cadreVaisseau,text="Vaisseau Nova",command = self.creervaisseau2("nova"))
        self.btnNova.pack(side=TOP)
        self.btnSuicide=Button(self.cadreVaisseau,text="Vaisseau Suicide",command = self.creervaisseau2("suicide"))
        self.btnSuicide.pack(side=TOP)
        self.btnBiologique=Button(self.cadreVaisseau,text="Vaisseau Biologique",command = self.creervaisseau2("biologique"))
        self.btnBiologique.pack(side=TOP)
        self.btnRetour=Button(self.cadreVaisseau,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
        
        #voyage
        self.btnVoyage=Button(self.cadrevoyage,text ="Voyage dans galaxie",bg="darkgray",command =self.voyageGalax)
        self.btnVoyage.pack()
        
        self.changecadreetat(self.cadreetataction)
        
    def voirplanete(self):
        self.parent.voirplanete(self.maselection)

    def voirgalaxie(self):
        self.parent.voirgalaxie()
    
    def AfficherChoixVaisseau(self):
        self.changecadreetat(self.cadreVaisseau)
        
    def Retour(self):
        self.changecadreetat(self.cadreetataction)
    
    def initsysteme(self,i):
        self.systeme=i
        self.affichermodelestatique(i)
    
    def affichermodelestatique(self,i):
        self.chargeimages()
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
                self.canevas.create_oval(x-n,y-n,x+n,y+n,fill=p.couleur,tags=(i.proprietaire,"planete",p.id,"inconnu", i.id,x,y))
            else:
                self.canevas.create_oval(x-n,y-n,x+n,y+n,fill=p.couleur,tags=(i.proprietaire,"planete",p.id,p.proprietaire,i.id,int(x),int(y)))
              
            #self.canevas.create_oval(x-n,y-n,x+n,y+n,fill="red",tags=(i.proprietaire,"planete",p.id,"inconnu",i.id,int(x),int(y)))
            x,y=hlp.getAngledPoint(math.radians(p.angle),p.distance*UAmini,100,100)
            self.minimap.create_oval(x-mini,y-mini,x+mini,y+mini,fill=p.couleur,tags=())
        
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
                
    def creervaisseau(self,typeVaisseau):#typeVaisseau):
        if self.maselection:
            self.parent.parent.creervaisseau(self.maselection[5],self.maselection[2],typeVaisseau)#5 = id sys 3 = id planete
            self.maselection=None
            self.canevas.delete("selecteur")
     
    def creervaisseau2(self,typeVaisseau):
        print ("2")
    
    def creerstation(self):
        if self.maselection:
            print(self.systeme.id)  
            self.parent.parent.creerstationspatiale(self.maselection[5],self.maselection[2])
            self.maselection=None
            self.canevas.delete("selecteur")
    
    def chargeimages(self):
        im = Image.open("./images/chasseur.png")
        self.images["chasseur"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/colonisateur.png")
        self.images["colonisateur"] = ImageTk.PhotoImage(im)   

    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.canevas.delete("selecteur")
        self.canevas.delete("projectile")
        self.afficherselection()
        e=self.UA2pixel
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            for j in i.vaisseauxinterstellaires:
                if j.idSysteme==self.systeme.id:
                    if j.dansGalaxie==False:
                        jx=j.x*e
                        jy=j.y*e
                        x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                        x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                        x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                        x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                        if isinstance(j,VaisseauChaseur):
                            im=self.parent.modes["systemes"][j.idSysteme].images["chasseur"]
                            self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"chasseur") )
                        if isinstance(j,VaisseauColonisation) :
                            im=self.parent.modes["systemes"][j.idSysteme].images["colonisateur"]
                            self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"colonisateur") )  
                            
                        if j.projectile!=None:
                            for pro in j.projectile:
                                x=pro.x*e
                                y=pro.y*e
                                taille = pro.taille
                                couleur = pro.couleur
                                self.canevas.create_oval(x-10,y-10,x+10,y+10,fill="blue",tags=("projectile"))
                                self.canevas.create_line(x*e,y*e,pro.x,y,fill="white",width=2, tags=("projectile"))
                   
                        for pro in j.projectile:
                            x=pro.x*e
                            y=pro.y*e
                            taille = pro.taille
                            couleur = pro.couleur
                            self.canevas.create_oval(x-10,y-10,x+10,y+10,fill=couleur,tags=("projectile"))
                            #self.canevas.create_line(j.x*e,j.y*e,j.cibleAttaque.x*e,j.cibleAttaque.y*e,fill="white",width=2, tags=("projectile"))

            for j in i.stationspatiaux:
                if j.systemeid==self.systeme.id:
                    jx=(j.x*e)
                    jy=(j.y*e)
                    self.canevas.create_oval((jx-j.taille),(jy-j.taille),(jx+j.taille),(jy+j.taille),fill=j.couleurJoueur, tags=("artefact"), outline= "white", width = 1)
                    
    def changerproprietaire(self):
        pass
               
    def afficherselection(self):
        if self.maselection!=None:
            #print(self.maselection)
            e=self.UA2pixel
            joueur=self.modele.joueurs[self.parent.nom]
            if self.maselection[1]=="planete":
                for i in self.systeme.planetes:
                    if i.id == self.maselection[2]:
                        x=float(self.maselection[3])
                        y=float(self.maselection[4])
                        t=i.taille*100 +10
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),
                                                outline=joueur.couleur,
                                                tags=("select","selecteur"))
            if self.maselection[1]=="vaisseauinterstellaire":
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
        e=self.UA2pixel
        xy=evt.x/e,evt.y/e
        xy2=evt.x,evt.y
        t=self.canevas.gettags("current")
        if t and t[0]!="current":
            
            if t[1] == "planete"  :
                
                if self.maselection and self.maselection[1]=="vaisseauinterstellaire":
                    print("IN systeme + select VAISSEAUINTERSTELLAIRE")
                    print(xy)
                    self.parent.parent.ciblerdestination(self.maselection[2],t[2],self.systeme.id,xy)
                else:     
                    self.maselection=[self.parent.nom,t[1],t[2],t[5],t[6],t[4]]  # prop, type, id; self.canevas.find_withtag(CURRENT)#[0]
                    print(t)
                    self.montreplaneteselection()
                
            elif t[1]=="vaisseauinterstellaire":
                print("IN VAISSEAUINTERSTELLAIRE",t)
                self.maselection=[self.parent.nom,t[1],t[2],xy2]
                self.montrevaisseauxselection()  
            
            elif t[1]=="systeme":
                if self.maselection and self.maselection[1]=="vaisseauinterstellaire":
                    print("IN systeme + select VAISSEAUINTERSTELLAIRE")
                    self.parent.parent.ciblerdestination(self.maselection[2],t[2],self.systeme.id,xy)
                           
                elif self.parent.nom in t:
                    print("IN systeme  PAS SELECTION")
                    self.maselection=[self.parent.nom,t[1],t[2]]
                    self.montresystemeselection()
                else:    
                    print("IN systeme + RIEN")
                    self.maselection=None
                    self.lbselectecible.pack_forget()
                    self.canevas.delete("selecteur")
            else:
                print("Objet inconnu")
            # ici je veux envoyer un message comme quoi je visite cette planete
            # et me mettre en mode planete sur cette planete, d'une shot
            # ou est-ce que je fais selection seulement pour etre enteriner par un autre bouton
            
            #self.parent.parent.atterrirdestination(nom,idsysteme,idplanete)
        else:
            print("Region inconnue")               
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("selecteur")
    
    def cliquervue2(self,evt):
        print("vue 2")
        self.changecadreetat(None)
        e=self.UA2pixel
 
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        xy=(x/100,y/100)
      
        t=self.canevas.gettags("current")
         
        if self.maselection and self.maselection[1]=="vaisseauinterstellaire":
            print("IN systeme + select VAISSEAUINTERSTELLAIRE")
            print(xy)
           
            self.parent.parent.ciblerEspace(self.maselection[2],self.systeme.id,xy)

           
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadrevoyage)
            
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
        
        
    def voyageGalax(self):
        self.parent.parent.voyageGalax(self.maselection[0],self.maselection[2])
        self.maselection=None
        self.lbselectecible.pack_forget()
        self.canevas.delete("selecteur")