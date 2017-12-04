import random
import numpy as np
from helper import Helper as hlp
import math
from OE_objetsRessource import Ressource
from OE_objetsVaisseaux import *
from OE_objetsBatiments import *
from OE_objetsDeco import *
from IdMaker import *

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
    coordonneesPossiblesVilles = ((8, 8), (42, 42), (8, 42), (42, 8), (25, 8), (25, 42), (8, 25), (8, 42), (25, 25))#coordonnées possibles pour la création des futures villes, variable statique
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
        self.ressourceACollecter=Ressource(bronze = 2000, titanium = 2000, uranium = 2000)#################TEMPORAIRE, A MODIFIER#################
        self.tuiles = self.generationMap()
        self.x = x
        self.y = y
        self.dicRessourceParJoueur = {}
        
    
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
            self.infrastructures=[Ville(self)]"""

    def setProprietairePlanete(self, proprio, couleur):
        print('changement de proprio : ', proprio, '   pour la planete id# ', self.id)
        self.couleur=couleur
        self.proprietaire=proprio
    
    def coloniser(self, nomJoueur):
        nbVilles = 0
        for i in self.infrastructures:#on compte les villes deja presentes sur la planete et on vérifie si le joueur n'a pas déjà une ville
            if isinstance(i, Ville):
                nbVilles += 1
                if(i.proprietaire == nomJoueur):
                    self.parent.parent.parent.nouveauMessageSystemChat("Vous avez déjà une ville!")
                    return False
        if(nbVilles == len(self.coordonneesPossiblesVilles)):#verifie si le nombre de villes maximal est deja atteint
            self.parent.parent.parent.nouveauMessageSystemChat("Vous avez atteint le maximum","de ville!")
            return False
        coord = self.coordonneesPossiblesVilles[nbVilles]#coordonnee de depart
        self.parent.parent.parent.creerBatiment(nomJoueur, self.parent.id, self.id, coord[0] * 100, coord[1] * 100,"Ville")
        self.dicRessourceParJoueur[nomJoueur] = Ressource()
        
        #self.visiteurs
        self.parent.parent.parent.nouveauMessageSystemChat("Planète colonisée!")
        return True
       
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
                distsol=random.randrange(100)/10 #distance en unite astronomique 150000000km
                taille=random.randrange(5,30)/100 # en masse solaire
                angle=random.randrange(360)
                
                x,y=hlp.getAngledPoint(math.radians(angle),distsol,0,0)
                x = self.diametre/2 +x

                y = self.diametre/2 +y

                planete = Planete(self,type,distsol,taille,angle,self.parent.createurId.prochainid(), x,y)
                #planete.initplanete()
                self.planetes.append(planete)#ici
                
                
    def setProprietairePlanete(self, proprio, couleur):
        #self.proprietaire=proprio
        numPlaneteProprio = random.randrange(0,len(self.planetes))
        planeteProprio = self.planetes[numPlaneteProprio]
        planeteProprio.setProprietairePlanete(proprio.id, couleur)
                        #parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu"
        planeteProprio.infrastructures=[Ville(self, proprio.nom, self.id, planeteProprio.id, 800, 800, self.parent.createurId.prochainid(), proprio = proprio.nom)]
        planeteProprio.dicRessourceParJoueur[proprio.nom] = Ressource()
        proprio.maplanete=planeteProprio
        
        #self.parent.parent.changerTagsVue(self, planeteProprio, proprio, couleur)
