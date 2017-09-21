class Infrastructure():
    def __init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant):
        self.parent=parent
        self.id=idSuivant
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid

class Ville(Infrastructure):
    def __init__(self, parent, nom, systemeid, planeteid, idSuivant, x = 2500, y = 2500, proprio="inconnu"):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.parent=parent
        self.id=self.parent.parent.parent.createurId.prochainid()
        self.x=x
        self.y=y
        self.proprietaire=proprio
        self.taille=20
               
class Mine(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.entrepot=0
        self.besoinhumain=5
        self.besoinelectricite=5
        
    def detruireMine(self):
        self.ressource.Humain+self.besoinhumain
        self.ressource.Electricite+self.besoinelectricite
        
class Ferme(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.entrepot=0
        self.besoinhumain=5
        self.besoinelectricite=5
        
class Hopital(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.bonheurProduit = 5
        
class Laboratoire(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)