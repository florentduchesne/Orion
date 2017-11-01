from OE_objetsRessource import *
import math
#super-classe des mines, camps de bucherons, etc.
class BatimentRessources():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment, production):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        self.productionRessources = production
        
#superclasse des usines a vaisseaux, usines a drones, etc.     
class BatimentManufacture():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        
#super-classe des hopitaux, des hotels de ville, des laboratoires, etc.
class BatimentInfrastructure():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        
#super-classe des defenses
class BatimentDefense():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
        self.parent = parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
     
class StationSpatiale(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.planetex = planeteid.x
        self.planetey = planeteid.y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.angle=0
        self.taille = 5
        #======================================================
        """RESSOURCE"""
        self.besoinhumain=50
        self.besoinelectricite= 100
        self.titanium=1000
        """STRUCTURE"""
        self.vie=15000
        self.dommage=50
        self.protection=100
        #======================================================
    
    def orbiter(self):
        self.angle +=1
        if self.angle >= 360:
            self.angle -= 360
        self.x = self.planetex + (self.orbite * math.cos((math.pi *2) * (1.0*self.angle/360.0)))
        self.y = self.planetey +(self.orbite * math.sin((math.pi * 2) * (1.0*self.angle/360.0)))
    
    def AugmenterNiveau(self):
        coutTitanium=10
        if self.nom.ressource - coutTitanium > 0:
            pass
    
    
class Mur(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        print("Objet Mur Creer")
        #======================================================
        """RESSOURCE"""
        self.bois=300
        """STRUCTURE"""
        self.vie= 1000
        self.protection=100 
        #======================================================

class Bouclier(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent=parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        #======================================================
        """RESSOURCE"""
        self.titanium=1000
        self.besoinelectricite=100
        """STRUCTURE"""
        self.vie= 10000
        self.protection=100 
        self.taille=1000
        #======================================================

class Tour(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        #======================================================
        """RESSOURCE"""
        self.bois=300
        self.besoinhumain=10
        """STRUCTURE"""
        self.vie= 1000
        self.dommage=100
        self.protection=100
        #======================================================

class Canon(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        #======================================================
        """RESSOURCE"""
        self.bois=300
        self.besoinhumain=10
        """STRUCTURE"""
        self.vie= 1000
        self.dommage=100
        self.protection=100
        #======================================================
        
        
        
################BATIMENTS RESSOURCES################
class Puit(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "puit"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, Ressource(eau = 5))

class Ferme(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "ferme"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, Ressource(nourriture = 5))

class Mine(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "mine"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, Ressource(bronze = 5))

class CampBucherons(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "campBucherons"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, Ressource(bois = 5))

class CentraleElectrique(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "centraleElectrique"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, Ressource(electricite = 5))
    
################BATIMENTS INFRASTRUCTURES################
class Ville(BatimentInfrastructure):
    def __init__(self, parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu", nomBatiment = "ville"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)
        self.proprietaire=proprio
        self.taille=20
        
class Hopital(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "hopital"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)
        
class Laboratoire(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "laboratoire"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class Ecole(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "ecole"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class Banque(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "banque"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

################BATIMENTS MANUFACTURES################
class UsineVehicule(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVehicule"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class UsineVaisseau(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVaisseau"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class UsineDrone(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineDrone"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)