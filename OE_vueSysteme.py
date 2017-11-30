# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import math
from helper import Helper as hlp
from OE_vuePerspective import *
from math import degrees
from OE_objetsVaisseaux import VaisseauChasseur, VaisseauColonisation, VaisseauAttaque, VaisseauTank, VaisseauMere



class VueSysteme(Perspective):
    def __init__(self,parent):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planetes={}
        self.systeme=None
        self.maselection=None
        self.couleurBG1 = "#222831"
        self.couleurBG2 = "#393E46"
        self.couleurBouton = "#0092ca"
        self.couleurBoutonDesactive = "#50a2c1"
        self.chatEcrireLesNomsDesJoueurs()
        
        self.btnvuegalaxie.configure(bg=self.couleurBouton, command=self.voirgalaxie, state=NORMAL)
        
        self.mesSelections=[]
        self.initX = 0
        self.initY = 0
        self.UA2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomiques       
        print("Diametre: ", self.modele.diametre)
        self.largeur=int(self.modele.diametre*self.UA2pixel)
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        
        self.labid.bind("<Button>",self.identifierplanetemere)
        self.btncreervaisseau=Button(self.cadreetataction,text="Creer Vaisseau",command=self.AfficherChoixVaisseau, bg=self.couleurBouton)
        self.btncreervaisseau.pack()
        
        ##############Base##############
        self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation, bg=self.couleurBouton)
        self.btncreerstation.pack()

        self.btnRecolterRessources=Button(self.cadreetataction, text="Récolter les ressources", command=self.recolterRessources, bg=self.couleurBouton)
        self.btnRecolterRessources.pack()
        
        ##############Vaisseaux##############
        self.btnChasseur=Button(self.cadreVaisseau,text="Vaisseau Chasseur", bg=self.couleurBouton,command = lambda : self.creervaisseau("chasseur"))
        self.btnChasseur.pack(side=TOP)
        self.btnCommerce=Button(self.cadreVaisseau,text="Vaisseau Commerce", bg=self.couleurBouton,command = self.creervaisseau2("commerce"))
        self.btnCommerce.pack(side=TOP)
        self.btnBombarde=Button(self.cadreVaisseau,text="Vaisseau Bombarde", bg=self.couleurBouton,command = self.creervaisseau2("bombarde"))
        self.btnBombarde.pack(side=TOP)
        self.btnColonisation=Button(self.cadreVaisseau,text="Vaisseau Colonisation", bg=self.couleurBouton,command = lambda : self.creervaisseau("colonisateur"))
        self.btnColonisation.pack(side=TOP)
        self.btnTank=Button(self.cadreVaisseau,text="Vaisseau Tank", bg=self.couleurBouton,command = lambda : self.creervaisseau("tank"))
        self.btnTank.pack(side=TOP)
        self.btnMere=Button(self.cadreVaisseau,text="Vaisseau Mere", bg=self.couleurBouton,command = lambda : self.creervaisseau("mere"))
        self.btnMere.pack(side=TOP)
        self.btnLaser=Button(self.cadreVaisseau,text="Vaisseau Laser", bg=self.couleurBouton,command = self.creervaisseau2("laser"))
        self.btnLaser.pack(side=TOP)
        self.btnNova=Button(self.cadreVaisseau,text="Vaisseau Nova", bg=self.couleurBouton,command = self.creervaisseau2("nova"))
        self.btnNova.pack(side=TOP)
        self.btnSuicide=Button(self.cadreVaisseau,text="Vaisseau Suicide", bg=self.couleurBouton,command = self.creervaisseau2("suicide"))
        self.btnSuicide.pack(side=TOP)
        self.btnBiologique=Button(self.cadreVaisseau,text="Vaisseau Biologique", bg=self.couleurBouton,command = self.creervaisseau2("biologique"))
        self.btnBiologique.pack(side=TOP)
        self.btnRetour=Button(self.cadreVaisseau,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
        
        self.lbselectecible=Label(self.cadreetatmsg,text="Choisir cible",bg="darkgrey")
        self.lbselectecible.pack()
        
        #voyage
        self.btnVoyage=Button(self.cadrevoyage,text ="Voyage dans galaxie", bg=self.couleurBouton,command =self.voyageGalax)
        self.btnVoyage.pack()
        
        self.changecadreetat(self.cadreetataction)
        
    def voirplanete(self):
        self.parent.voirplanete(self.maselection)
        self.btnvueplanete.configure(bg=self.couleurBoutonDesactive, command=self.voirplanete, state=DISABLED)

    def voirgalaxie(self):
        self.parent.voirgalaxie()
        self.btnvueplanete.configure(bg=self.couleurBoutonDesactive, command=self.voirplanete, state=DISABLED)
    
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
        
    def recolterRessources(self):
        if self.maselection and self.maselection[1] == "planete":
            print(self.maselection)
                                        #i.proprietaire,"planete",planete.id,"inconnu", systeme.id,x,y
            self.parent.parent.recolterRessources(self.maselection[5], self.maselection[2])
            pass
    
    def chargeimages(self):
        for x in range(0,361):
            im = Image.open("./images/colonisateur.png")
            self.images[("colonisateur"+str(x))] = ImageTk.PhotoImage(im.rotate(-x)) 
            im = Image.open("./images/chasseur.png")
            self.images[("chasseur"+str(x))] = ImageTk.PhotoImage(im.rotate(-x)) 
            im = Image.open("./images/vaisseauTank.png")
            self.images[("tank"+str(x))] = ImageTk.PhotoImage(im.rotate(-x))  
            im = Image.open("./images/vaisseauMere.png")
            self.images[("mere"+str(x))] = ImageTk.PhotoImage(im.rotate(-x))    

    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.canevas.delete("selecteur")
        self.canevas.delete("projectile")
        self.canevas.delete("stationspatiale")
        self.afficherselection()
        e=self.UA2pixel
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            if i.nouveauMessageChatTxt != None:
                self.nouveauMessageChat(i.nouveauMessageChatTxt)
                i.nouveauMessageChatTxt = None
            for j in i.vaisseauxinterstellaires:
                if j.idSysteme==self.systeme.id:
                    if j.dansGalaxie==False:
                        jx=j.x*e
                        jy=j.y*e
                        x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
   
                        angle = int(math.degrees(j.angleinverse))

                                        
                     #   if (isinstance(j, VaisseauChasseur)):
                    #        jx=j.x*e
                   #         jy=j.y*e
                  #          x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                            #x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                           # x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                          #  x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                            
                      
                            #self.canevas.create_line(x,y,x0,y0,fill="yellow",width=3,
                             #                        tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",))
                            #self.canevas.create_line(x0,y0,x1,y1,fill=i.couleur,width=4,
                              #                       tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y))
                           # self.canevas.create_line(x1,y1,x2,y2,fill="red",width=2,
                            #                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                            
                        if isinstance(j,VaisseauChasseur):
                            if not j.dansVaisseauMere:
                                tag =("chasseur"+str(angle))
                                im=self.parent.modes["systemes"][j.idSysteme].images[tag]
                                self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"chasseur") )

                        elif isinstance(j,VaisseauColonisation) :
                            if not j.dansVaisseauMere:
                                tag =("colonisateur"+str(angle))
                                im=self.parent.modes["systemes"][j.idSysteme].images[tag]     
                                self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"colonisateur") )  

        
                        elif isinstance(j, VaisseauTank) :
                            if not j.dansVaisseauMere:
                                tag =("tank"+str(angle))
                                im=self.parent.modes["systemes"][j.idSysteme].images[tag]
                                self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"tank") )
                        
                        elif isinstance(j, VaisseauMere) :
                            tag =("mere"+str(angle))
                            im=self.parent.modes["systemes"][j.idSysteme].images[tag]
                            self.parent.modes["systemes"][j.idSysteme].canevas.create_image(x,y,image=im, tags = (j.proprietaire,"vaisseauinterstellaire",j.id,"artefact",x,y,"mere") )

                        
                        if isinstance(j, VaisseauAttaque) :
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
                    self.canevas.create_oval((jx-j.taille),(jy-j.taille),(jx+j.taille),(jy+j.taille),fill=j.couleurJoueur, tags=(j.proprietaire,"stationspatiale",j.id,j.x,j.y), outline= "white", width = 1)
                    
    def changerproprietaire(self):
        pass
               
    def afficherselection(self):
        e=self.UA2pixel
        joueur=self.modele.joueurs[self.parent.nom]
        if self.maselection!=None:
            #print(self.maselection)
            
            if self.maselection[1]=="planete":
                for i in self.systeme.planetes:
                    if i.id == self.maselection[2]:
                        x=float(self.maselection[3])
                        y=float(self.maselection[4])
                        t=i.taille*100 +10
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),
                                                outline=joueur.couleur,
                                                tags=("select","selecteur"))
            elif self.maselection[1]=="stationspatiale":
                print("Selectionner StaionSpatiale!!!!")
                print("Station ID: " + str(self.maselection[2]))
                
        if len(self.mesSelections) !=0:
            for v in self.mesSelections:
                for i in joueur.vaisseauxinterstellaires:
                    if i.id == v[2]:
                        x=i.x
                        y=i.y
                        t=25
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
        for v in joueur.vaisseauxinterstellaires:
                if(v.idSysteme == self.systeme.id):
                    vaisseauX = v.x*100
                    vaisseauY = v.y*100                   
                    if vaisseauX >= pluspetitx and vaisseauX <= plusgrandx and vaisseauY >= pluspetity and vaisseauY <= plusgrandy:                    
                        self.mesSelections.append((self.parent.nom,"vaisseauinterstellaire",v.id))
    
        
    def cliquerGauche(self,evt):
        self.canevas.delete("selectionner")   
        self.maselection = None
        self.mesSelections.clear()        
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        self.initX = x
        self.initY = y
        xy2=evt.x,evt.y
        t=self.canevas.gettags("current")
        self.btnvueplanete.configure(bg=self.couleurBoutonDesactive, command=self.voirplanete, state=DISABLED)
        
        #liste de tuples 1: le type de la selection(planete, vaisseau), 2: le id de la selection
        print(t)
        if len(t) != 0:
            if t[1] == "planete":
                self.maselection=[self.parent.nom,t[1],t[2],t[5],t[6],t[4]]  # prop, type, id; self.canevas.find_withtag(CURRENT)#[0]
                self.montreplaneteselection()
                self.btnvueplanete.configure(bg=self.couleurBouton, command=self.voirplanete, state=NORMAL)
            elif t[1] == "stationspatiale":
                self.maselection=[self.parent.nom,t[1],t[2],t[3],t[4]]
            elif t[1] == "vaisseauinterstellaire":
                self.cadrevoyage.pack()
                self.mesSelections.append((self.parent.nom,t[1],t[2]))
            elif len(t) >= 6:
                if t[6] == "mere":
                    self.mesSelections.append((self.parent.nom,t[1],t[2],xy2))
                    self.montrevaisseauxselection()
            elif t[1] == "vaisseauinterstellaire":
                self.mesSelections.append((self.parent.nom,t[1],t[2],xy2)) 
                self.pasVoyager() 
          
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
                    if t[1] == "planete":
                        planete=[self.parent.nom,t[1],t[2],t[5],t[6],t[4]]
                        self.parent.parent.ciblerdestination(v[2],planete[2],self.systeme.id,xy)
                    elif t[1] == "vaisseauinterstellaire":
                        vaisseau=[self.parent.nom,t[1],t[2],xy2]
                        print(vaisseau)
                        print(v)
                        self.parent.parent.ciblerdestination(v[2],vaisseau[2],self.systeme.id,xy)
                else:
                    self.parent.parent.ciblerEspace(v[2],self.systeme.id,xy)

        
    def cliquerCentre(self, evt):
        xy2=evt.x,evt.y
        t=self.canevas.gettags("current")
        if len(t) != 0:
            if t[6] == "mere":
                self.mesSelections.append((self.parent.nom,t[1],t[2],xy2))
                self.montrevaisseauxselection()
            elif t[1] == "vaisseauinterstellaire":
                self.mesSelections.append((self.parent.nom,t[1],t[2],xy2)) 
                self.pasVoyager() 
                    
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadrevoyage)
        
    def RemplirVaisseau(self):
        pass
    
    def ViderVaisseau(self):
        pass
    
    def pasVoyager(self):
        self.changecadreetat(None)
            
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
        joueur=self.modele.joueurs[self.parent.nom]
        for v in self.mesSelections:        
            self.parent.parent.voyageGalax(v[0],v[2])        
            for jv in joueur.vaisseauxinterstellaires:
                if jv.id == v[2]:
                    if isinstance(jv, VaisseauMere):
                        jv.dansGalaxie = True
                        jv.cible=None             
        self.maselection=None
        self.mesSelections.clear()
        self.lbselectecible.pack_forget()
        self.canevas.delete("selecteur")
