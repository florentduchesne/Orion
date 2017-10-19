from OE_objetsJoueur import *
from OE_objets import *


class Modele():
    def __init__(self,parent,joueurs,dd):
        self.parent=parent
        self.createurId=self.parent.createurId
        self.diametre,self.densitestellaire,qteIA=dd
        self.nbsystemes=int(self.diametre**2/self.densitestellaire)
        print(self.nbsystemes)
        self.ias=[]    # IA 
        self.joueurs={}
        self.joueurscles=joueurs
        self.actionsafaire={}
        self.pulsars=[]
        self.systemes=[]
        self.terrain=[]
        self.creersystemes(int(qteIA))  # nombre d'ias a ajouter
        self.compteur = 20
        
    def creersystemes(self,nbias):  # IA ajout du parametre du nombre d'ias a ajouter
        
        for i in range(self.nbsystemes):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            self.systemes.append(Systeme(self,x,y))
        
        for i in range(20):
            x=random.randrange(self.diametre*10)/10
            y=random.randrange(self.diametre*10)/10
            self.pulsars.append(Pulsar(self,x,y,self.createurId.prochainid()))
            
        np=len(self.joueurscles) + nbias  # on ajoute le nombre d'ias
        planes=[]
        systemetemp=self.systemes[:]
        while np:
            p=random.choice(systemetemp)
            if p not in planes and len(p.planetes)>0:
                planes.append(p)
                systemetemp.remove(p)
                np-=1
        couleurs=["cyan","goldenrod","orangered","greenyellow",
                  "dodgerblue","yellow2","maroon1","chartreuse3",
                  "firebrick1","MediumOrchid2","DeepPink2","blue"]    # IA ajout de 3 couleurs
        
        
        
        for i in self.joueurscles:
            #parent,nom,systemeorigine,couleur
            systemeOriginine = planes.pop(0)
            couleurProp = couleurs.pop(0)
            self.joueurs[i]=Joueur(self,i,systemeOriginine,couleurProp)
            #faire fonction qui va changer le propri�taire de la planete/systemesolaire
            
            systemeOriginine.setProprietairePlanete(self.joueurs[i],  couleurProp)
            #self.parent.changerTagsVue(i,couleurProp)

        for i in range(nbias): # IA
            nomia="IA_"+str(i)
            self.joueurscles.append(nomia)
            ia=IA(self,nomia,planes.pop(0),couleurs.pop(0))
            self.joueurs[nomia]=ia  #IA
            self.ias.append(ia)  #IA
            
    def creervaisseau(self,planete):
        self.parent.actions.append([self.parent.monnom,"creervaisseau",planete])
        print("modele ok")
            
    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
                self.joueurs[i[0]].actions[i[1]](i[2])
            del self.actionsafaire[cadre]
                
        for i in self.joueurscles:
            self.joueurs[i].prochaineaction()
            
        for i in self.ias:
            i.analysesituation()
            
        for i in self.pulsars:
            i.evoluer()
        
        self.augmenterRessources()
            
    def changerproprietaire(self,nom,couleur,syst):
        self.parent.changerproprietaire(nom,couleur,syst)
        
    def augmenterRessources(self):
        if self.compteur == 0:
            self.compteur = 40
            for i in range(self.systemes.__len__()):#boucle a travers les systemes
                for j in range(self.systemes.__getitem__(i).planetes.__len__()):#boucle a travers les planetes
                    for k in range(self.systemes.__getitem__(i).planetes.__getitem__(j).infrastructures.__len__()):#boucle a travers les infrastructures
                        self.systemes.__getitem__(i).planetes.__getitem__(j).ressource.humain += 2 #on augmente la population
                        if( isinstance(self.systemes.__getitem__(i).planetes.__getitem__(j).infrastructures.__getitem__(k), Mine)):
                            print ("un mine!")
                            if(self.systemes.__getitem__(i).planetes.__getitem__(j).ressourceACollecter.bronze > 0):
                                self.systemes.__getitem__(i).planetes.__getitem__(j).ressourceACollecter.bronze -= 5
                                self.systemes.__getitem__(i).planetes.__getitem__(j).ressource.bronze += 5
                            print (self.systemes.__getitem__(i).planetes.__getitem__(j).ressource.bronze)
                        elif(isinstance(self.systemes.__getitem__(i).planetes.__getitem__(j).infrastructures.__getitem__(k), Ville)):
                            #print ("une ville!")
                            pass
        else:
            self.compteur -= 1