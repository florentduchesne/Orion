from OE_objetsJoueur import *
from OE_objets import *
from OE_constructeurBatimentHelper import ConstructeurBatimentHelper


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
        self.compteurLabel = 20
        self.constructeurBatimentHelper = ConstructeurBatimentHelper()
        
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
     
            
    def creervaisseau(self,idsysteme,idplanete,typeVaisseau):
        ids=idsysteme,idplanete,typeVaisseau
        self.parent.actions.append([self.parent.monnom,"creervaisseau",ids])
       
        
    def creerstationspatiale(self,systeme,planete):
        ids =systeme,planete
        self.parent.actions.append([self.parent.monnom,"creerstationspatiale",ids])
            
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
        
        self.miseAJourLabelsRessources()
            
    def changerproprietaire(self,nom,couleur,syst):
        self.parent.changerproprietaire(nom,couleur,syst)
        
    def augmenterRessources(self):
        if self.compteur == 0:
            self.compteur = 40
            for systeme in self.systemes:#boucle a travers les systemes
                for planete in systeme.planetes:#boucle a travers les planetes
                    for infra in planete.infrastructures:#boucle a travers les batiments
                        if(isinstance(infra, BatimentRessources)):
                            #if(planete.ressourceACollecter.estPlusGrandOuEgal(infra.productionRessources)):
                            planete.ressourceACollecter.soustraireRessources(infra.productionRessources)#diminue les ressources disponibles sur la planete
                            planete.dicRessourceParJoueur[infra.proprietaire].additionnerRessources(infra.productionRessources)#augmente les ressources de la planet
                        if isinstance(infra, Banque):
                            self.joueurs[infra.proprietaire].ressources.additionnerRessources(planete.dicRessourceParJoueur[infra.proprietaire])
                            planete.dicRessourceParJoueur[infra.proprietaire] = Ressource()
                            
                            
        else:
            self.compteur -= 1
            
    def miseAJourLabelsRessources(self):
        if self.compteurLabel == 0:
            self.compteurLabel = 20
            self.parent.vue.miseAJourLabelsRessources()
        else:
            self.compteurLabel -= 1