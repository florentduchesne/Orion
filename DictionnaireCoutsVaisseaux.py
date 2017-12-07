from OE_objetsRessource import Ressource
from OE_objetsVaisseaux import VaisseauAttaque, VaisseauChasseur, VaisseauTank,\
    VaisseauColonisation, VaisseauCommercial, VaisseauNova, VaisseauSuicide, \
    VaisseauBiologique, VaisseauMere, VaisseauBombarde, VaisseauLaser

dictionnaireCoutsVaisseaux = {
    VaisseauAttaque:(Ressource(bronze=300, bois=200), 1),
    VaisseauChasseur:(Ressource(bronze=250, bois=150), 1),
    VaisseauTank:(Ressource(eau=450, bronze=250, metasic= 200), 1),
    VaisseauColonisation:(Ressource(titanium=300, bronze=250), 1),
    VaisseauCommercial:(Ressource(bronze=300, bois=200), 1),
    VaisseauNova:(Ressource(bronze=300, bois=200), 1),
    VaisseauSuicide:(Ressource(bronze=300, bois=200), 1),
    VaisseauBiologique:(Ressource(bronze=300, bois=200), 1),
    VaisseauMere:(Ressource(bronze=300, bois=200), 1),
    VaisseauBombarde:(Ressource(bronze=300, bois=200), 1),
    VaisseauLaser:(Ressource(titanium=300, bois=200), 1)
    }