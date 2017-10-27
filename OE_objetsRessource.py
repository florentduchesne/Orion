class Ressource():
    def __init__(self, electricite = 0, uranium = 0, humain = 0, nourriture = 0, eau = 0, bronze = 0,
                titanium = 0, point_science = 0, allocationHumain = 0, allocationElectricite = 0,
                bois = 0, charbon = 0, metasic = 0, moral = 0):
        self.dictRess = {}
        self.dictRess["electricite"] = electricite
        self.dictRess["uranium"] = uranium
        self.dictRess["humain"] = humain
        self.dictRess["nourriture"] = nourriture
        self.dictRess["eau"] = eau
        self.dictRess["bronze"] = bronze
        self.dictRess["titanium"] = titanium
        self.dictRess["point_science"] = point_science
        self.dictRess["allocation humain"] = allocationHumain
        self.dictRess["allocation electricite"] = allocationElectricite
        self.dictRess["bois"] = bois
        self.dictRess["charbon"] = charbon
        self.dictRess["metasic"] = metasic
        self.dictRess["moral"] = moral
        
        #self.argent=0
    def estPlusGrandOuEgal(self, ressource):
        
        for cleRess in self.dictRess:
            if self.dictRess[cleRess] < ressource.dictRess[cleRess]:
                return False
        return True
    
    def soustraireRessources(self, ressource):
        for cleRess in self.dictRess:
            self.dictRess[cleRess] -= ressource.dictRess[cleRess]

    def additionnerRessources(self, ressource):
        for cleRess in self.dictRess:
            self.dictRess[cleRess] -= ressource.dictRess[cleRess]
        
class RessourceSpeciale():
    def __init__(self, cellule_mutante = 0, robot_chips = 0, lacrima = 0, nova = 0):
        self.cellule_mutante = cellule_mutante
        self.robot_chips = robot_chips
        self.lacrima = lacrima
        self.nova = nova