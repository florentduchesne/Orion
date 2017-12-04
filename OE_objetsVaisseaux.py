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
        self.taille=32
        self.base=systeme
        self.angletrajet=0
        self.angleinverse=0
        self.x=x-1
        self.y=y-1
        self.taille=30
        self.vitesse=random.choice([0.001,0.003,0.005,0.01])*5 #0.5
        self.cible=None
        self.vie = 100 
        self.niveau = 1 # niveau
        self.idSysteme =idSysteme
        self.dansGalaxie = False
        self.range = 3 #temporaire
        self.dansVaisseauMere = False

    def initialisation(self):
        if self.niveau>1 :
            for ame in range(self.niveau):
                ame.augmentation

    def avancer(self):
        rep=None
        if self.cible and isinstance(self.cible, Systeme): #Deplacement dans la galaxie
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse/2.5,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                rep=self.cible
                self.base=self.cible
                self.cible=None
            return rep
        
        elif self.cible and isinstance(self.cible, Planete): #deplacement dans un système
            x=self.cible.x
            y=self.cible.y
            self.angletrajet = hlp.calcAngle(self.x,self.y,x,y)
            
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y)-1 <=self.vitesse:#si le vaisseau est arrivé
                rep=self.cible
                self.base=self.cible
                if(isinstance(self, VaisseauColonisation)):
                    if not self.dansVaisseauMere :  
                        print("ceci est un vaisseau colonisateur")
                        if self.cible.coloniser(self.proprietaire):
                            #self.parent.systemesvisites.append(Systeme)
                            return "colonisation"
                self.cible=None
            return rep#on retourne la cible
        elif self.cible and isinstance(self.cible, Vaisseau):
            x=self.cible.x
            y=self.cible.y
            self.angletrajet = hlp.calcAngle(self.x,self.y,x,y)
            if self.dansGalaxie == False:
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            else:
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse/2.5,self.x,self.y)
            if hlp.calcDistance(self.x,self.y,x,y)-1 <=self.vitesse:
                if isinstance(self.cible, VaisseauMere):
                        self.cible.RemplirVaisseau(self)
                        rep=self.cible
                        self.base=self.cible
                        self.cible=None
            return rep
        elif self.cible!=None:
            x=self.cible.x
            y=self.cible.y
            if self.dansGalaxie == False:
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            else:
                self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse/2.5,self.x,self.y)
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
    
    def augmentation(self) :
        self.niveau += 1

    
class VaisseauAttaque(Vaisseau):
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats,portee,typeVaisseau):
        Vaisseau.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,typeVaisseau)
        self.attaque = Degats
        self.range = portee
        self.enAttaque=False
        self.augmentationDomamage = 2
        self.augmentationVie = 2
        self.augmentationPortee = 1
        self.listeCibleAttaquer=[]
        self.listeCibleAttaquerStation=[]
        self.cibleAttaque= None
        self.attaque = 1
        self.projectile=[]
        self.tempsRecharge=0
            
        

    def attaquer(self):       
        if self.cibleAttaque.vie>0:
            self.enAttaque=True

            if self.tempsRecharge==0:
                p=Projectile(self,self.cibleAttaque,0.05)
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
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau,maxVaisseau):
        VaisseauAttaque.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau)
        self.maxVaisseau = maxVaisseau
        self.systemePresent = self.base
        self.attaque = 15
        self.vie = self.vie * 2
        self.vitesse = 0.01*5
        self.augmentationCargo = 1
        self.augmentationPortee = 1
        self.augmentationVie = 1
        self.augmentationAttaque = 1
        self.vaisseau = []
    
    def RemplirVaisseau(self, vaisseauaAjouter):
        self.vaisseauaAjouter = vaisseauaAjouter
        if not isinstance(self.vaisseauaAjouter, VaisseauMere):
            if self.maxVaisseau > len(self.vaisseau) :
                self.vaisseau.append(self.vaisseauaAjouter)
                self.vaisseauaAjouter.dansVaisseauMere = True
                self.vaisseauaAjouter.x = None
                self.vaisseauaAjouter.y = None
                
            else : 
                print ("Vaisseau Mere Plein")
        else :
            ("un vaisseau Mere ne peut pas rentre dans un autre vaisseau Mere")
    
    def SortirVaisseau (self) :
        print ("allo")
        if not self.dansGalaxie:
            print("ici")
            for v in range (len(self.vaisseau)):
                print("pas de probleme")
                self.vaisseau[v].dansVaisseauMere = False
                self.vaisseau[v].idSysteme = self.idSysteme
                self.vaisseau[v].x = self.x + v
                self.vaisseau[v].y = self.y + v
                self.vaisseau[v] = []
        else :
            print("Le vaisseau Mere peut se vider que dans un systeme")
    
    def augmentation(self) :
        self.niveau += 1
        if self.niveau%2 :
            self.vie +=self.augmentationVie
            self.attaque+=self.augmentationAttaque
        else :
            self.maxVaisseau += self.augmentationCargo
            
        if self.niveau%5 == 0:
            self.portee+=self.augmentationPortee
            

class VaisseauChasseur(VaisseauAttaque):
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau):
        VaisseauAttaque.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau)
        self.attaque =  self.attaque+20
        self.vitesse = 0.005*5

    
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
    def __init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau):
        VaisseauAttaque.__init__(self,parent,nom,systeme,idSuivant,idSysteme,x,y,Degats, portee,typeVaisseau)
        self.attaque =  self.attaque+15
        self.vie = self.vie + 50
        self.vitesse = 0.003*5
        self.portee = portee + 5
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

      

