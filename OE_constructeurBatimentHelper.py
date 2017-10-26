import OE_objetsBatiments
from DictionnaireCoutAllocationAgeBatiments import dictionnaireCoutAllocationAgeBatiments

class ConstructeurBatimentHelper():
    def __init__(self):
        self.dictionnaire = self.creerDictionnaire()
    
    def creerDictionnaire(self):
        return dictionnaireCoutAllocationAgeBatiments
    
    def construireBatiment(self, ressourceJoueur, nomBatiment):
        coutBatiment = self.dictionnaire[nomBatiment][0]
        if(ressourceJoueur.estPlusGrandOuEgal(coutBatiment)):
            ressourceJoueur.soustraireRessources(coutBatiment)
            print("assez de ressources")
            return True
        else:
            print("pas assez de ressources")
            print("cout : ")
            print(coutBatiment)
            print("ressources disponibles :")
            print(ressourceJoueur)
            return False