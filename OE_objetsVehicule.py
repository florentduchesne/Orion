# -*- coding: utf-8 -*-



class Vehicule():
    def __init__(self, parent, nom, planete, idSuivant, idplanete):
        self.parent = parent
        self.id = idSuivant
        self.idplanete = idplanete
        self.proprietaire = nom
        self.taille = 0 #a noter dans les sous-classes de vehicule
        self.base = planete
        self.angletrajet=0
        self.angleinverse=0
        self.x=self.base.x
        self.y=self.base.y
        self.cible=None 
        
    def ciblerDestination(self):
        pass
    
    def rechargeBatterie(self):
        pass 
    
    
class vehiculeTank(Vehicule):
    def __init__(self, parent, nom, planete, idSuivant):
        Vehicule.__init__(self,parent, nom, planete, idSuivant)
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
    
    
    
    
    
    