from helper import Helper as hlp
import math

class Projectile():
    def __init__(self,parent,cible):
        self.parent =parent
        self.cible=cible
        self.type=None
        self.vitesse= 0.05
        self.degat=1+self.parent.attaque
        self.taille=5
        self.x=self.parent.x
        self.y = self.parent.y
        self.positionDepart=self.parent.x,self.parent.y
        self.positionCible=self.cible.x,self.parent.y
        self.couleur="blue"
        self.form="circle"
        self.angleinverse=0
        self.angletrajet=0
        self.temps=0
        
    def avancer(self):
        rep=None
   
        if self.cible!=None:
            
            #print(self.cible.x,self.x,self.cible.y,self.y)
            #print("munition")
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse,self.x,self.y)
            if hlp.calcDistance(int(self.x),int(self.y),int(x),int(y)) <=self.vitesse:
            #if self.x ==x and self.y == y:
                print("cible toucher")
                rep= None
                self.cible.vie = self.cible.vie - self.degat 
                print(self.cible.vie)
                #self.parent.projectile.remove(self)
                #self.base=self.cible
                self.cible=None
            else:
                self.ciblerdestination()  
                
            if self.temps%4==0:
                self.couleur="red"
            else:
                self.couleur="blue"
            self.temps+=1
            return rep
        
    def ciblerdestination(self):
        
        self.angletrajet=hlp.calcAngle(self.x,self.y,self.cible.x,self.cible.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,self.cible.x,self.cible.y)
        