import random
from helper import Helper as hlp
import math
from OE_objets import *
from OE_projectile import *
from numpy.distutils.fcompiler import none

class Vaisseau():
    #self, parent, nom, systemeid, planeteid, x, y, idsuivant
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,typeVaisseau):#,niveau):
        self.parent=parent
        self.id=idSuivant
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=x-1
        self.y=y-1
        self.taille=30
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None
        self.vie = 100 
        self.niveau =1 # niveau
        self.idSysteme =idSysteme
        self.dansGalaxie = False
        self.range = 3 #temporaire

    def initialisation(self):
        if self.niveau>1 :
            for ame in range(self.niveau):
                ame.augmentation
        
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
            # print(self.cible.x,self.x,self.cible.y,self.y)
            x=self.cible.x
            y=self.cible.y
            self.angletrajet = hlp.calcAngle(self.x,self.y,x,y)
            
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y)-1 <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        elif self.cible and isinstance(self.cible, Vaisseau):
            x=self.cible.x
            y=self.cible.y
            self.angletrajet = hlp.calcAngle(self.x,self.y,x,y)
            
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y)-1 <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                #self.cible=None
            return rep
        elif self.cible!=None:
           # print(self.cible.x,self.x,self.cible.y,self.y)
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(int(self.x),int(self.y),int(x),int(y)) <=self.vitesse:
            #if self.x ==x and self.y == y:
                rep= None
                self.base=self.cible
                self.cible=None
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
    
    def augmentation(self) :
        self.niveau += 1

    
class VaisseauAttaque(Vaisseau):
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats,portee,typeVaisseau):
        Vaisseau.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,typeVaisseau)
        self.attaque = Degats
        self.range = portee
        self.cibleAttaque=None 
        self.enAttaque=False
        self.listeCibleAttaquer=[]
        self.augmentationDomamage = 2
        self.augmentationVie = 2
        self.augmentationPortee = 1
        self.listeCibleAttaquer=[]
        self.cibleAttaque= None
        self.attaque = 1
        self.projectile=[]
        self.tempsRecharge=0
            
        

    def attaquer(self):       
        if self.cibleAttaque.vie>0:
            self.enAttaque=True

            if self.tempsRecharge==0:
                p=Projectile(self,self.cibleAttaque)
                self.projectile.append(p)
                p.ciblerdestination()
                self.tempsRecharge=10
            else:
                self.tempsRecharge=self.tempsRecharge-1
            

        else: 
            self.enAttaque=False         
            self.listeCibleAttaquer.remove(self.cibleAttaque)
            
            self.cibleAttaque=None  

    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2:
            self.dommage += self.augmentationDomamage     
        else :
            self.augmentationVie
      
        if self.niveau%5 == 0:
            self.portee+=self.augmentationPortee
            
            
class VaisseauCommercial(Vaisseau):
    def __init__(self, max):
        self.ressource = Ressource()
        self.maxRessource =max
        self.vitesse = 0.001*5
        self.AugmentationRessource = 5
        
    def RemplirVaisseau(self, ressource, quantite):
        pass
    
    def EchangerRessource(self,ressource, quantite):
        pass
    
    def augmentation (self):
        self.niveau += 1
        if self.niveau%2:
            self.maxRessources += self.AugmentationRessource
      

class VaisseauNova(Vaisseau):
    def __init__(self):
        self.nova = 0
        self.vitesse = 0.01*5
     
    def RecolterNova(self):
        self.nova += 1
        
class VaisseauColonisation(Vaisseau):
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,maxPersonne, maxAliments,typeVaisseau):
        Vaisseau.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,typeVaisseau)
        self.maxPersonnes = maxPersonne
        self.nbPersonne = 0
        self.maxAliments = maxAliments
        self.aliments = 0
        self.vie += self.vie+ 50
        self.vitesse = 0.003*5
        self.augmentationAliments = 1
        self.augmentationPersonne = 1
        
    def AjouterPersonne (self, nombre):
        if self.nbPersonne+nombre < self.maxPersonne:
            self.nbPersonne = self.nbPersonne + nombre
    
    def AjouterAliments (self, nombre):   
        if self.aliments+nombre < self.maxAliments:
            self.aliments = self.aliments + nombre
            
    def DevenirVille (self, planete):
        pass
    
    def augmentation(self):
        self.niveau += 1
        if self.niveau%2:
            self.maxAliments +=self.augmentationAliments
        else :
            self.maxPersonnes +=self.augmentationPersonne
        
        
class VaisseauSuicide(Vaisseau):
    def __init__(self, portee):
        self.attaque = 100
        self.vie = 50
        self.vitesse = 0.003*5
        self.portee = portee
    
    def AutoDesctruction(self): 
        pass
    
class VaisseauBiologique(Vaisseau):
    def __init__(self, maladie):
        self.maladie = maladie
        self.vitesse = 0.005*5
        
    def IncuberMaladie(self):
        pass
    
    def Contaminer(self):
        pass
        
class VaisseauMere(VaisseauAttaque):
    def __init__(self, maxVaisseau):
        self.maxVaisseau = maxVaisseau
        self.systemePresent = self.base
        self.attaque = 15
        self.vie = self.vie * 2
        self.vitesse = 0.01*5
        self.augmentationCargo = 1
        self.augmentationPortee = 1
        self.augmentationVie = 1
        self.augmentationAttaque = 1
    
    def RemplirVaisseau(self):
        pass
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2 :
            self.vie +=self.augmentationVie
            self.attaque+=self.augmentationAttaque
        else :
            self.maxVaisseau += self.augmentationCargo
            
        if self.niveau%5 == 0:
            self.portee+=self.augmentationPortee
            

class VaisseauChaseur(VaisseauAttaque):
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau):
        VaisseauAttaque.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau)
        self.attaque =  self.attaque+20
        self.vitesse = 0.001*5

    
class VaisseauBombarde(VaisseauAttaque):
    def __init__(self):
        self.attaque =  self.attaque+30
        self.vitesse = 0.005*5
        self.portee = self.portee + 5

class VaisseauLaser(VaisseauAttaque):
    def __init__(self):
        self.attaque = self.attaque+45
        self.vitesse = 0.01*5
        self.portee = self.portee + 10
    
class VaisseauTank(VaisseauAttaque):
    def __init__(self):
        self.attaque =  self.attaque+15
        self.vie = self.vie + 50
        self.vitesse = 0.003*5
        self.portee = self.portee + 5
        self.augmentationPortee = 1
        self.augmentationVie = 2
        self.augmentationAttaque = 1
        
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2:
            self.attaque += self.augmentationAttaque
        if self.niveau%5 == 0:
            self.portee+=self.augmentationPortee
            
        self.vie += self.augmentationVie

      

