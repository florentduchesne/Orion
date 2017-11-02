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
        
        ##############BATIMENTS RESSOURCES##############
        self.btncreerMine=Button(self.cadreetataction,text="Creer Mine",command=self.creerMine)
        self.btncreerMine.pack()
        self.btncreerCampBucherons=Button(self.cadreetataction,text="Creer Camp de bûcherons",command=self.creerCampBucherons)
        self.btncreerCampBucherons.pack()
        self.btncreerPuit=Button(self.cadreetataction,text="Creer Puit",command=self.creerpuit)
        self.btncreerPuit.pack()
        self.btncreerFerme=Button(self.cadreetataction,text="Creer Ferme",command=self.creerFerme)
        self.btncreerFerme.pack()
        self.btncreerCentraleElectrique=Button(self.cadreetataction,text="Creer Centrale Electrique",command=self.creerCentraleElectrique)
        self.btncreerCentraleElectrique.pack()
        
        ##############BATIMENTS INFRASTRUCTURES##############
        self.btncreerHopital=Button(self.cadreetataction,text="Creer Hôpital",command=self.creerHopital)
        self.btncreerHopital.pack()
        self.btncreerEcole=Button(self.cadreetataction,text="Creer École",command=self.creerEcole)
        self.btncreerEcole.pack()
        self.btncreerLaboratoire=Button(self.cadreetataction,text="Creer Laboratoire",command=self.creerLaboratoire)
        self.btncreerLaboratoire.pack()
        self.btncreerBanque=Button(self.cadreetataction,text="Creer Banque",command=self.creerBanque)
        self.btncreerBanque.pack()
        
        ##############BATIMENTS MANUFACTURES##############
        self.btncreerUsineVehicules=Button(self.cadreetataction,text="Creer Usine à Véhicules",command=self.creerUsineVehicules)
        self.btncreerUsineVehicules.pack()
        self.btncreerUsineVaisseaux=Button(self.cadreetataction,text="Creer Usine à Vaisseaux",command=self.creerUsineVaisseaux)
        self.btncreerUsineVaisseaux.pack()
        self.btncreerUsineDrones=Button(self.cadreetataction,text="Creer Usine à Drones",command=self.creerUsineDrones)
        self.btncreerUsineDrones.pack()
        
        ##############BATIMENTS DEFENSES##############
        self.btncreermur=Button(self.cadreetataction,text="Creer Mur",command=self.creermur)
        self.btncreermur.pack()
        self.btncreercanon=Button(self.cadreetataction,text="Creer Canon",command=self.creercanon)
        self.btncreercanon.pack()
        self.btncreerbouclier=Button(self.cadreetataction,text="Creer Bouclier",command=self.creerbouclier)
        self.btncreerbouclier.pack()
        self.btncreertour=Button(self.cadreetataction,text="Creer Tour",command=self.creertour)
        self.btncreertour.pack()
        ##############UNITES AU SOL##############
        self.btncreertank=Button(self.cadreetataction,text="Creer Tank",command=self.creervehiculetank)
        self.btncreertank.pack()
        
        
        ##############CADRE AMELIORATION BATIMENT##############
        self.btnAmeliorerBatiment=Button(self.cadreAmeliorationBatiments, text="Améliorer bâtiment", command=self.ameliorerBatiment)
        self.btnAmeliorerBatiment.pack()
        self.btnDetruireBatiment=Button(self.cadreAmeliorationBatiments, text="Détruire bâtiment", command=self.detruireBatiment)
        self.btnDetruireBatiment.pack()
        
        #self.btncreerstation=Button(self.cadreetataction,text="Creer Station",command=self.creerstation)
        #self.btncreerstation.pack()
        
        self.btnvuesysteme=Button(self.cadreetataction,text="Voir Systeme",command=self.voirsysteme)
        self.btnvuesysteme.pack(side=BOTTOM)
        
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
        self.macommande="drones"
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
        
    def detruireBatiment(self):
        pass
    
    def voirsysteme(self):
        self.parent.cadreRessourcesPlanete.pack_forget()
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
                self.canevas.create_image(t.y,t.x,image=self.images[t.image], tags=(None, None, t.x,t.y,"tuile"))
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
                self.canevas.create_image(i.x,i.y,image=self.images["ville"], tags=(None, None, t.x,t.y,"tuile"))               
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
        
        im = Image.open("./images/Batiments/Ferme1.png")
        self.images["Ferme1"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Batiments/Ferme2.png")
        self.images["Ferme2"] = ImageTk.PhotoImage(im)
        
        im = Image.open("./images/Tiles/gazon100x100.png")
        self.images["gazon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Tiles/eau100x100.png")
        self.images["eau"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/Vehicules/tankhaut.png")
        self.images["vehiculetank"] = ImageTk.PhotoImage(im)
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
        pass
            
    def changerproprietaire(self,prop,couleur,systeme): 
        pass
               
    def afficherselection(self):
        pass
      
    def cliquervue(self,evt):
        t=self.canevas.gettags("current")
        print("print t")
        print(t)
        
        
        if self.maselection ==None and t[4] != 'tuile':
            self.maselection = t
            pass
        elif self.maselection != None and t[4] == 'tuile':
            if self.maselection[4] == 'vehiculetank': 
                print('le tank va finir par avancer!!!')
                self.parent.parent.ciblerdestinationvehicule(self.maselection[0], evt.x,evt.y, t[1])
                self.maselection = None
                pass
        
        if t and t[0]!="current":
            if t[0]==self.parent.nom:
                self.montreAmeliorationBatiments()
                self.macommande=None
                self.maselection=None
                print("montre menu amelioration")
                pass
            elif t[1]=="systeme":
                pass
            elif self.maselection == None and t[4]=="tuile":
                print("creation batiment")
                if self.macommande == "vehiculetank":
                    x=self.canevas.canvasx(evt.x)
                    y=self.canevas.canvasy(evt.y)
                    self.parent.parent.creerBatiment(self.parent.nom,self.systemeid,self.planeteid,x,y, "vehiculetank")
                    minix = (x *200) / self.largeur
                    miniy = (y *200) / self.hauteur
                    self.minimap.create_rectangle(minix-2,miniy-2,minix+2,miniy+2,fill="SpringGreen3")

                    self.macommande=None
                    self.maselection=None
                elif self.macommande != None:
                    print("ma commande")
                    print(self.macommande)
                    x=int(t[3])
                    y=int(t[2])
                    print('position de la mine x = {0}, y = {1}'.format(t[0],t[1]))
                    self.parent.parent.creerBatiment(self.parent.nom,self.systemeid,self.planeteid,x,y, self.macommande)
                    self.macommande = None
                else:
                    self.montresystemeselection()
                    print("montre menu a droite")
                    self.macommande=None
                    self.maselection=None
            #elif self.macommande == None:
                
                
                
            
            '''
            elif self.maselection != None and t[2] == "tuile":
                self.maselection = [self.parent.monnom,t[1],t[2]]
                print("coucou")
                print(self.maselection)
                pass
            '''
    
            
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
    
