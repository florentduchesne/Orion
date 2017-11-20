import random
import numpy as np
from helper import Helper as hlp
import math
from OE_objetsRessource import Ressource
from OE_objetsVaisseaux import *
from OE_objetsBatiments import *
from OE_objetsDeco import *

class Pulsar():
    def __init__(self,parent,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.periode=random.randrange(20,50,5)
        self.moment=0
        self.phase=1 
        self.mintaille=self.taille=random.randrange(2,4)
        self.maxtaille=self.mintaille++random.randrange(1,3)
        self.pas=self.maxtaille/self.periode
        self.taille=self.mintaille
        
    def evoluer(self):
        self.moment=self.moment+self.phase
        if self.moment==0:
            self.taille=self.mintaille
            self.phase=1
        elif self.moment==self.periode:
            self.taille=self.mintaille+self.maxtaille
            self.phase=-1
        else:
            self.taille=self.mintaille+(self.moment*self.pas)
                
class Planete():
    def __init__(self,parent,type,dist,taille,angle,idSuivant,x,y):
        self.parent=parent
        self.id=idSuivant #ici
        self.parent=parent
        self.posXatterrissage=random.randrange(5000)
        self.posYatterrissage=random.randrange(5000)
        self.infrastructures=[]
        self.vehiculeplanetaire=[]
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.distance=dist
        self.type=type
        self.taille=taille
        self.angle=angle
        self.couleur="red"
        self.ressource=Ressource(bronze = 1000, bois = 1000, charbon=5000, titanium=10000, nourriture=1000, eau=1000)
        self.ressourceACollecter=Ressource(bronze = 2000, titanium = 2000, uranium = 2000)#################TEMPORAIRE, A MODIFIER#################
        self.tuiles = self.generationMap()
        self.x = x
        self.y =y
    
    def generationMap(self): 
        tuiles = []
        x = 0
        y = 0
        #image="gazon","eau"
        image="gazon"
        for i in range(0,int((5000/100)+1)):
            list = []
            tuiles.append(list)
            for j in range(0,int((5000/100)+1)):
                #gazon = TuileGazon(x,y,image[random.randrange(2)-1])
                gazon = TuileGazon(x,y,image)
                tuiles[i].append(gazon)
                x+=100
            y+=100
            x=0
        return tuiles
    """
    def initplanete(self):
        if self.proprietaire != "inconnu":
            print(self.proprietaire)
            print("initplanete dans planete")
            self.infrastructures=[Ville(self)]"""

    def setProprietairePlanete(self, proprio, couleur):
        print('changement de proprio : ', proprio, '   pour la planete id# ', self.id)
        self.couleur=couleur
        print('print proprio : ', proprio)
        self.proprietaire=proprio
       
class Etoile():
    def __init__(self,parent,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.type=random.choice(["rouge","rouge","rouge",
                                 "jaune","jaune",
                                 "bleu"])
        self.taille=random.randrange(25)/10 +0.1   # en masse solaire
        
class Systeme():
    def __init__(self,parent,x,y):
        self.parent=parent
        self.id=self.parent.createurId.prochainid()
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.diametre=50 # UA unite astronomique = 150000000km
        self.x=x
        self.y=y
        self.etoile=Etoile(self,x,y,self.parent.createurId.prochainid())
        self.planetes=[]
        self.planetesvisites=[]
        self.creerplanetes()
        
    def creerplanetes(self):
        systemeplanetaire=random.randrange(5)+1 # 4 chance sur 5 d'avoir des planetes
        if systemeplanetaire:
            nbplanetes=(random.randrange(12))+1
           
            for i in range(nbplanetes):
                type=random.choice(["roc","gaz","glace"])
                distsol=random.randrange(250)/10 #distance en unite astronomique 150000000km
                taille=random.randrange(50)/100 # en masse solaire
                angle=random.randrange(360)
                
                x,y=hlp.getAngledPoint(math.radians(angle),distsol,0,0)
                x = self.diametre/2 +x

                y = self.diametre/2 +y

                #print(x,y)
                planete = Planete(self,type,distsol,taille,angle,self.parent.createurId.prochainid(), x,y)
                #planete.initplanete()
                self.planetes.append(planete)#ici
                
                
    def setProprietairePlanete(self, proprio, couleur):
        #self.proprietaire=proprio
        print('systeme = ', self.id, ' le nombre de planete dans le systeme : ', len(self.planetes))
        numPlaneteProprio = random.randrange(0,len(self.planetes))
        planeteProprio = self.planetes[numPlaneteProprio]
        planeteProprio.setProprietairePlanete(proprio.id, couleur)
                        #parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu"
        print("proprio nom : ")
        print(proprio.nom)
        print(self.id)
        print(planeteProprio.id)
        print(self.parent.createurId.prochainid())
        planeteProprio.infrastructures=[Ville(self, proprio.nom, self.id, planeteProprio.id, self.parent.createurId.prochainid(), proprio = proprio.nom)]
        proprio.maplanete=planeteProprio
        
        #self.parent.parent.changerTagsVue(self, planeteProprio, proprio, couleur)
