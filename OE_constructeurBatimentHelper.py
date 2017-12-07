import OE_objetsBatiments
from OE_objetsRessource import Ressource
from DictionnaireCoutAllocationAgeBatiments import dictionnaireCoutAllocationAgeBatiments

class ConstructeurBatimentHelper():
    def __init__(self, parent):
        self.dictionnaire = self.creerDictionnaire()
        self.parent = parent
    
    def creerDictionnaire(self):
        return dictionnaireCoutAllocationAgeBatiments
    
    def construireBatiment(self, ressourcePlanete, ressourceJoueur, nomBatiment):
        ressourceTotal=Ressource()
        ressourceTotal.additionnerRessources(ressourceJoueur)
        ressourceTotal.additionnerRessources(ressourcePlanete)
        
        coutBatiment = self.dictionnaire[nomBatiment][0]
        if(ressourceTotal.estPlusGrandOuEgal(coutBatiment)):
            ressourceJoueur.soustraireRessourcesJoueurETPlanet(ressourcePlanete, coutBatiment)
            return True
        else:
            self.parent.parent.nouveauMessageSystemChat("Pas assez de ressource")
            return False