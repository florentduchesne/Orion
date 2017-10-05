import random
from helper import Helper as hlp
import math
from OE_objetsRessource import Ressource
from OE_objetsVaisseaux import *
from OE_objetsInfrastructure import *

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
    def __init__(self,parent,type,dist,taille,angle,idSuivant):
        self.parent=parent
        self.id=idSuivant #ici
        self.parent=parent
        self.posXatterrissage=random.randrange(5000)
        self.posYatterrissage=random.randrange(5000)
        self.infrastructures=[]
        self.proprietaire="inconnu"
        self.visiteurs={}
        self.distance=dist
        self.type=type
        self.taille=taille
        self.angle=angle
        self.couleur="red"
        self.ressource=Ressource(self)
        self.ressourceACollecter=Ressource(self)
        
        #Changer moi, je ne suis pas du tout �quillibr� :(
        self.ressource.Eau=10
        self.ressourceACollecter.bronze=100
        self.ressourceACollecter.titanium=100
        self.ressourceACollecter.uranium=100
        
    def initplanete(self):
        if self.proprietaire != "inconnu":
            self.infrastructures=[Ville(self)]


    def setProprietairePlanete(self, proprio, couleur):
        print('changement de proprio : ', proprio, '   pour la planete id# ', self.id)
        self.couleur=couleur
        print('print proprio : ', proprio)
        self.proprietaire=proprio

    def creerMineRestriction(self):
        if (self.joueur.ressource.humain - self.besoinhumain)> 0 and (self.joueur.ressource.electricite - self.besoinelectricite) > 0:
            self.ressource.Humain-self.besoinhumain;
            self.ressource.Electricite-self.besoinelectricite;
            return True
        else :
            return False

class TuileGazon():
    def __init__(self,x,y):
        self.taille = 50
        self.image="gazon"
        self.x = x
        self.y = y
       
class Etoile():
    def __init__(self,parent,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
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
        systemeplanetaire=random.randrange(5) # 4 chance sur 5 d'avoir des planetes
        if systemeplanetaire:
            nbplanetes=random.randrange(12)+1
            for i in range(nbplanetes):
                type=random.choice(["roc","gaz","glace"])
                distsol=random.randrange(250)/10 #distance en unite astronomique 150000000km
                taille=random.randrange(50)/100 # en masse solaire
                angle=random.randrange(360)

                planete = Planete(self,type,distsol,taille,angle,self.parent.createurId.prochainid())
                planete.initplanete()
                self.planetes.append(planete)#ici
                
                
    def setProprietairePlanete(self, proprio, couleur):
        #self.proprietaire=proprio
        print('systeme = ', self.id, ' le nombre de planete dans le systeme : ', len(self.planetes))
        numPlaneteProprio = random.randrange(0,len(self.planetes))
        planeteProprio = self.planetes[numPlaneteProprio]
        planeteProprio.setProprietairePlanete(proprio.id, couleur)
                        #parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu"
        planeteProprio.infrastructures=[Ville(self, proprio.nom, self.id, planeteProprio.id, self.parent.createurId.prochainid())]
        
        proprio.maplanete=planeteProprio
        
        #self.parent.parent.changerTagsVue(self, planeteProprio, proprio, couleur)
