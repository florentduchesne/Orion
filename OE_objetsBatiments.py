from OE_objetsRessource import *
import math
from OE_constructeurBatimentHelper import ConstructeurBatimentHelper
from DictionnaireCoutAllocationAgeBatiments import *
from OE_projectile import *

def verifierSiJoueurAUneVilleSurLaPlanete(joueur, planete):
    print("joueur qui améliore: " + joueur.nom)
    for infra in planete.infrastructures:
        if isinstance(infra, Ville):
            print("infra proprio" + infra.proprietaire)
            if infra.proprietaire == joueur.nom:
                print("le batiment vous appartient")
                return True
    return False
        

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
        self.proprietaire = proprio
        self.vie = 100
        self.humains = 0
        
    def recalculerProduction(self):
        for ressource in self.productionRessources.dictRess:
            self.productionRessources.dictRess[ressource] *= 1.0 + (float(self.humains) * 0.1)
        
    def ajouterHumain(self, joueur, planete):
        if planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] >= 1:
            planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] -= 1
            self.humains += 1
            self.recalculerProduction()
        elif joueur.ressources.dictRess["humain"] >= 1:
            joueur.ressources.dictRess["humain"] -= 1
            self.humain += 1
            self.recalculerProduction()
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucun humain disponible")
            
        
    def ameliorer(self, joueur, planete):
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            if verifierSiJoueurAUneVilleSurLaPlanete(joueur, planete):
                planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.dicRessourceParJoueur[joueur.nom], joueur.ressources, nouveauNom)
                if(planeteAAssezDeRessources):
                    joueur.parent.parent.effacerBatiment(self.planeteid, self.nomBatiment, self.id)
                    self.nomBatiment = nouveauNom
                    self.listeNiveaux.remove(self.nomBatiment)
                    joueur.parent.parent.nouveauMessageSystemChat("Bâtiment amélioré!")
                    self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                    joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment, self.id)
                    self.vie *= 2
                    self.recalculerProduction()
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucune amélioration possible!")
        
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
        self.proprietaire = proprio
        self.vie = 100
        
    def recalculerProduction(self):
        for ressource in self.productionRessources.dictRess:
            ressource *= 1 + (self.humains * 0.1)
        
    def ajouterHumain(self, joueur, planete):
        if planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] >= 1:
            planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] -= 1
            self.humains += 1
            self.recalculerProduction()
        elif joueur.dicRessourceParJoueur[joueur.nom].dictRess["humain"] >= 1:
            joueur.dicRessourceParJoueur[joueur.nom].dictRess["humain"] -= 1
            self.humain += 1
            self.recalculerProduction()
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucun humain disponible")
        
    def ameliorer(self, joueur, planete):
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            if verifierSiJoueurAUneVilleSurLaPlanete(joueur, planete):
                planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.dicRessourceParJoueur[joueur.nom], joueur.ressources, nouveauNom)
                if(planeteAAssezDeRessources):
                    joueur.parent.parent.effacerBatiment(self.planeteid, self.nomBatiment, self.id)
                    self.nomBatiment = nouveauNom
                    self.listeNiveaux.remove(self.nomBatiment)
                    joueur.parent.parent.nouveauMessageSystemChat("Bâtiment amélioré!")
                    self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                    joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment, self.id)
                    self.vie *= 2
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucune amélioration possible!")
        
#super-classe des hopitaux, des hotels de ville, des laboratoires, etc.
class BatimentInfrastructure():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment, productionRessources, listeNiveaux = [], proprio = "patate"):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
        self.productionRessources = productionRessources
        self.nomBatiment = nomBatiment
        self.listeNiveaux = listeNiveaux
        self.proprietaire = proprio
        self.vie = 100
        
    def recalculerProduction(self):
        for ressource in self.productionRessources.dictRess:
            print("ancienne production : " + str(self.productionRessources.dictRess[ressource]))
            self.productionRessources.dictRess[ressource] *= 1.0 + (float(self.humains) * 0.1)
            print("nouvelle production : " + str(self.productionRessources.dictRess[ressource]))
        
    def ajouterHumain(self, joueur, planete):
        if planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] >= 1:
            planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] -= 1
            self.humains += 1
            self.recalculerProduction()
        elif joueur.ressources.dictRess["humain"] >= 1:
            joueur.ressources.dictRess["humain"] -= 1
            self.humain += 1
            self.recalculerProduction()
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucun humain disponible")
        
    def ameliorer(self, joueur, planete):
        if(len(self.listeNiveaux) > 0):
            nouveauNom = self.listeNiveaux[0]
            if verifierSiJoueurAUneVilleSurLaPlanete(joueur, planete):
                planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.dicRessourceParJoueur[joueur.nom], joueur.ressources, nouveauNom)
                if(planeteAAssezDeRessources):
                    joueur.parent.parent.effacerBatiment(self.planeteid, self.nomBatiment, self.id)
                    self.nomBatiment = nouveauNom
                    self.listeNiveaux.remove(self.nomBatiment)
                    joueur.parent.parent.nouveauMessageSystemChat("Bâtiment amélioré!")
                    #self.productionRessources = dictionnaireProductionRessources[self.nomBatiment]
                    joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment, self.id)
                    self.vie *= 2
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucune amélioration possible!")
        
#super-classe des defenses
class BatimentDefense():
    def __init__(self,parent,nom,idSysteme, planeteid,x,y, idSuivant, nomBatiment, vie, listeNiveaux = [], proprio = "patate"):
        self.parent = parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.planeteid=planeteid
        self.systemeid=idSysteme
        self.nomBatiment = nomBatiment
        self.listeNiveaux = listeNiveaux
        self.proprietaire = proprio
        self.vie = vie
        self.productionRessources = Ressource()
        
    def recalculerProduction(self):
        for ressource in self.productionRessources.dictRess:
            print("ancienne production : " + str(self.productionRessources.dictRess[ressource]))
            self.productionRessources.dictRess[ressource] *= 1.0 + (float(self.humains) * 0.1)
            print("nouvelle production : " + str(self.productionRessources.dictRess[ressource]))
        
    def ajouterHumain(self, joueur, planete):
        if planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] >= 1:
            planete.dicRessourceParJoueur[joueur.nom].dictRess["humain"] -= 1
            self.humains += 1
            self.recalculerProduction()
        elif joueur.ressources.dictRess["humain"] >= 1:
            joueur.ressources.dictRess["humain"] -= 1
            self.humain += 1
            self.recalculerProduction()
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucun humain disponible")
        
    def ameliorer(self, joueur, planete):
        if verifierSiJoueurAUneVilleSurLaPlanete(joueur, planete):
            if(len(self.listeNiveaux) > 0):
                nouveauNom = self.listeNiveaux[0]
            
                planeteAAssezDeRessources = joueur.parent.constructeurBatimentHelper.construireBatiment(planete.dicRessourceParJoueur[joueur.nom], joueur.ressources, nouveauNom)
                if(planeteAAssezDeRessources):
                    joueur.parent.parent.effacerBatiment(self.planeteid, self.nomBatiment, self.id)
                    self.nomBatiment = nouveauNom
                    self.listeNiveaux.remove(self.nomBatiment)
                    joueur.parent.parent.nouveauMessageSystemChat("Bâtiment amélioré!")
                    joueur.parent.parent.afficherBatiment(joueur.nom,self.systemeid,self.planeteid,self.x,self.y, self.nomBatiment, self.id)
                    self.vie *= 2
        else:
            joueur.parent.parent.nouveauMessageSystemChat("Aucune amélioration possible!")
     
class StationSpatiale():
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y, couleurJoueur,planete, proprio = "patate"):
        #BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.proprietaire = proprio
        self.systemeid=idSysteme
        self.base=systeme
        self.angle=0
        self.taille = ((planete.taille * 100) / 4)
        self.planetex = self.x
        self.planetey = self.y
        self.orbite = planete.taille + 0.3
        self.couleurJoueur = couleurJoueur
        
        
        """variable pour attaque"""
        
        self.listeCibleAttaquer=[]
        self.cibleAttaque= None
        self.attaque = 2
        self.projectile=[]
        self.tempsRecharge=0
        self.range=5
        #======================================================
        """RESSOURCE"""
        self.besoinhumain=50
        self.besoinelectricite= 100
        self.titanium=1000

        """STRUCTURE"""
        self.vie=300
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

    def attaquer(self):       
        if self.cibleAttaque.vie>0:
            self.enAttaque=True
            
            if self.tempsRecharge==0:
                
                p=Projectile(self,self.cibleAttaque,0.05)
                self.projectile.append(p)
                p.ciblerdestination()
                self.tempsRecharge=15
            else:
                self.tempsRecharge=self.tempsRecharge-1
            

        else: 
            self.enAttaque=False         
            self.listeCibleAttaquer.remove(self.cibleAttaque)
            
            self.cibleAttaque=None  
            
class Mur(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "mur", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, 1000, listeNiveaux=[], proprio = proprio)
        #======================================================
        """STRUCTURE"""
        self.protection=100 
        #======================================================

class Bouclier(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant, nomBatiment = "bouclier", proprio = "patate"):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, 250, listeNiveaux=[], proprio = proprio)
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
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, 200, listeNiveaux=[], proprio = proprio)
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
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant, nomBatiment, 150, listeNiveaux=["Canon_Ion","Canon_Acid"], proprio = proprio)
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
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Puit2"], proprio = proprio)

class Ferme(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "ferme", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Ferme2", "Ferme3"], proprio = proprio)

class Mine(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "mine", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Mine2", "Mine3"], proprio = proprio)

class CampBucherons(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "campBucherons", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Camp_Bucherons2", "Camp_Bucherons3"], proprio = proprio)

class CentraleElectrique(BatimentRessources):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "Centrale_Charbon", proprio = "patate"):
        BatimentRessources.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], listeNiveaux = ["Centrale_Nucleaire", "Grosse_Centrale_Nucleaire", "Eolienne", "Panneau_Solaire"], proprio = proprio)
    
################BATIMENTS INFRASTRUCTURES################
class Ville(BatimentInfrastructure):#self, proprio.nom, self.id, planeteProprio.id, self.parent.createurId.prochainid()
    def __init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment = "Ville", proprio="inconnu"):
        print("ressource")
        print(dictionnaireProductionRessources[nomBatiment].dictRess["humain"])
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, "Ville", dictionnaireProductionRessources[nomBatiment], listeNiveaux=["Ville2", "Ville3"], proprio=proprio)
        self.taille=20

class Banque(BatimentInfrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "Banque", proprio = "patate"):
        BatimentInfrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, dictionnaireProductionRessources[nomBatiment], proprio = proprio)

################BATIMENTS MANUFACTURES################
class UsineVehicule(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVehicule", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, proprio = proprio)

class UsineVaisseau(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineVaisseau", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, proprio = proprio)

class UsineDrone(BatimentManufacture):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant, nomBatiment = "usineDrone", proprio = "patate"):
        BatimentManufacture.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant, nomBatiment, proprio = proprio)