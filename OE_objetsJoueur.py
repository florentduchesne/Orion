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
        self.stationspatiaux=[]
        self.vehiculeplanetaire=[]
        self.objetgalaxie=[]
        self.ressources = Ressource(bois = 46, bronze = 53)
        self.niveauVaisseau = 1
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerdestination":self.ciblerdestination,
                      "ciblerdestinationvehicule":self.ciblerdestinationvehicule,
                      "atterrirplanete":self.atterrirplanete,
                      "visitersysteme":self.visitersysteme,
                      "creerbatiment":self.creerBatiment,
                      "creervehiculetank":self.creervehiculetank,
                      "creervehiculecommerce":self.creervehiculecommerce,
                      "creervehiculeavion":self.creervehiculeavion,
                      "creerstationspatiale":self.creerstationspatiale,
                      "ciblerEspace":self.ciblerEspace,
                      "voyageGalax":self.voyageGalax,
                      "voyageSystem":self.voyageSystem}
        self.listeSousClassesBatiment = {"Mine1":Mine,
                                         "Camp_Bucherons1":CampBucherons,
                                         "Usine_Vehicule":UsineVehicule,
                                         "Usine_Vaisseau1":UsineVaisseau,
                                         "Usine_Drone":UsineDrone,
                                         "Centrale_Charbon":CentraleElectrique,
                                         "Hopital1":Hopital,
                                         "Ecole":Ecole,
                                         "Laboratoire":Laboratoire,
                                         "Puit1":Puit,
                                         "Banque":Banque,
                                         "Ferme1":Ferme,
                                         "Mur":Mur,
                                         "Tour":Tour,
                                         "Canon":Canon,
                                         "Bouclier":Bouclier
                                         }
      
    def creerstationspatiale(self,listeparams):
        idsystem,idplanete=listeparams
        for i in self.systemesvisites:
            if i.id==idsystem:
                for p in i.planetes:
                    if idplanete==p.id:
                        station=StationSpatiale(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.couleur,p)
                        self.stationspatiaux.append(station)
                        print("Station Creer")
                        print("taille: " + str(p.taille))
                        print("distance: " + str(p.distance))
                        print("angle: " + str(p.angle))                        
                        return 1            
                    
    def ameliorerBatiment(self, maSelection, planete, systeme):
        print("AMELIORATION BATIMENT DANS OBJ JOUEUR")
        print(maSelection)
        #print(planete.infrastructures)
        planete = self.getPlanete(planete, systeme)
        for infra in planete.infrastructures:
            print("infra y : " + str(infra.y))
            print("infra x : " + str(infra.x))
            print("maSelection 2 : " + str(maSelection[2]))
            print("maSelection 3 : " + str(maSelection[3]))
            if int(maSelection[2]) == int(infra.x) and int(maSelection[3]) == int(infra.y):
                print(infra.nomBatiment)
                infra.ameliorer(self, planete)
                return
    
    def getPlanete(self, planeteID, systemeID):
        for systeme in self.systemesvisites:
            if systeme.id == systemeID:
                for planete in systeme.planetes:
                    if planete.id == planeteID:
                        return planete
        

    def creerBatiment(self, listeparams):
        nom, systemeid, planeteid, x, y, nomBatiment =listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        ###ON FAIT LES CAS SPECIAUX###
                        if(nomBatiment == "vehiculetank"):
                            self.creervehiculetank(listeparams)
                            return
                        if(nomBatiment == "Bouclier"):
                            aAssezDeRessources = self.parent.constructeurBatimentHelper.construireBatiment(j.ressource, self.ressources, nomBatiment)
                            if(aAssezDeRessources):
                                batiment=self.listeSousClassesBatiment[nomBatiment](self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomBatiment)
                                j.infrastructures.append(batiment)
                                self.parent.parent.afficherbouclier(nom,systemeid,planeteid,x,y,self.couleur,nomBatiment)
                            return
                        
                        ###SI PAS DE CAS SPECIAUX, ON APPELLE LE CONSTRUCTEUR GENERAL###
                        aAssezDeRessources = self.parent.constructeurBatimentHelper.construireBatiment(j.ressource, self.ressources, nomBatiment)
                        if(aAssezDeRessources):
                            batiment=self.listeSousClassesBatiment[nomBatiment](self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomBatiment, nom)
                            j.infrastructures.append(batiment)
                            self.parent.parent.afficherBatiment(nom,systemeid,planeteid,x,y, nomBatiment)
                        else:
                            print("construction du batiment impossible")

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
        idsystem,idplanete=ids#,typeVaisseau=ids
        for i in self.systemesvisites:
            if i.id==idsystem:
                for p in i.planetes:
                    #print("vais creer")
                    if idplanete==p.id:
                       # print("vais creer")
                        v=Vaisseau(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,)#self.niveauVaisseau)
                        self.vaisseauxinterstellaires.append(v)
                        return 1            

    def creervehiculetank(self, listeparams):
        nom,systemeid,planeteid,x,y, nomBatiment=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        tank=vehiculeTank(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid())
                        j.vehiculeplanetaire.append(tank)
                        self.vehiculeplanetaire.append(tank)
                        self.parent.parent.affichervehiculetank(nom,systemeid,planeteid,x,y, tank.id)

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
                            
    def ciblerEspace(self,ids):
        idori,idsyteme,xy=ids
        
        
        
        #xy =Coord(xyEsp)
        for i in self.vaisseauxinterstellaires:
            if i.id== idori:
                              
                
                xy =Coord((xy[0],xy[1]))
                print("cible espace")
                i.ciblerdestination(xy)
                                
                                #i.ciblerdestination(Coord(xy))
                return

    def voyageGalax(self,ids):
        idpropri,idVais=ids
        for i in self.vaisseauxinterstellaires:
            if i.id == idVais:
                for j in self.parent.systemes:
                    if j.id==i.idSysteme:
                        #i.x= j.x
                       # i.y=j.y
                        i.x= j.x-1
                        i.y=j.y-1
                        i.dansGalaxie=True
                        self.objetgalaxie.append(i)

    def voyageSystem(self,ids): 
        idVais,idpropri,idSystem=ids
        for i in self.vaisseauxinterstellaires:
            if i.id == idVais:
                for j in self.parent.systemes:
                    if j.id==idSystem:
                        i.idSysteme=j.id
                        i.dansGalaxie=False
                        i.x=25-2
                        i.y=25-2
                        self.objetgalaxie.remove(i)
                               
    def ciblerdestinationvehicule(self, ids):
        print('une étape du déplacement de plus!!!')
        idorigine, x, y, idplanete, idvehicule = ids
        for i in self.vehiculeplanetaire:
            if i.id == idvehicule:
                c = Coord((x,y))
                i.ciblerdestination(c)
                pass
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
                '''
                if rep:
                    if rep.proprietaire=="inconnu":
                        if rep not in self.systemesvisites:
                            self.systemesvisites.append(rep)
                            self.parent.changerproprietaire(self.nom,self.couleur,rep)
                '''
        
        for i in self.stationspatiaux:
                i.orbiter()
        
        self.detecterCible()
        #self.choisirCible()
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