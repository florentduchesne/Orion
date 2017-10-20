class Ressource():
    def __init__(self, electricite = 0, uranium = 0, humain = 0, nourriture = 0, eau = 0, bronze = 0,
                titanium = 0, point_science = 0, allocationHumain = 0, allocationElectricite = 0,
                bois = 0, charbon = 0, metasic = 0, moral = 0):
        self.electricite = electricite
        self.uranium = uranium
        self.humain = humain
        self.nourriture = nourriture
        self.eau = eau
        self.bronze = bronze
        self.titanium = titanium
        self.point_science = point_science
        self.allocationHumain = allocationHumain
        self.allocationElectricite = allocationElectricite
        self.bois = bois
        self.charbon = charbon
        self.metasic = metasic
        self.moral = moral
        
        #self.argent=0
    def estPlusGrandOuEgal(self, ressource):
        if self.electricite < ressource.electricite:# - ressource.allocationElectricite:
            return False
        if self.uranium < ressource.uranium:
            return False
        #if self.humain >= ressource.humain:# - ressource.allocationHumain:
        #    print("elec :")
        #    print(self.electricite)
        #    print(ressource.electricite)
        #    return False
        if self.nourriture < ressource.nourriture:
            return False
        if self.eau < ressource.eau:
            return False
        if self.bronze < ressource.bronze:
            return False
        if self.titanium < ressource.titanium:
            return False
        if self.point_science < ressource.point_science:
            return False
        #if self.allocationElectricite >= ressource.allocationElectricite:
        #    return False
        if self.bois < ressource.bois:
            return False
        if self.charbon < ressource.charbon:
            return False
        if self.metasic < ressource.metasic:
            return False
        if self.moral < ressource.moral:
            return False
        return True
    
    def soustraireRessources(self, ressource):
        self.allocationElectricite += ressource.allocationElectricite
        self.uranium -= ressource.uranium
        self.allocationHumain += ressource.allocationHumain
        self.nourriture -= ressource.nourriture
        self.eau -= ressource.eau
        self.bronze -= ressource.bronze
        self.titanium -= ressource.titanium
        self.point_science -= ressource.point_science
        self.allocationElectricite -= ressource.allocationElectricite
        self.bois -= ressource.bois
        self.charbon -= ressource.charbon
        self.metasic -= ressource.metasic
        self.moral -= ressource.moral
        
    def additionnerRessources(self, ressource):
        self.allocationElectricite -= ressource.allocationElectricite
        self.uranium += ressource.uranium
        self.allocationHumain -= ressource.allocationHumain
        self.nourriture += ressource.nourriture
        self.eau += ressource.eau
        self.bronze += ressource.bronze
        self.titanium += ressource.titanium
        self.point_science += ressource.point_science
        self.allocationElectricite += ressource.allocationElectricite
        self.bois += ressource.bois
        self.charbon += ressource.charbon
        self.metasic += ressource.metasic
        self.moral += ressource.moral
        
class RessourceSpeciale():
    def __init__(self, cellule_mutante = 0, robot_chips = 0, lacrima = 0, nova = 0):
        self.cellule_mutante = cellule_mutante
        self.robot_chips = robot_chips
        self.lacrima = lacrima
        self.nova = nova