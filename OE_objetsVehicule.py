# -*- coding: utf-8 -*-

from OE_objetsRessource import Ressource
from helper import Helper as hlp
import math

class Vehicule():
    
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant,nomVehicule):
        self.parent = parent
        self.id = idSuivant
        self.planeteid = planeteid
        self.systemeid=systemeid
        self.nomVehicule = nomVehicule
        self.proprietaire = parent.nom
        self.niveau = parent.niveau
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
    
    def avancer(self):
        rep = None
        x=self.cible.x
        y=self.cible.y
        self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesseDeplacement,self.x,self.y)
        if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesseDeplacement:
            rep=self.cible
            self.base=self.cible
            self.cible=None
        return rep  
    
    def verificationRessources(self):
            infoCout = dictionnaireCoutVehicule[self.nomVehicule]
            coutressource = infoCout[0]
            if (self.parent.ressources.estPlusGrandOuEgal(coutressource)):
                #diminuer les ressources au joueur
                self.parent.ressources.soustraireRessources(coutressource)   
                return True
            else:
                return False
 
    def ameliorer(self):
        nomVehiculeAmeliorer = self.nomVehicule[:-1]
        infoCout = dictionnaireCoutVehicule[nomVehiculeAmeliorer]
        coutressource = infoCout[0]
        
        if (self.parent.ressources.estPlusGrandOuEgal(coutressource)):
            #diminuer les ressources au joueur
            self.parent.ressources.soustraireRessources(coutressource)   
            return True
        else:
            return False
        
        self.nomVehicule = nomVehiculeAmeliorer
        pass
    
    def rechargeBatterie(self):
        pass 
    
    
class vehiculeTank(Vehicule):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomVehicule):
        Vehicule.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomVehicule)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=2
        self.puissance = 0
        
    def attaque(self):
        pass
    
class vehiculehelicoptere(Vehicule):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomVehicule):
        Vehicule.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomVehicule)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=2
        self.puissance = 0
    
    
dictionnaireCoutVehicule={
"vehiculetank1":[Ressource(bois=10, bronze=10), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"vehiculetank2":[Ressource(bois=50, bronze=50), Ressource(allocationElectricite=10, allocationHumain=10), 2],
"vehiculetank3":[Ressource(bois=100, bronze=100), Ressource(allocationElectricite=20, allocationHumain=20), 3],
"vehiculehelicoptere1":[Ressource(bois=10, bronze=10), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"vehiculehelicoptere2":[Ressource(bois=50, bronze=50), Ressource(allocationElectricite=10, allocationHumain=10), 2],
"vehiculehelicoptere3":[Ressource(bois=100, bronze=100), Ressource(allocationElectricite=20, allocationHumain=20), 3]
    }
    
    
    
    
    
    