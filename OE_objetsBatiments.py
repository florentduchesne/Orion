from OE_objetsRessource import *
import math
from OE_constructeurBatimentHelper import ConstructeurBatimentHelper
from DictionnaireCoutAllocationAgeBatiments import *

#super-classe des mines, camps de bucherons, etc.
class BatimentRessources():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment, production, listeNiveaux = [], proprio = "patate"):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        self.productionRessources = production
        self.listeNiveaux = listeNiveaux
        
    def ameliorer(self, joueur, planete):
        print("AMELIORER DANS OBJ BATIMENT")
        print(self.listeNiveaux)
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.ressource, joueur.ressources, nouveauNom)
            if(planeteAAssezDeRessources):
                self.nomBatiment = nouveauNom
                self.listeNiveaux.remove(self.nomBatiment)
                print("assez de ressources pour l'amelioration")
                self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment)
        else:
            print("PLUS D'AMÉLIORATIONS DISPONIBLES")
        
#superclasse des usines a vaisseaux, usines a drones, etc.     
class BatimentManufacture():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment, listeNiveaux = [], proprio = "patate"):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        self.listeNiveaux = listeNiveaux
        
    def ameliorer(self, joueur, planete):
        print("AMELIORER DANS OBJ BATIMENT")
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.ressource, joueur.ressources, nouveauNom)
            if(planeteAAssezDeRessources):
                self.nomBatiment = nouveauNom
                self.listeNiveaux.remove(self.nomBatiment)
                print("assez de ressources pour l'amelioration")
                self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment)
        else:
            print("PLUS D'AMÉLIORATIONS DISPONIBLES")
        
#super-classe des hopitaux, des hotels de ville, des laboratoires, etc.
class BatimentInfrastructure():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment, listeNiveaux = [], proprio = "patate"):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.nomBatiment = nomBatiment
        self.listeNiveaux = listeNiveaux
        
    def ameliorer(self, joueur, planete):
        print("AMELIORER DANS OBJ INFRASTRUCTURE")
        print(self.listeNiveaux)
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.ressource, joueur.ressources, nouveauNom)
            if(planeteAAssezDeRessources):
                self.nomBatiment = nouveauNom
                self.listeNiveaux.remove(self.nomBatiment)
                print("assez de ressources pour l'amelioration")
                self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment)
        else:
            print("PLUS D'AMÉLIORATIONS DISPONIBLES")
        
#super-classe des defenses
class BatimentDefense():
    def __init__(self,parent,nom,idSysteme, planeteid,x,y, idSuivant, nomBatiment, listeNiveaux = [], proprio = "patate"):
        self.parent = parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.planeteid=planeteid
        self.systemeid=idSysteme
        self.nomBatiment = nomBatiment
        self.listeNiveaux = listeNiveaux
        self.proprio = proprio
        
    def ameliorer(self, joueur, planete):
        print("AMELIORER DANS OBJ BATIMENT")
        print(self.listeNiveaux)
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.ressource, joueur.ressources, nouveauNom)
            if(planeteAAssezDeRessources):
                self.nomBatiment = nouveauNom
                self.listeNiveaux.remove(self.nomBatiment)
                print("assez de ressources pour l'amelioration")
                joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment)
        else:
            print("PLUS D'AMÉLIORATIONS DISPONIBLES")
     
class StationSpatiale():
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y, couleurJoueur,planete, proprio = "patate"):
        #BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=idSysteme
        self.base=systeme
        self.angle=0
        self.taille = ((planete.taille * 100) / 4)
        self.planetex = self.x
        self.planetey = self.y
        self.orbite = planete.taille + 0.3
        self.couleurJoueur = couleurJoueur
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
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "mur", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, listeNiveaux=[])
        print("Objet Mur Creer")
        #======================================================
        """RESSOURCE"""
        self.bois=300
        """STRUCTURE"""
        self.vie= 1000
        self.protection=100 
        #======================================================

class Bouclier(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "bouclier", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, listeNiveaux=[])
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
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "tour", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, listeNiveaux=[])
        #======================================================
        """RESSOURCE"""
        self.bois=300
        self.besoinhumain=10
        """STRUCTURE"""
        self.vie= 1000
        self.dommage=100
        self.protection=100
        #======================================================

class Canon(BatimentDefense):#self,parent,nom,systeme,idSuivant,idSysteme,x,y, nomBatiment, listeNiveaux = [], proprio = "patate"):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "canon", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, listeNiveaux=["Canon_Ion","Canon_Acid"])
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
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "puit", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Puit2", "Puit3"])

class Ferme(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "ferme", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Ferme2", "Ferme3"])

class Mine(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "mine", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Mine2", "Mine3"])

class CampBucherons(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "campBucherons", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Camp_Bucherons2", "Camp_Bucherons3"])

class CentraleElectrique(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "centraleElectrique", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Centrale_Nucleaire", "Eolienne", "PanneauSolaire"])
    
################BATIMENTS INFRASTRUCTURES################
class Ville(BatimentInfrastructure):
    def __init__(self, parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu", nomBatiment = "ville"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)
        self.proprietaire=proprio
        self.taille=20
        
class Hopital(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "hopital", proprio = "patate"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)
        
class Laboratoire(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "laboratoire", proprio = "patate"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class Ecole(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "ecole", proprio = "patate"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class Banque(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "banque", proprio = "patate"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

################BATIMENTS MANUFACTURES################
class UsineVehicule(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVehicule", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class UsineVaisseau(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVaisseau", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)

class UsineDrone(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineDrone", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment)