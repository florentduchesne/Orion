# -*- coding: utf-8 -*-



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
        self.x=x
        self.y=y
        self.cible=None 
        
    def ciblerDestination(self):
        pass
    
    def rechargeBatterie(self):
        pass 
    
    
class vehiculeTank(Vehicule):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Vehicule.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.qtProjectile = 0
        self.vitesseAttaque = 0
        self.vie = 0
        self.vitesseDeplacement=0
        self.puissance = 0
        
    def attaque(self):
        pass
    
        
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
    
    
    
    
    
    