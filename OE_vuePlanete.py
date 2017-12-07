# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
from helper import Helper as hlp
from OE_vuePerspective import *
import OE_objetsBatiments
from OE_objetsVehicule import vehiculeTank, vehiculehelicoptere
from DictionnaireCoutAllocationAgeBatiments import dictionnaireCoutAllocationAgeBatiments, dictionnaireProductionRessources
from OE_objetsRessource import Ressource
from test.test_iterlen import NoneLengthHint
from OE_objetsJoueur import Joueur

class VuePlanete(Perspective):
    def __init__(self,parent,syste,plane):
        Perspective.__init__(self,parent)
        self.modele=self.parent.modele
        self.planete=plane
        self.systeme=syste
        self.maselection=None
        self.mesSelections = []
        self.initX = 0
        self.initY = 0
        self.macommande=None
        self.chatEcrireLesNomsDesJoueurs()
        self.UA2pixel=self.parent.modele.diametre*2 # ainsi la terre serait a self.UA2pixel pixels du soleil et Uranus a 19 Unites Astronomiques 
        
        self.couleurBG1 = "#222831"
        self.couleurBG2 = "#393E46"
        self.couleurBouton = "#0092ca"
        self.couleurBoutonDesactive = "#50a2c1"
        
        
        self.KM2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomique       
        self.largeur=int(self.modele.diametre*self.KM2pixel)
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="green")
        
        self.btnvuesysteme.configure(bg=self.couleurBouton, command=self.voirsysteme, state=NORMAL)
        
        ##############MenuPrincipale##############
        self.btnBatiment=Button(self.cadreetataction,text="Creer un Batiment ressource",command=self.AfficherBatiment, bg=self.couleurBouton)
        self.btnBatiment.pack(side=TOP)
        self.btnInfrastructure=Button(self.cadreetataction,text="Creer une Infrastructure",command=self.AfficherInfrastructure, bg=self.couleurBouton)
        self.btnInfrastructure.pack(side=TOP)
        self.btnManufacture=Button(self.cadreetataction,text="Creer une Manufacture",command=self.AfficherManufacture, bg=self.couleurBouton)
        self.btnManufacture.pack(side=TOP)
        self.btnDefense=Button(self.cadreetataction,text="Creer une Defense",command=self.AfficherDefense, bg=self.couleurBouton)
        self.btnDefense.pack(side=TOP)
        self.btnVehicule=Button(self.cadreetataction,text="Creer un Vehicule",command=self.AfficherVehicule, bg=self.couleurBouton)
        self.btnVehicule.pack(side=TOP)
        
        ##############BATIMENTS RESSOURCES##############
        self.btncreerMine=Button(self.cadreBatiment,text="Mine",command=self.creerMine, bg=self.couleurBouton)
        self.btncreerMine.pack(side=TOP)
        self.btncreerCampBucherons=Button(self.cadreBatiment,text="Camp de bûcherons",command=self.creerCampBucherons, bg=self.couleurBouton)
        self.btncreerCampBucherons.pack(side=TOP)
        self.btncreerPuit=Button(self.cadreBatiment,text="Puit",command=self.creerpuit, bg=self.couleurBouton)
        self.btncreerPuit.pack(side=TOP)
        self.btncreerFerme=Button(self.cadreBatiment,text="Ferme",command=self.creerFerme, bg=self.couleurBouton)
        self.btncreerFerme.pack(side=TOP)
        self.btnRetour=Button(self.cadreBatiment,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
        
        
        ##############BATIMENTS INFRASTRUCTURES##############
        self.btncreerBanque=Button(self.cadreInfrastructure,text="Creer Banque",command=self.creerBanque, bg=self.couleurBouton)
        self.btncreerBanque.pack(side=TOP)
        self.btnRetour=Button(self.cadreInfrastructure,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
        
        ##############BATIMENTS MANUFACTURES##############
        self.btncreerUsineVehicules=Button(self.cadreManufacture,text="Creer Usine à Véhicules",command=self.creerUsineVehicules, bg=self.couleurBouton)
        self.btncreerUsineVehicules.pack(side=TOP)
        self.btncreerUsineVaisseaux=Button(self.cadreManufacture,text="Creer Usine à Vaisseaux",command=self.creerUsineVaisseaux, bg=self.couleurBouton)
        self.btncreerUsineVaisseaux.pack(side=TOP)
        self.btnRetour=Button(self.cadreManufacture,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
       
        
        ##############BATIMENTS DEFENSES##############
        self.btncreermur=Button(self.cadreDefense,text="Creer Mur",command=self.creermur, bg=self.couleurBouton)
        self.btncreermur.pack(side=TOP)
        self.btncreercanon=Button(self.cadreDefense,text="Creer Canon",command=self.creercanon, bg=self.couleurBouton)
        self.btncreercanon.pack(side=TOP)
        self.btncreertour=Button(self.cadreDefense,text="Creer Tour",command=self.creertour, bg=self.couleurBouton)
        self.btncreertour.pack(side=TOP)
        self.btncreerbouclier=Button(self.cadreDefense,text="Creer Bouclier",command=self.creerbouclier, bg=self.couleurBouton)
        self.btncreerbouclier.pack(side=TOP)
        self.btnRetour=Button(self.cadreDefense,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
        ##############Vehicule##############
        self.btncreertank=Button(self.cadreVehicule,text="Creer Tank",command=self.creervehiculetank, bg=self.couleurBouton)
        self.btncreertank.pack(side=TOP)
        self.btncreertank=Button(self.cadreVehicule,text="Creer Hélicoptère",command=self.creervehiculehelicoptere, bg=self.couleurBouton)
        self.btncreertank.pack(side=TOP)
        self.btnRetour=Button(self.cadreVehicule,text="Retour",command=self.Retour, bg=self.couleurBouton)
        self.btnRetour.pack(side=BOTTOM)
        
        
        ##############CADRE AMELIORATION BATIMENT##############
        self.btnAmeliorerBatiment=Button(self.cadreAmeliorationBatiments, text="Améliorer bâtiment", command=self.ameliorerBatiment, bg=self.couleurBouton)
        self.btnAmeliorerBatiment.pack()
        self.btnDetruireBatiment=Button(self.cadreAmeliorationBatiments, text="Détruire bâtiment", command=self.detruireBatiment, bg=self.couleurBouton)
        self.btnDetruireBatiment.pack()
        self.lblRessourcesAmelioration = Label(self.cadreAmeliorationBatiments, text="")
        self.lblProductionRessources = Label(self.cadreAmeliorationBatiments, text="")
        
        ##############CADRE AMELIORATION VÉHICULE##############
        
        self.btnAmeliorerVehicule=Button(self.cadreAmeliorationVehicule, text="Améliorer véhicule", command=self.ameliorerVehicule, bg=self.couleurBouton)
        self.btnAmeliorerVehicule.config(state=DISABLED);
        self.btnAmeliorerVehicule.pack()
        self.btnDetruireVehicule=Button(self.cadreAmeliorationVehicule, text="Détruire véhicule", command=self.detruireVehicule, bg=self.couleurBouton)
        self.btnDetruireVehicule.config(state=DISABLED);
        self.btnDetruireVehicule.pack()
        
        
        
        
        #self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        #self.btncreerstation.pack()
        
        self.jeMontreLeMenuDAmelioration = False
        
        self.changecadreetat(self.cadreetataction)
    
    ##############MenuPrincipale##############
    def AfficherBatiment(self):
        self.changecadreetat(self.cadreBatiment)
    def AfficherManufacture(self):
        self.changecadreetat(self.cadreManufacture)
    def AfficherInfrastructure(self):
        self.changecadreetat(self.cadreInfrastructure)
    def AfficherVehicule(self):
        self.changecadreetat(self.cadreVehicule)
    def AfficherDefense(self):
        self.changecadreetat(self.cadreDefense)
    def Retour(self):
        self.changecadreetat(self.cadreetataction)
    
    ##############BATIMENTS RESSOURCES##############
    def creerMine(self):
        self.macommande="Mine1"
    def creerCampBucherons(self):
        self.macommande="Camp_Bucherons1"
    def creerpuit(self):
        self.macommande="Puit1"
    def creerFerme(self):
        self.macommande="Ferme1"
    def creerCentraleElectrique(self):
        self.macommande="Centrale_Charbon"
    ##############BATIMENTS INFRASTRUCTURES##############
    def creerBanque(self):
        self.macommande="Banque"
    ##############BATIMENTS MANUFACTURES##############
    def creerUsineVehicules(self):
        self.macommande="Usine_Vehicule"
    def creerUsineVaisseaux(self):
        self.macommande="Usine_Vaisseau1"
    def creerUsineDrones(self):
        self.macommande="Usine_Drone"
    ##############BATIMENTS DEFENSES##############
    def creertour(self):
        self.macommande="Tour"
    def creermur(self):
        self.macommande="Mur"
    def creercanon(self):
        self.macommande="Canon"
    def creerbouclier(self):
        self.macommande="Bouclier"
    ##############UNITES AU SOL##############
    def creervehiculetank(self):
        self.macommande="vehiculetank"
        self.maselection=None
    def creervehiculehelicoptere(self):
        print("bouton")
        self.macommande="vehiculehelicoptere"
        self.maselection=None
    def creervehiculecommerce(self):
        self.macommande="vehiculecommerce"
    def creervehiculeavion(self):
        self.macommande="vehiculeavion"
    ##############AUTRES##############
    def creerstation(self):
        self.macommande="station"
        
    ##############AMELIORER BATIMENT##############
    def ameliorerBatiment(self):
                            #ou self.parent.parent.monnom?
        self.modele.joueurs[self.maselection[0]].ameliorerBatiment(self.maselection, self.planete, self.systeme)
        self.montresystemeselection()
        self.maselection = None
        
    def detruireBatiment(self):
        pass
    
    ##############AMELIORER BATIMENT##############
    def ameliorerVehicule(self): 
        self.modele.joueurs[self.maselection[0]].ameliorerVehicule(self.maselection, self.planete, self.systeme)
        self.montresystemeselection()
        self.maselection = None
        pass
    
    def detruireVehicule(self):
        pass
    
    def voirsysteme(self):
        self.parent.cadreRessourcesPlanete.pack_forget()
        for i in self.modele.systemes:
            if i.id==self.systeme:
                self.parent.voirsysteme(i)
            
    def initplanete(self,sys,plane):
        s=None
        p=None
        for i in self.modele.systemes:
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
                self.canevas.create_image(t.y,t.x,image=self.images[t.image], tags=(None, None, t.x,t.y,"tuile",t.estPrise)) 
        scrollBarX = 0
        scrollBarY = 0
        #Dessin des infrastructues de la planete.
        for i in p.infrastructures:
            if isinstance(i, OE_objetsBatiments.Ville):
                scrollBarX = i.x
                scrollBarY = i.y
                self.canevas.create_image(i.x,i.y,image=self.images["Ville"], tags=(i.proprietaire, i.planeteid, i.x,i.y,"Ville", i.id))               
                minix = (i.x *200) / self.largeur
                miniy = (i.y *200) / self.hauteur  
                for j in self.parent.modele.joueurs:
                    if j == i.proprietaire:
                        joueur = self.parent.modele.joueurs[j]
                self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill=joueur.couleur)
                
        #self.canevas.create_image(p.posXatterrissage,p.posYatterrissage,image=self.images["Ville"])
        #Centre sur la Ville principal.
        canl=int(scrollBarX-400)/self.largeur
        canh=int(scrollBarY-400)/self.hauteur
        
        self.canevas.xview(MOVETO,canl)
        self.canevas.yview(MOVETO, canh)
        
        #minix = (p.posXatterrissage *200) / self.largeur
        #miniy = (p.posYatterrissage *200) / self.hauteur
        #self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="grey11") 
    def chargeimages(self):
        im = Image.open("./images/Batiments/mine1.png")
        self.images["Mine1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/mine2.png")
        self.images["Mine2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/mine3.png")
        self.images["Mine3"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Camp_Bucherons1.png")
        self.images["Camp_Bucherons1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Camp_Bucherons2.png")
        self.images["Camp_Bucherons2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Camp_Bucherons3.png")
        self.images["Camp_Bucherons3"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/mine1.png")
        self.images["Puit1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/mine2.png")
        self.images["Puit2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/mine3.png")
        self.images["Puit3"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Usine_Vehicule.png")
        self.images["Usine_Vehicule"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Usine_Vaisseau.png")
        self.images["Usine_Vaisseau1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Usine_Vaisseau2.png")
        self.images["Usine_Vaisseau2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Usine_Drone.png")
        self.images["Usine_Drone"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Centrale_Charbon.png")
        self.images["Centrale_Charbon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Centrale_Nucleaire.png")
        self.images["Centrale_Nucleaire"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Grosse_Centrale_Nucleaire.png")
        self.images["Grosse_Centrale_Nucleaire"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Eolienne.png")
        self.images["Eolienne"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Panneau_Solaire.png")
        self.images["Panneau_Solaire"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Ville1.png")
        self.images["Ville"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ville2.png")
        self.images["Ville2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ville3.png")
        self.images["Ville3"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Banque.png")
        self.images["Banque"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Laboratoire.png")
        self.images["Laboratoire"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Puit1.png")
        self.images["Puit1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Puit2.png")
        self.images["Puit2"] = ImageTk.PhotoImage(im)
        
        
        im = Image.open("./images/Batiments/Ecole.png")
        self.images["Ecole"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/College.png")
        self.images["College"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Universite.png")
        self.images["Universite"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Ferme1.png")
        self.images["Ferme1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ferme2.png")
        self.images["Ferme2"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Batiments/Hopital1.png")
        self.images["Hopital1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Hopital2.png")
        self.images["Hopital2"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Tiles/gazon100x100.png")
        self.images["gazon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Tiles/eau100x100.png")
        self.images["eau"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Vehicules/tankhaut.png")
        self.images["vehiculetankhaut"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankbas.png")
        self.images["vehiculetankbas"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankgauche.png")
        self.images["vehiculetankgauche"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankdroit.png")
        self.images["vehiculetankdroit"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Vehicules/helibas.png")
        self.images["vehiculehelicopterebas"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/helihaut.png")
        self.images["vehiculehelicopterehaut"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/heligauche.png")
        self.images["vehiculehelicopteregauche"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/helidroit.png")
        self.images["vehiculehelicopteredroit"] = ImageTk.PhotoImage(im)
              
        im = Image.open("./images/Batiments/canon.png")
        self.images["Tour"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/wall.png")
        self.images["Mur"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/canon1.png").resize((100,100))
        self.images["Canon"] = ImageTk.PhotoImage(im)
        self.images["Canon_Ion"] = ImageTk.PhotoImage(im)
        self.images["Canon_Acid"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/bouclier.png")
        self.images["Bouclier"] = ImageTk.PhotoImage(im)
    

    def afficherdecor(self):
        pass
                
    def creervaisseau(self):
        pass

    def afficherpartie(self,mod):
        joueur=self.modele.joueurs[self.parent.nom]
        self.canevas.delete("vehiculetank")
        self.minimap.delete("vehiculetank")
        self.canevas.delete("vehiculehelicoptere")
        self.minimap.delete("vehiculehelicoptere")
        self.canevas.delete("projectile")
        #self.canevas.delete("selecteur")
        self.afficherselection()
        e=self.KM2pixel
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            if i.nouveauMessageChatTxt != None:
                self.nouveauMessageChat(i.nouveauMessageChatTxt)
                i.nouveauMessageChatTxt = None
            for j in i.vehiculeplanetaire:
                print(j)
                #if j.idSysteme==self.systeme.id:
                jx=j.x
                jy=j.y
                #jx=j.x*e
                #jy=j.y*e
                x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                
                minix = (x *200) / self.largeur 
                miniy = (y *200) / self.largeur 
                    
                if isinstance(j, vehiculeTank):                  
                    if (j.angledegre >= 0 and j.angledegre <= 45) or (j.angledegre >= 315 and j.angledegre <= 360):#gauche
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankgauche"]
                    elif j.angledegre >= 45 and j.angledegre <= 135:#haut
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankhaut"]
                    elif j.angledegre >= 135 and j.angledegre <= 225:#droit
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankdroit"]                     
                    else :#bas
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankbas"]
                        
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i.nom, j.planeteid,x ,y ,"vehiculetank",j.id) ) 
                     
                    #mini-map   
                    self.parent.modes["planetes"][j.planeteid].minimap.create_rectangle(minix-2, miniy-2, minix+2, miniy+2, fill = j.parent.couleur, tags=("vehiculetank"))                  
                    
                    if j.projectile!=None:
                        for pro in j.projectile:
                            #print("ici")
                            x=pro.x
                            y=pro.y
                            taille = pro.taille
                            couleur = pro.couleur
                            self.canevas.create_oval(x-10,y-10,x+10,y+10,fill=couleur,tags=("projectile")) 
                            
                elif isinstance(j, vehiculehelicoptere):
                    if (j.angledegre >= 0 and j.angledegre <= 45) or (j.angledegre >= 315 and j.angledegre <= 360):#gauche
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculehelicopteregauche"]
                    elif j.angledegre >= 45 and j.angledegre <= 135:#haut
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculehelicopterehaut"]
                    elif j.angledegre >= 135 and j.angledegre <= 225:#droit
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculehelicopteredroit"]   
                    else :#bas
                        im=self.parent.modes["planetes"][j.planeteid].images["vehiculehelicopterebas"]
                    
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i.nom, j.planeteid,x ,y ,"vehiculehelicoptere",j.id) ) 
                    #mini-map
                    
                    self.parent.modes["planetes"][j.planeteid].minimap.create_rectangle(minix-2, miniy-2, minix+2, miniy+2, fill = j.parent.couleur, tags=("vehiculehelicoptere"))
                    
                    if j.projectile!=None:     
                        for pro in j.projectile:
                            x=pro.x*e
                            y=pro.y*e
                            taille = pro.taille
                            couleur = pro.couleur
                            self.canevas.create_oval(x-10,y-10,x+10,y+10,fill=couleur,tags=("projectile")) 

         
         
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        self.canevas.delete("select","selecteur") 
        joueur=self.modele.joueurs[self.parent.nom]
        if self.maselection!=None:
            x = int(self.maselection[2]) - 50
            y = int(self.maselection[3]) - 50
            self.canevas.create_rectangle(x,y,x+100,y+100,dash=(2,2),outline=joueur.couleur,tags=("select","selecteur"))            
        if len(self.mesSelections) !=0:
            for v in self.mesSelections:
                for i in joueur.vehiculeplanetaire:
                    if i.id == v[5]:                    
                        x=i.x
                        y=i.y
                        t=25
                        if(x != None and y != None) :
                            self.canevas.create_rectangle((x)-t,(y)-t,(x)+t,(y)+t,dash=(2,2),
                                                        outline=joueur.couleur,
                                                        tags=("select","selecteur"))    
            
    def cliquerGauche(self, evt):
        self.canevas.delete("selectionner","select","selecteur", "lblCoutRessources") 
        t=self.canevas.gettags("current")
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)
        self.maselection = None
        self.mesSelections.clear()
        self.initX = x
        self.initY = y
        if t[0] != 'current':            
            if t[4] == 'tuile':
                self.montresystemeselection()
            elif t[4] == 'vehiculetank' or t[4] == 'vehiculehelicoptere':
                self.mesSelections.clear()
                self.montreAmeliorationVehicule()
                self.mesSelections.append(t)               
            else:
                
                self.montreAmeliorationBatiments()
                self.lblRessourcesAmelioration.pack_forget()
                self.lblProductionRessources.pack_forget()
                self.lblRessourcesAmelioration = Label(self.cadreAmeliorationBatiments, text="Aucune amélioration disponible")
                self.lblProductionRessources = Label(self.cadreAmeliorationBatiments, text="Ce bâtiment ne produit aucune ressource")
                
                #affiche le label de cout d'amélioration pour le batiment sur lequel on a cliqué
                nomBatiment = t[4]
                nomProchainNiveau = "Ville"
                for systeme in self.parent.modele.systemes:
                    if systeme.id == self.systeme:
                        for planete in systeme.planetes:
                            if planete.id == self.planete:
                                for infra in planete.infrastructures:
                                    if infra.nomBatiment == nomBatiment:
                                        if len(infra.listeNiveaux):
                                            nomProchainNiveau = infra.listeNiveaux[0]
                                            print(nomProchainNiveau)
                                            break
                                        
                ressourcesAmelioration = dictionnaireCoutAllocationAgeBatiments[nomProchainNiveau][0]
                ressourcesProduction = dictionnaireProductionRessources[nomBatiment]
                chaineListeRessourcesAmelioration = ""
                chaineListeRessourcesProduction = ""
                for ress in ressourcesAmelioration.dictRess:
                    if ressourcesAmelioration.dictRess[ress] != 0:
                        chaineListeRessourcesAmelioration +=  "\n" + ress + " : " + str(ressourcesAmelioration.dictRess[ress])
                for ress in ressourcesProduction.dictRess:
                    if ressourcesProduction.dictRess[ress] != 0:
                        chaineListeRessourcesProduction += "\n" + ress + " : " + str(ressourcesProduction.dictRess[ress])
                if chaineListeRessourcesAmelioration != "":
                    self.lblRessourcesAmelioration = Label(self.cadreAmeliorationBatiments, text="Ressources amélioration" + chaineListeRessourcesAmelioration)
                if chaineListeRessourcesProduction != "":
                    self.lblProductionRessources = Label(self.cadreAmeliorationBatiments, text="Production ressources" + chaineListeRessourcesProduction)
                self.lblRessourcesAmelioration.pack()
                self.lblProductionRessources.pack()
                self.maselection = t
                
            if self.macommande != None and t[5]=='0':
                    if (self.macommande == "vehiculetank" or self.macommande == "vehiculehelicoptere"):
                        x=self.canevas.canvasx(evt.x)
                        y=self.canevas.canvasy(evt.y)
                    else:
                        x=int(t[3])
                        y=int(t[2])
                    self.parent.parent.creerBatiment(self.parent.nom,self.systemeid,self.planeteid,x,y, self.macommande)
                    self.macommande = None
                    self.maselection=None                              
     
    def cliquerDroite(self, evt):
        self.canevas.delete("selectionner","select","selecteur") 
        t=self.canevas.gettags("current")
        if len(self.mesSelections) != 0:
            if t[4] == "vehiculetank" or t[4] == "vehiculehelicoptere":
                xdeplacement = float(t[2])
                ydeplacement = float(t[3])
            else:
                xdeplacement = self.canevas.canvasx(evt.x)
                ydeplacement = self.canevas.canvasy(evt.y)            
            for vehicule in self.mesSelections:
                self.parent.parent.ciblerdestinationvehicule(vehicule[0], xdeplacement,ydeplacement, t[5], vehicule[5])        
    
    def maintenirGauche(self, evt):
        joueur=self.modele.joueurs[self.parent.nom]
        self.mesSelections.clear() 
        x=self.canevas.canvasx(evt.x)
        y=self.canevas.canvasy(evt.y)                 
        self.canevas.delete("selectionner","select","selecteur")       
        self.canevas.create_rectangle(self.initX,self.initY,x,y,dash=(2,2),outline=joueur.couleur,tags=("selectionner"))
        pluspetitx = hlp.valeurminimal(self.initX,x)
        plusgrandx = hlp.valeurmaximal(self.initX,x)
        pluspetity = hlp.valeurminimal(self.initY,y)
        plusgrandy = hlp.valeurmaximal(self.initY,y)
        for vj in joueur.vehiculeplanetaire:
                if(vj.planeteid == self.planeteid):
                    vehiculeX = vj.x
                    vehiculeY = vj.y
                    if vehiculeX >= pluspetitx and vehiculeX <= plusgrandx and vehiculeY >= pluspetity and vehiculeY <= plusgrandy:                    
                        self.mesSelections.append((self.parent.nom,self.planeteid,vehiculeX,vehiculeY,"vehiculetank",vj.id,"current"))   
                    

    def changerTagTuile(self,posy, posx, char):  
        itemX = self.canevas.find_withtag("current")
        self.canevas.itemconfig(itemX[0],  tags=(None, None, posy,posx,"tuile",char))             
            
    def montresystemeselection(self):
        self.changecadreetat(self.cadreetataction)
        
    def montreAmeliorationBatiments(self):
        self.changecadreetat(self.cadreAmeliorationBatiments)
        
    def montreAmeliorationVehicule(self):
        self.changecadreetat(self.cadreAmeliorationVehicule)
        
    def montrevaisseauxselection(self):
        self.changecadreetat(self.cadreetatmsg)
    
    def afficherartefacts(self,joueurs):
        pass
    
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
        
    def effacerBatiment(self, id):
        self.canevas.delete(id)
    
    def afficherBatiment(self, x, y, im, t):
        minix = (x *200) / self.largeur
        miniy = (y *200) / self.hauteur
        self.canevas.create_image(x,y, image=im, tags =t)
        self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill=t[0].couleur)
        
    def afficherMine(self, x, y, im):
        minix = (x *200) / self.largeur
        miniy = (y *200) / self.hauteur
        self.canevas.create_image(x,y, image=im)
        self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="white")
        pass

