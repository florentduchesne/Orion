import random
from helper import Helper as hlp
import math
from OE_objets import *
from OE_projectile import *
from numpy.distutils.fcompiler import none

class Vaisseau():
    def __init__(self,parent,nom,systeme,idSuivant,niveau):
        self.parent=parent
        self.id=idSuivant
        self.proprietaire=nom
        self.taille=16
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=5
        self.y=5
        self.taille=16
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None
        self.vie = 100 
        self.niveau = niveau
        
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
            print(self.cible.x,self.x,self.cible.y,self.y)

            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
            
#        else:
 #           print(self.cible.x,self.x,self.cible.y,self.y)
  #          x=self.cible.x
   #         y=self.cible.y
    #        self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
     #       if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
      #          rep= None
       #         self.base=self.cible
        #        self.cible=None
         #   return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        #print("Distance",dist," en ", int(dist/self.vitesse))
    
    def augmentation(self) :
        self.niveau += 1
            
class VaisseauAttaque(Vaisseau):
    def __init__(self, Degats, portee):
        self.dommage = Degats
        self.range = portee
        self.cibleAttaque=None 
        self.enAttaque=False
        self.listeCibleAttaquer=[]
            
        
    def attaquer(self):       
        if self.cibleAttaque.vie>0:
            #print(self.cibleAttaque.vie)
            self.enAttaque=True
            protile = Projectile(self,self.cibleAttaque)
            self.cibleAttaque.vie = self.cibleAttaque.vie - protile.degat 
        else: 
            #print("retirer cible")
            self.enAttaque=False         
            #self.cibleAttaque.proprietaire="inconnu"
            self.listeCibleAttaquer.remove(self.cibleAttaque)

            self.cibleAttaque=None  
            self.planetteCible=None 
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2:
            self.dommage += 2      
        else :
            self.vie +=2
      
        if self.niveau%5 == 0:
            self.portee+=1
            
            
class VaisseauCommercial(Vaisseau):
    def __init__(self, max):
        self.ressource = Ressource()
        self.maxRessource = max
        self.vitesse = 0.001*5
        
    def RemplirVaisseau(self, ressource, quantite):
        pass
    
    def EchangerRessource(self,ressource, quantite):
        pass
    
    def augmentation (self):
        self.niveau += 1
        if self.niveau%2:
            self.maxRessources += 5
        if self.niveau%5 == 0:
            self.portee+=1

class VaisseauNova(Vaisseau):
    def __init__(self):
        self.nova = none
        self.vitesse = 0.01*5
    
    def RecolterNova(self):
        self.nova += 1
        
class VaisseauColonisation(Vaisseau):
    def __init__(self,maxPersonne, maxAliments):
        self.maxPersonnes = maxPersonne
        self.nbPersonne = 0
        self.maxAliments = maxAliments
        self.aliments = 0
        self.vie += self.vie+ 50
        self.vitesse = 0.003*5
        
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
            self.maxAliments +=1
        else :
            self.maxPersonnes +=1
            
        if self.niveau%5 == 0:
            self.portee+=1
        
class VaisseauSuicide(Vaisseau):
    def __init__(self, portee):
        self.dommage = 100
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
    
    def RemplirVaisseau(self):
        pass
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2 :
            self.vie +=1
            self.attaque+=1
        else :
            self.maxVaisseau +=1
            
        if self.niveau%5 == 0:
            self.portee+=1
            

class VaisseauChaseur(VaisseauAttaque):
    def __init__(self):
        self.attaque = 20
        self.vitesse = 0.001*5

    
class VaisseauBombarde(VaisseauAttaque):
    def __init__(self):
        self.attaque = 30
        self.vitesse = 0.005*5
        self.portee = self.portee + 5

class VaisseauLaser(VaisseauAttaque):
    def __init__(self):
        self.attaque = 45
        self.vitesse = 0.01*5
        self.portee = self.portee + 10
    
class VaisseauTank(VaisseauAttaque):
    def __init__(self):
        self.attaque = 15
        self.vie = self.vie + 50
        self.vitesse = 0.003*5
        self.portee = self.portee + 5
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2:
            self.dommage += 2
        if self.niveau%5 == 0:
            self.portee+=1
            
        self.vie += 2

      

