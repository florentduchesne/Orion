import random
from helper import Helper as hlp
import math
from OE_objetsVaisseaux import *
from OE_objetsBatiments import *
from OE_objetsRessource import Ressource
from OE_objetsVehicule import vehiculeTank, vehiculeCommerce, vehiculeAvion
from OE_coord import *


class Joueur():
    def __init__(self,parent,nom,systemeorigine,couleur):
        self.parent=parent
        self.id=parent.createurId.prochainid()
        self.artificiel=0   # IA
        self.nom=nom
        self.systemeorigine=systemeorigine
        self.couleur=couleur
        self.maplanete=None
        self.systemesvisites=[systemeorigine]
        self.vaisseauxinterstellaires=[]
        self.vaisseauxinterplanetaires=[]
        self.vehiculeplanetaire=[]
        self.ressources = Ressource(bois = 46, bronze = 53)
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerdestination":self.ciblerdestination,
                      "ciblerdestinationvehicule":self.ciblerdestinationvehicule,
                      "atterrirplanete":self.atterrirplanete,
                      "visitersysteme":self.visitersysteme,
                      "creermine":self.creermine,
                      "creermur":self.creermur,
                      "creertour":self.creertour,
                      "creercanon":self.creercanon,
                      "creerbouclier":self.creerbouclier,
                      "creervehiculetank":self.creervehiculetank,
                      "creervehiculecommerce":self.creervehiculecommerce,
                      "creervehiculeavion":self.creervehiculeavion,
                      "creerstationspatiale":self.creerstationspatiale}
        
    def creertour(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        tour=Tour(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.infrastructures.append(tour)
                        self.parent.parent.affichertour(nom,systemeid,planeteid,x,y)

    def creercanon(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        canon=Canon(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.infrastructures.append(canon)
                        self.parent.parent.affichercanon(nom,systemeid,planeteid,x,y)
        
    def creerbouclier(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        bouclier=Bouclier(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.infrastructures.append(bouclier)
                        self.parent.parent.afficherbouclier(nom,systemeid,planeteid,x,y,self.couleur)
        
    
    def creermur(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        mur=Mur(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.infrastructures.append(mur)
                        self.parent.parent.affichermur(nom,systemeid,planeteid,x,y)
                        
    def creerstationspatiale(self,id):
        print("station dans joueur")

    def creermine(self,listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        aAssezDeRessources = self.parent.constructeurBatimentHelper.construireBatiment(j.ressource, "Mine")
                        if(aAssezDeRessources):
                            mine=Mine(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), "Mine")
                            j.infrastructures.append(mine)
                            self.parent.parent.affichermine(nom,systemeid,planeteid,x,y)
                        else:
                            print("construction de mine impossible")
                        
    def atterrirplanete(self,d):
        nom,systeid,planeid=d
        for i in self.systemesvisites:
            if i.id==systeid:
                for j in i.planetes:
                    if j.id==planeid:
                        i.planetesvisites.append(j)
                        if nom==self.parent.parent.monnom:
                            self.parent.parent.voirplanete(i.id,j.id)
                        return 1
        
    def visitersysteme(self,systeme_id):
        for i in self.parent.systemes:
            if i.id==systeme_id:
                self.systemesvisites.append(i)
                
    def creervaisseau(self,ids):
        idsystem,idplanete=ids
        for i in self.systemesvisites:
            if i.id==idsystem:
                for p in i.planetes:
                    print("vais creer")
                    if idplanete==p.id:
                        print("vais creer")
                        v=Vaisseau(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y)
                        self.vaisseauxinterstellaires.append(v)
                        return 1            

    def creervehiculetank(self, listeparams):
        nom,systemeid,planeteid,x,y=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        tank=vehiculeTank(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.vehiculeplanetaire.append(tank)
                        self.vehiculeplanetaire.append(tank)
                        self.parent.parent.affichervehiculetank(nom,systemeid,planeteid,x,y)

    def creervehiculecommerce(self, id):
        for i in self.systemesvisites:
            if i.id == id:
                vt = vehiculeCommerce(self, self.nom, i, self.parent.createurId.prochainid())
                self.vehiculeplanetaire.append(vt)
                return 1
    
    def creervehiculeavion(self, id):
        for i in self.systemesvisites:
            if i.id == id:
                vt = vehiculeAvion(self, self.nom, i, self.parent.createurId.prochainid())
                self.vehiculeplanetaire.append(vt)
                return 1
        
        
    def ciblerdestination(self,ids):
        idori,iddesti,idsyteme,xy=ids
        for i in self.vaisseauxinterstellaires:
            if i.id== idori:
                for j in self.parent.systemes:
                    if j.id== idsyteme:
                        for p in j.planetes:
                            if p.id== iddesti:
                                #i.cible=j
                                print("cible trouver")
                                i.ciblerdestination(p)
                                
                                #i.ciblerdestination(Coord(xy))
                                return
                for j in self.systemesvisites:
                    if j.id== idsyteme:
                        for p in j.planetes:
                            if p.id== iddesti:
                                #i.cible=j
                                i.ciblerdestination(p)
                                #i.ciblerdestination(Coord(xy))
                                return
     
    def ciblerdestinationvehicule(self, ids):
        print('une étape du déplacement de plus!!!')
        idorigine, x, y, idplanete = ids
        for i in self.vehiculeplanetaire:
            
            pass
        '''
        for i in self.vehiculeplanetaire:
            if i.id == idorigine:
                i.ciblerdestination()
        '''
        pass
        
    def prochaineaction(self): # NOTE : cette fonction sera au coeur de votre developpement
        for i in self.vaisseauxinterstellaires:
            if i.cible:
                #print("avancer")
                rep=i.avancer()
                if rep:
                    if rep.proprietaire=="inconnu":
                        if rep not in self.systemesvisites:
                            self.systemesvisites.append(rep)
                            self.parent.changerproprietaire(self.nom,self.couleur,rep)
       
        for i in self.vehiculeplanetaire:
            if i.cible:
                rep=i.avancer()
                if rep:
                    if rep.proprietaire=="inconnu":
                        if rep not in self.systemesvisites:
                            self.systemesvisites.append(rep)
                            self.parent.changerproprietaire(self.nom,self.couleur,rep)
        
        #self.detecterCible()
       # self.choisirCible()
       # self.retirerVaiseauMort()
        
    def detecterCible(self):
        for jKey in self.parent.joueurscles:
            if jKey is self.nom:
                pass
            else:
                j=self.parent.joueurs.get(jKey)
                for vaisseau in self.vaisseauxinterplanetaires:
                    vaisseau.listeCibleAttaquer.clear()
                    for vaisseauEnnemi in j.vaisseaux:
                        if vaisseau.systemePresent.id == vaisseauEnnemi.systemePresent.id:
                            distance = hlp.calcDistance(vaisseau.position[0],vaisseau.position[1],vaisseauEnnemi.position[0],vaisseauEnnemi.position[1])
                            
                    
                
        
#  DEBUT IA
class IA(Joueur):
    def __init__(self,parent,nom,systemeorigine,couleur):
        Joueur.__init__(self,parent,nom,systemeorigine,couleur)
        self.contexte="systeme"
        self.delaiaction=random.randrange(5,10)*20  # le delai est calcule pour chaque prochaine action en seconde
        #self.derniereaction=time.time()
        
    # NOTE sur l'analyse de la situation   
    #          on utilise le temps (time.time() retourne le nombre de secondes depuis 1970) pour le delai de 'cool down'
    #          la decision dependra du contexte (modes de la vue)
    #          aussi presentement - on s'occupe uniquement d'avoir un vaisseau et de deplacer ce vaisseau vers 
    #          le systeme le plus proche non prealablement visite.
    def analysesituation(self):
        #t=time.time()
        if self.delaiaction==0:
            if self.contexte=="systeme":
                if len(self.vaisseauxinterstellaires)==0:
                    c=self.parent.parent.cadre+5
                    if c not in self.parent.actionsafaire.keys(): 
                        self.parent.actionsafaire[c]=[] 
                    self.parent.actionsafaire[c].append([self.nom,"creervaisseau",self.systemeorigine.id])
                    print("AJOUTER VAISSEAU ",self.systemeorigine.x,self.systemeorigine.y)
                else:
                    for i in self.vaisseauxinterstellaires:
                        sanscible=[]
                        if i.cible==None:
                            sanscible.append(i)
                        if sanscible:
                            vi=random.choice(sanscible)
                            systtemp=None
                            systdist=1000000000000
                            for j in self.parent.systemes:
                                d=hlp.calcDistance(vi.x,vi.y,j.x,j.y)
                                print ("DISTANCE ",i,d)
                                if d<systdist and j not in self.systemesvisites:
                                    systdist=d
                                    systtemp=j
                            if systtemp:
                                vi.ciblerdestination(systtemp)
                                print("CIBLER ",systtemp,systtemp.x,systtemp.y)
                            else:
                                print("JE NE TROUVE PLUS DE CIBLE")
                                
                self.delaiaction=random.randrange(5,10)*20
        else:
            self.delaiaction-=1
                #print("CIV:" ,self.nom,self.couleur, self.delaiaction)
        
# FIN IA