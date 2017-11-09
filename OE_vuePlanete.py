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
        self.maselection=None
        self.macommande=None
        
        self.KM2pixel=100 # ainsi la terre serait a 100 pixels du soleil et Uranus a 19 Unites Astronomique       
        self.largeur=int(self.modele.diametre*self.KM2pixel)
        self.hauteur=self.largeur
        
        self.canevas.config(scrollregion=(0,0,self.largeur,self.hauteur))
        self.canevas.config(bg="green")
        
        ##############MenuPrincipale##############
        self.btnBatiment=Button(self.cadreetataction,text="Creer un Batiment ressource",command=self.AfficherBatiment)
        self.btnBatiment.pack(side=TOP)
        self.btnInfrastructure=Button(self.cadreetataction,text="Creer une Infrastructure",command=self.AfficherInfrastructure)
        self.btnInfrastructure.pack(side=TOP)
        self.btnManufacture=Button(self.cadreetataction,text="Creer une Manufacture",command=self.AfficherManufacture)
        self.btnManufacture.pack(side=TOP)
        self.btnDefense=Button(self.cadreetataction,text="Creer une Defense",command=self.AfficherDefense)
        self.btnDefense.pack(side=TOP)
        self.btnVehicule=Button(self.cadreetataction,text="Creer un Vehicule",command=self.AfficherVehicule)
        self.btnVehicule.pack(side=TOP)
        
        ##############BATIMENTS RESSOURCES##############
        self.btncreerMine=Button(self.cadreBatiment,text="Mine",command=self.creerMine)
        self.btncreerMine.pack(side=TOP)
        self.btncreerCampBucherons=Button(self.cadreBatiment,text="Camp de bûcherons",command=self.creerCampBucherons)
        self.btncreerCampBucherons.pack(side=TOP)
        self.btncreerPuit=Button(self.cadreBatiment,text="Puit",command=self.creerpuit)
        self.btncreerPuit.pack(side=TOP)
        self.btncreerFerme=Button(self.cadreBatiment,text="Ferme",command=self.creerFerme)
        self.btncreerFerme.pack(side=TOP)
        self.btnRetour=Button(self.cadreBatiment,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
        
        
        ##############BATIMENTS INFRASTRUCTURES##############
        self.btncreerEcole=Button(self.cadreInfrastructure,text="Creer École",command=self.creerEcole)
        self.btncreerEcole.pack(side=TOP)
        self.btncreerHopital=Button(self.cadreInfrastructure,text="Creer Hôpital",command=self.creerHopital)
        self.btncreerHopital.pack(side=TOP)
        self.btncreerBanque=Button(self.cadreInfrastructure,text="Creer Banque",command=self.creerBanque)
        self.btncreerBanque.pack(side=TOP)
        self.btncreerLaboratoire=Button(self.cadreInfrastructure,text="Creer Laboratoire",command=self.creerLaboratoire)
        self.btncreerLaboratoire.pack(side=TOP)
        self.btnRetour=Button(self.cadreInfrastructure,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
        
        ##############BATIMENTS MANUFACTURES##############
        self.btncreerCentraleElectrique=Button(self.cadreManufacture,text="Centrale Electrique",command=self.creerCentraleElectrique)
        self.btncreerCentraleElectrique.pack(side=TOP)
        self.btncreerUsineVehicules=Button(self.cadreManufacture,text="Creer Usine à Véhicules",command=self.creerUsineVehicules)
        self.btncreerUsineVehicules.pack(side=TOP)
        self.btncreerUsineVaisseaux=Button(self.cadreManufacture,text="Creer Usine à Vaisseaux",command=self.creerUsineVaisseaux)
        self.btncreerUsineVaisseaux.pack(side=TOP)
        self.btncreerUsineDrones=Button(self.cadreManufacture,text="Creer Usine à Drones",command=self.creerUsineDrones)
        self.btncreerUsineDrones.pack(side=TOP)
        self.btnRetour=Button(self.cadreManufacture,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
       
        
        ##############BATIMENTS DEFENSES##############
        self.btncreermur=Button(self.cadreDefense,text="Creer Mur",command=self.creermur)
        self.btncreermur.pack(side=TOP)
        self.btncreercanon=Button(self.cadreDefense,text="Creer Canon",command=self.creercanon)
        self.btncreercanon.pack(side=TOP)
        self.btncreertour=Button(self.cadreDefense,text="Creer Tour",command=self.creertour)
        self.btncreertour.pack(side=TOP)
        self.btncreerbouclier=Button(self.cadreDefense,text="Creer Bouclier",command=self.creerbouclier)
        self.btncreerbouclier.pack(side=TOP)
        self.btnRetour=Button(self.cadreDefense,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
        ##############Vehicule##############
        self.btncreertank=Button(self.cadreVehicule,text="Creer Tank",command=self.creervehiculetank)
        self.btncreertank.pack(side=TOP)
        self.btnRetour=Button(self.cadreVehicule,text="Retour",command=self.Retour)
        self.btnRetour.pack(side=BOTTOM)
        
        
        ##############CADRE AMELIORATION BATIMENT##############
        self.btnAmeliorerBatiment=Button(self.cadreAmeliorationBatiments, text="Améliorer bâtiment", command=self.ameliorerBatiment)
        self.btnAmeliorerBatiment.pack()
        self.btnDetruireBatiment=Button(self.cadreAmeliorationBatiments, text="Détruire bâtiment", command=self.detruireBatiment)
        self.btnDetruireBatiment.pack()
        
        #self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        #self.btncreerstation.pack()
        
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir Systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
        
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
    def creerHopital(self):
        self.macommande="Hopital1"
    def creerEcole(self):
        self.macommande="Ecole"
    def creerLaboratoire(self):
        self.macommande="laboratoire"
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
    def creervehiculecommerce(self):
        self.macommande="vehiculecommerce"
    def creervehiculeavion(self):
        self.macommande="vehiculeavion"
    ##############AUTRES##############
    def creerstation(self):
        self.macommande="station"
        print("Creer station EN CONSTRUCTION")
        
    ##############AMELIORER BATIMENT##############
    def ameliorerBatiment(self):
        print("ON AMELIORE UN BATIMENT")
        self.modele.joueurs[self.maselection[0]].ameliorerBatiment(self.maselection, self.planete, self.systeme)
        self.montresystemeselection()
        self.maselection = None
        
    def detruireBatiment(self):
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
                self.canevas.create_image(i.x,i.y,image=self.images["ville"], tags=(i.proprietaire, i.planeteid, t.x,t.y,"ville", i.id))               
                minix = (i.x *200) / self.largeur
                miniy = (i.y *200) / self.hauteur
                
                self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="grey11")
            else:
               #self.parent.afficherBatiment(joueur,systemeid,planeteid,x,y,nom)
               pass
                
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
        self.images["Usine_Vaisseau"] = ImageTk.PhotoImage(im)
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
        self.images["ville"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ville2.png")
        self.images["ville2"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ville3.png")
        self.images["ville3"] = ImageTk.PhotoImage(im)
        
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
        self.images["vehiculetank"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankbas.png")
        self.images["vehiculetankbas"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankgauche.png")
        self.images["vehiculetankgauche"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankdroit.png")
        self.images["vehiculetankdroit"] = ImageTk.PhotoImage(im)
              
        im = Image.open("./images/Batiments/canon.png")
        self.images["Tour"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/wall.png")
        self.images["Mur"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/canon1.png").resize((100,100))
        self.images["Canon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/bouclier.png")
        self.images["Bouclier"] = ImageTk.PhotoImage(im)
    

    def afficherdecor(self):
        pass
                
    def creervaisseau(self):
        pass

    def afficherpartie(self,mod):
        
        self.canevas.delete("vehiculetank")
        #self.canevas.delete("selecteur")
        self.afficherselection()
        #e=self.UA2pixel
        for i in mod.joueurscles:
            i=mod.joueurs[i]
            for j in i.vehiculeplanetaire:
                #if j.idSysteme==self.systeme.id:
                jx=j.x
                jy=j.y
                #jx=j.x*e
                #jy=j.y*e
                x2,y2=hlp.getAngledPoint(j.angletrajet,8,jx,jy)
                x1,y1=hlp.getAngledPoint(j.angletrajet,4,jx,jy)
                x0,y0=hlp.getAngledPoint(j.angleinverse,4,jx,jy)
                x,y=hlp.getAngledPoint(j.angleinverse,7,jx,jy)
                
                #ajouter if pour changer l'image selon l'angle de la destination...
                if (j.angledegre >= 0 and j.angledegre <= 45) or (j.angledegre >= 315 and j.angledegre <= 360):#gauche
                    im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankgauche"]
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i, j.planeteid,x ,y ,"vehiculetank",j.id) )  
                    pass
                elif j.angledegre >= 45 and j.angledegre <= 135:#haut
                    im=self.parent.modes["planetes"][j.planeteid].images["vehiculetank"]
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i, j.planeteid,x ,y ,"vehiculetank",j.id) ) 
                    pass
                elif j.angledegre >= 135 and j.angledegre <= 225:#droit
                    im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankdroit"]
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i, j.planeteid,x ,y ,"vehiculetank",j.id) ) 
                    pass
                else :#bas
                    im=self.parent.modes["planetes"][j.planeteid].images["vehiculetankbas"]
                    self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i, j.planeteid,x ,y ,"vehiculetank",j.id) ) 
                    pass
                #im=self.parent.modes["planetes"][j.planeteid].images["vehiculetank"]
                #self.parent.modes["planetes"][j.planeteid].canevas.create_image(x,y,image=im, tags = (i, j.planeteid,x ,y ,"vehiculetank",j.id) )   
                
                '''
                self.canevas.create_line(x,y,x0,y0,fill="yellow",width=3,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                self.canevas.create_line(x0,y0,x1,y1,fill=i.couleur,width=4,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                self.canevas.create_line(x1,y1,x2,y2,fill="red",width=2,
                                         tags=(j.proprietaire,"vaisseauinterstellaire",j.id,"artefact"))
                '''
         
         
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        
        if self.maselection!=None:
            #e=self.UA2pixel
            joueur=self.modele.joueurs[self.parent.nom]
            if self.maselection[4]=="vehiculetank":
                for i in joueur.vehiculeplanetaire:
                    if i.id == self.maselection[1]:
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas
                        
                        '''
                        self.canevas.create_rectangle((x*e)-t,(y*e)-t,(x*e)+t,(y*e)+t,dash=(2,2),
                                                    outline=joueur.couleur,
                                                    tags=("select","selecteur"))
                        '''
        
    def cliquervue(self,evt):
        t=self.canevas.gettags("current")
        
        
        ##REMET LE MENU A DROITE PAR DEFAUT APRES AVOIR AMELIORE UN BATIMENT##
        if(self.jeMontreLeMenuDAmelioration):
            self.jeMontreLeMenuDAmelioration = False
            self.montresystemeselection()
            print("montre menu a droite")
            self.macommande=None
            self.maselection=None
        
        print("print t : ")
        print(t)
        print('event : ' + str(evt.x) + ' - ' + str(evt.y))
        
        if self.maselection ==None and t[4] != 'tuile':
            self.maselection = t
            pass
        elif self.maselection != None and t[4] == 'tuile':
            if self.maselection[4] == 'vehiculetank': 
                print('le tank va finir par avancer!!!')
                print('destination : ' + str(evt.x) +' - ' + str(evt.y))
                print('actuel : ' + str(self.maselection[2]) + ' - ' + str(self.maselection[3]))
                
                xdeplacement = self.canevas.canvasx(evt.x)
                ydeplacement = self.canevas.canvasx(evt.y)
                self.parent.parent.ciblerdestinationvehicule(self.maselection[0], xdeplacement,ydeplacement, t[1], self.maselection[5])
                self.maselection = None
                pass
        else:
            self.maselection = None
        
        if t and t[0]!="current":
            if t[0]==self.parent.nom:##SI ON CLIQUE SUR UN BATIMENT, ON MONTRE LE MENU D'AMELIORATION
                self.montreAmeliorationBatiments()
                self.macommande=None
                self.jeMontreLeMenuDAmelioration = True
                print("clic sur un batiment existant")
                pass
            elif t[1]=="systeme":
                pass
            elif self.maselection == None and t[4]=="tuile":
                print(t)
                print("clic sur une tuile vide")
                if self.macommande == "vehiculetank"  and t[5]=='0':
                    x=self.canevas.canvasx(evt.x)
                    y=self.canevas.canvasy(evt.y)
                    self.parent.parent.creerBatiment(self.parent.nom,self.systemeid,self.planeteid,x,y, "vehiculetank")
                    minix = (x *200) / self.largeur
                    miniy = (y *200) / self.hauteur
                    self.minimap.create_rectangle(minix-2,miniy-2,minix+2,miniy+2,fill="SpringGreen3")
                    #self.changerTagTuile(t[3],t[2],'1')
                    self.macommande=None
                    self.maselection=None

                elif self.macommande != None and t[5]=='0':
                    x=int(t[3])
                    y=int(t[2])
                    print('position de la mine x = {0}, y = {1}'.format(t[0],t[1]))
                    self.parent.parent.creerBatiment(self.parent.nom,self.systemeid,self.planeteid,x,y, self.macommande)
                    self.macommande = None
                        
                    
    def changerTagTuile(self,posy, posx, char):  
        itemX = self.canevas.find_withtag("current")
        self.canevas.itemconfig(itemX[0],  tags=(None, None, posy,posx,"tuile",char))             
            
    def montresystemeselection(self):
        self.changecadreetat(self.cadreetataction)
        
    def montreAmeliorationBatiments(self):
        self.changecadreetat(self.cadreAmeliorationBatiments)
        
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
    
    def afficherBatiment(self, x, y, im, t):
        minix = (x *200) / self.largeur
        miniy = (y *200) / self.hauteur
        self.canevas.create_image(x,y, image=im, tags = t)
        self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="white")
        
    def afficherMine(self, x, y, im):
        minix = (x *200) / self.largeur
        miniy = (y *200) / self.hauteur
        self.canevas.create_image(x,y, image=im)
        self.minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="white")
        pass
    
