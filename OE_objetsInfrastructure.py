<<<<<<< HEAD
import OE_objetsRessource

######Batiment_Ressources#########
class Batiment_Ressources():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
=======
class BatimentDefense():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
        self.parent = parent
        self.id=idsuivant
>>>>>>> a71dd3566409c782703929bb880c845037ce6c84
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
<<<<<<< HEAD
        self.CoutRessourcesAmelioration
"""
class Mine():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        #self.productionRessource = Ressource()
        self.multiplicateur = 1.1
        self.besoinhumain=5
        self.besoinelectricite=5
        
    def detruireMine(self):
        self.ressource.Humain+self.besoinhumain;
        self.ressource.Electricite+self.besoinelectricite;
"""
######Batiment_Manifacture#########
class Batiment_Manifacture():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
=======
     
class StationSpatiale(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
>>>>>>> a71dd3566409c782703929bb880c845037ce6c84
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
<<<<<<< HEAD

######Batiment_Infrastructure#########
class Batiment_Infrastructure():
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        self.parent=parent
        self.id=idSuivant
=======
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
    
    def AugmenterNiveau(self):
        coutTitanium=10
        if self.nom.ressource - coutTitanium > 0:
            pass
    
    
class Mur(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
        BatimentDefense.__init__(self, parent, nom, systemeid, planeteid, x, y, idsuivant)
        self.parent = parent
        self.id=idsuivant
>>>>>>> a71dd3566409c782703929bb880c845037ce6c84
        self.x=x
        self.y=y
        self.systemeid=systemeid
        self.planeteid=planeteid
<<<<<<< HEAD
"""
class Ville(Batiment_Infrastructure):
    def __init__(self,parent,nom, systemeid, planeteid, idSuivant, x=2500,y=2500, proprio="inconnu"):
        Batiment_Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.parent=parent
        self.id=self.parent.parent.parent.createurId.prochainid()
        self.x=x
        self.y=y
        self.proprietaire=proprio
        self.taille=20
        self.type = "Ville"
               
"""

























=======
        #======================================================
        """RESSOURCE"""
        self.bois=300
        """STRUCTURE"""
        self.vie= 1000
        self.protection=100 
        #======================================================

class Bouclier(BatimentDefense):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
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
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
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
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idsuivant):
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
        
        
>>>>>>> a71dd3566409c782703929bb880c845037ce6c84
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
    """  
class Hopital(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
        self.bonheurProduit = 5
        
class Laboratoire(Infrastructure):
    def __init__(self,parent,nom,systemeid,planeteid,x,y,idSuivant):
        Infrastructure.__init__(self, parent, nom, systemeid, planeteid, x, y, idSuivant)
"""