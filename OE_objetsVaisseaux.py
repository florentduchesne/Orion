import random
from helper import Helper as hlp
import math
from OE_objets import *

class Vaisseau():
    def __init__(self,parent,nom,systeme,idSuivant):
        self.parent=parent
        self.id=idSuivant
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
        self.y=self.base.y
        self.taille=16
        self.cargo=0
        self.uranium=1000
        self.besoinhumain=10
        self.besoinbronze= 100
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None 
        print("jexiste")
        
    def creerVaisseauRestriction(self):
        if (self.joueur.ressource.humain - self.besoinhumain) > 0:
            if (self.joueur.ressource.bronze - self.besoinbronze) > 0 :
                if (self.joueur.ressource.uranium - self.uranium) > 0:
                    self.joueur.ressource.humain - self.besoinhumain
                    self.joueur.ressource.bronze - self.besoinbronze
                    self.joueur.ressource.uranium - self.uranium
        

    def avancer(self):
        rep=None
        if self.cible and isinstance(self.cible, Systeme): #Deplacement dans la galaxie
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
        elif self.cible and isinstance(self.cible, Planete): #deplacement dans un système
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
        