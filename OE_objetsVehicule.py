# -*- coding: utf-8 -*-

from helper import Helper as hlp
import math

class Vehicule():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        self.parent = parent
        self.id = idSuivant
        self.planeteid = planeteid
        self.systemeid=systemeid
        self.proprietaire = nom
        self.taille = 0 #a noter dans les sous-classes de vehicule
        self.angletrajet=0
        self.angleinverse=0
        self.angledegre=0
        self.x=x
        self.y=y
        self.vitesse = 0.5
        self.cible=None #tuple de x et y
        
    def ciblerdestination(self,p):
        self.cible = p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        self.angledegre = math.degrees(self.angleinverse)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        pass
    
    def rechargeBatterie(self):
        pass 
    
    
class vehiculeTank(Vehicule):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Vehicule.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=2
        self.puissance = 0
        
    def avancer(self):
        rep = None
        x=self.cible.x
        y=self.cible.y
        print(x,y)
        self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesseDeplacement,self.x,self.y)
        if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesseDeplacement:
            rep=self.cible
            self.base=self.cible
            self.cible=None
        return rep
        
    def attaque(self):
        pass
    
class vehiculeCharAssaut(Vehicule):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Vehicule.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=2
        self.puissance = 0
        
    def avancer(self):
        rep = None
        x=self.cible.x
        y=self.cible.y
        print(x,y)
        self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesseDeplacement,self.x,self.y)
        if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesseDeplacement:
            rep=self.cible
            self.base=self.cible
            self.cible=None
        return rep
        
class vehiculeCommerce(Vehicule):
    def __init__(self, parent, nom, planete, idSuivant):
        Vehicule.__init__(self,parent, nom, planete, idSuivant)
        self.vie = 0
        self.vitesseDeplacement=0
        
    def remplirChargement(self):
        pass
    
    
class vehiculeAvion(Vehicule):
    def __init__(self, parent, nom, planete, idSuivant):
        Vehicule.__init__(self,parent, nom, planete, idSuivant)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=0
        self.puissance = 0
        
    def attaque(self):
        pass
    
    
    
    
    
    