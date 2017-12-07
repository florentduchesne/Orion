from OE_objetsRessource import Ressource

#Dictionnaire Des couts, d'allocation et de l'age.
# Exemple d'utilisation
# dictionaireCouteAllocationAgeBatiments["Mine"][0] C'est le cout
# dictionaireCouteAllocationAgeBatiments["Mine"][1] C'est l'allocation maximum du batiment
# dictionaireCouteAllocationAgeBatiments["Mine"][2] C'est l'age requis, l'age 1 est celle de base

dictionnaireCoutAllocationAgeBatiments = {
"Mine1":[Ressource(bois=50), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"Mine2":[Ressource(bois=100, bronze=100), Ressource(allocationElectricite=10, allocationHumain=10), 2],
"Mine3":[Ressource(bois=500, titanium=300), Ressource(allocationElectricite=10, allocationHumain=10), 3],
"Camp_Bucherons1":[Ressource(bronze=50), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"Camp_Bucherons2":[Ressource(bois=100, bronze=50), Ressource(allocationElectricite=10, allocationHumain=10), 2],
"Camp_Bucherons3":[Ressource(bois=200, titanium=200), Ressource(allocationElectricite=20, allocationHumain=20), 3],
"Usine_Vehicule":[Ressource(bois=100, bronze=100), Ressource(allocationElectricite=10, allocationHumain=10), 1],
"Usine_Vaisseau1":[Ressource(bois=100, bronze=200), Ressource(allocationElectricite=10, allocationHumain=10), 2],
"Usine_Vaisseau2":[Ressource(titanium=300), Ressource(allocationElectricite=25, allocationHumain=20), 3],
"Usine_Drone":[Ressource(titanium=200, metasic=200), Ressource(allocationElectricite=25, allocationHumain=25), 3],
"Centrale_Charbon":[Ressource(bronze=50, charbon=50), Ressource(allocationHumain=5), 1],
"Ville":[Ressource(), Ressource(), 1],
"Ville2":[Ressource(bois=200, bronze=200, nourriture=200, eau=200), Ressource(), 2],
"Ville3":[Ressource(titanium =500, uranium=500, nourriture=1000, eau=1000, bois=1000), Ressource(), 3],
"Puit1":[Ressource(), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"Puit2":[Ressource(bronze=50, titanium=50), Ressource(allocationElectricite=10, allocationHumain=5), 2],
"Banque":[Ressource(titanium=300, bronze=300), Ressource(allocationElectricite=20, allocationHumain=15), 2],
"Ferme1":[Ressource(bois=50), Ressource(allocationElectricite=5, allocationHumain=5), 1],
"Ferme2":[Ressource(bronze=100, bois=100), Ressource(allocationElectricite=15, allocationHumain=15), 2],
"Mur":[Ressource(bois=50), Ressource(), 1],
"Tour":[Ressource(bois=150), Ressource(allocationHumain=10), 1],
"Canon":[Ressource(bronze=100), Ressource(allocationElectricite=50, allocationHumain=25), 1],###############temporaire###########
"Canon_Ion":[Ressource(titanium=300, bronze=100), Ressource(allocationElectricite=50, allocationHumain=25), 3],
"Canon_Acid":[Ressource(titanium=500), Ressource(allocationElectricite=25, allocationHumain=25), 3],
"Bouclier":[Ressource(titanium=200, metasic=200), Ressource(allocationElectricite=55, allocationHumain=50), 3]
}

dictionnaireProductionRessources = {
    "Mine1":Ressource(bronze=2),
    "Mine2":Ressource(bronze=4, titanium = 2),
    "Mine3":Ressource(bronze=6, titanium = 4, metasic = 4),
    "Camp_Bucherons1":Ressource(bois=2),
    "Camp_Bucherons2":Ressource(bois=4),
    "Camp_Bucherons3":Ressource(bois=6),
    "Centrale_Charbon":Ressource(electricite=0.5),
    "Puit1":Ressource(eau=5),
    "Puit2":Ressource(eau=10),
    "Ferme1":Ressource(nourriture=5),
    "Ferme2":Ressource(nourriture=10),
    "Ville":Ressource(humain=0.1),
    "Ville2":Ressource(humain=0.2),
    "Ville3":Ressource(humain=0.5),
    "Banque":Ressource()
}