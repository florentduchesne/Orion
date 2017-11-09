from helper import Helper as hlp
import math

class Projectile():
    def __init__(self,parent,cible):
        self.parent =parent
        self.cible=cible
        self.type=None
        self.vitesse= 5
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
        
    def avancer(self):
        rep=None
   
        if self.cible!=None:
            
            #print(self.cible.x,self.x,self.cible.y,self.y)
            print("munition")
            x=self.cible.x
            y=self.cible.y
            self.x,self.y=hlp.getAngledPoint(self.angletrajet,self.vitesse*10,self.x,self.y)
            if hlp.calcDistance(int(self.x),int(self.y),int(x),int(y)) <=self.vitesse:
            #if self.x ==x and self.y == y:
                print("cible toucher")
                rep= None
                self.parent.cibleAttaque.vie = self.parent.cibleAttaque.vie - self.degat 

                self.base=self.cible
                self.cible=None
                
            return rep
        
    def ciblerdestination(self,p):
        self.cible=p
        self.angletrajet=hlp.calcAngle(self.x,self.y,p.x,p.y)
        self.angleinverse=math.radians(math.degrees(self.angletrajet)+180)
        dist=hlp.calcDistance(self.x,self.y,p.x,p.y)
        