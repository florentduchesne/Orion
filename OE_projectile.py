


class Projectile():
    def __init__(self,parent,cible):
        self.parent =parent
        self.cible=cible
        self.type=None
        self.vitesse= 5
        self.degat=5+self.parent.degat
        self.taille=5
        self.positionDepart=self.parent.position
        self.positionCible=self.cible.position
        self.couleur="blue"
        self.form="circle"
        
        