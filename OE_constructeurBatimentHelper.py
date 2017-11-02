import OE_objetsBatiments
from OE_objetsRessource import Ressource
from DictionnaireCoutAllocationAgeBatiments import dictionnaireCoutAllocationAgeBatiments

class ConstructeurBatimentHelper():
    def __init__(self):
        self.dictionnaire = self.creerDictionnaire()
    
    def creerDictionnaire(self):
        return dictionnaireCoutAllocationAgeBatiments
    
    def construireBatiment(self, ressourcePlanete, ressourceJoueur, nomBatiment):
        ressourceTotal=Ressource()
        ressourceTotal.additionnerRessources(ressourceJoueur)
        ressourceTotal.additionnerRessources(ressourcePlanete)
        
        coutBatiment = self.dictionnaire[nomBatiment][0]
        if(ressourceTotal.estPlusGrandOuEgal(coutBatiment)):
            ressourceJoueur.soustraireRessourcesJoueurETPlanet(ressourcePlanete, coutBatiment)
            print("assez de ressources")
            return True
        else:
            print("pas assez de ressources")
            print("cout : ")
            print(coutBatiment)
            print("ressources disponibles :")
            print(ressourcePlanete)
            return False