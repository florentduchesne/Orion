import random
from helper import Helper as hlp
import math
from OE_objetsVaisseaux import *
from OE_objetsBatiments import *
from OE_objetsRessource import Ressource
from OE_objetsVehicule import vehiculeTank, vehiculehelicoptere
from OE_coord import *
from DictionnaireCoutsVaisseaux import *



class Joueur():
    def __init__(self,parent,nom,systemeorigine,couleur):
        self.parent=parent
        self.id=parent.createurId.prochainid()
        self.artificiel=0   # IA
        self.nom=nom
        self.systemeorigine=systemeorigine
        self.couleur=couleur
        self.niveau = 1
        self.maplanete=None
        self.systemesvisites=[systemeorigine]
        self.vaisseauxinterstellaires=[]
        self.vaisseauxinterplanetaires=[]
        self.stationspatiaux=[]
        self.vehiculeplanetaire=[]
        self.objetgalaxie=[]
        self.ressources = Ressource(bois= 1500, bronze = 1500, metasic=500, eau=500, nourriture=500, titanium=500)
        self.niveauVaisseau = 1
        self.vaisseauAttaque = 5
        self.vaisseauPortee = 3
        self.vaisseauCargoPersonne = 5
        self.vaisseauCargoAliments = 5
        self.maxVaisseauMere = 3
        self.nouveauMessageChatTxt = None
        self.listMessageChat = []
        self.listeBatiment=[]
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerdestination":self.ciblerdestination,
                      "ciblerdestinationvehicule":self.ciblerdestinationvehicule,
                      "atterrirplanete":self.atterrirplanete,
                      "visitersysteme":self.visitersysteme,
                      "creerbatiment":self.creerBatiment,
                      "creervehiculetank":self.creervehiculetank,
                      "creervehiculehelicoptere":self.creervehiculehelicoptere,
                      "creerstationspatiale":self.creerstationspatiale,
                      "ciblerEspace":self.ciblerEspace,
                      "voyageGalax":self.voyageGalax,
                      "voyageSystem":self.voyageSystem,
                      "viderVaisseau": self.viderVaisseau,
                      "recolterBatiment":self.recolterRessources,
                      "voyageSystem":self.voyageSystem,
                      "nouveauMessageChat":self.nouveauMessageChat,
                      "initplanete":self.initplanete}
                    #"vaisseauAttaque":self.attaque
        self.listeSousClassesBatiment = {"Mine1":Mine,
                                         "Camp_Bucherons1":CampBucherons,
                                         "Usine_Vehicule":UsineVehicule,
                                         "Usine_Vaisseau1":UsineVaisseau,
                                         "Usine_Drone":UsineDrone,
                                         "Centrale_Charbon":CentraleElectrique,
                                         "Puit1":Puit,
                                         "Banque":Banque,
                                         "Ferme1":Ferme,
                                         "Mur":Mur,
                                         "Tour":Tour,
                                         "Canon":Canon,
                                         "Bouclier":Bouclier,
                                         "Ville":Ville
                                         }
        self.listeClassesVaisseaux = {"chasseur":VaisseauChasseur,
                                      "colonisateur":VaisseauColonisation,
                                      "tank":VaisseauTank,
                                      "mere":VaisseauMere
                                      
                                      
            }
      
    def creerstationspatiale(self,listeparams):
        idsystem,idplanete=listeparams
        for i in self.systemesvisites:
            if i.id==idsystem:
                for p in i.planetes:
                    if idplanete==p.id:
                        station=StationSpatiale(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.couleur,p)
                        self.stationspatiaux.append(station)                   
                        return 1            
                    

    def ameliorerBatiment(self, maSelection, planete, systeme):
        planete = self.getPlanete(planete, systeme)
        for infra in planete.infrastructures:
            if int(maSelection[2]) == int(infra.x) and int(maSelection[3]) == int(infra.y):
                infra.ameliorer(self, planete)
                return
    
    def ajouterHumain(self, maSelection, planete, systeme):
        planete = self.getPlanete(planete, systeme)
        for infra in planete.infrastructures:
            if int(maSelection[2]) == int(infra.x) and int(maSelection[3]) == int(infra.y):
                infra.ajouterHumain(self, planete)
                return
            
    def getPlanete(self, planeteID, systemeID):
        for systeme in self.parent.systemes:
            if systeme.id == systemeID:
                for planete in systeme.planetes:
                    if planete.id == planeteID:
                        return planete
        
    def initplanete(self,param):
        from OE_vuePlanete import VuePlanete
        idSys, idPlan = param
        s = VuePlanete(self.parent.parent.vue,idSys, idPlan)
        self.parent.parent.vue.modes["planetes"][idPlan] = s
        s.initplanete(idSys, idPlan)
        
    def creerBatiment(self, listeparams):
        print("créer batiment")
        print("mon nom : " + self.nom)
        
        nom, systemeid, planeteid, x, y, nomBatiment = listeparams
        
        print("nom proprio : " + nom)
        villeTrouvee = False
        for i in self.systemesvisites:
            if i.id==systemeid:
                for p in i.planetes:
                    if p.id==planeteid:
                        for infra in p.infrastructures:#on vérifie si le joueur possede une Ville sur la planete (ou s'il est en train de coloniser)
                            print("ville donc peut creer")
                            if isinstance(infra, Ville):
                                if infra.proprietaire == nom:
                                    villeTrouvee = True
                        if villeTrouvee or nomBatiment == "Ville":
                            
                            ###ON FAIT LES CAS SPECIAUX###
                            if(nomBatiment == "vehiculetank"):
                                self.creervehiculetank(listeparams)
                                return
                            if (nomBatiment == "vehiculehelicoptere"):
                                self.creervehiculehelicoptere(listeparams)
                                return
                            if(nomBatiment == "Bouclier"):
                                aAssezDeRessources = self.parent.constructeurBatimentHelper.construireBatiment(p.dicRessourceParJoueur[nom], self.ressources, nomBatiment)
                                if(aAssezDeRessources):
                                    batiment=self.listeSousClassesBatiment[nomBatiment](self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomBatiment, proprio = nom)
                                    p.infrastructures.append(batiment)
                                    self.listeBatiment.append(batiment)
                                    self.parent.parent.afficherbouclier(nom,systemeid,planeteid,x,y,self.couleur,nomBatiment)
                                return
                            
                            ###SI PAS DE CAS SPECIAUX, ON APPELLE LE CONSTRUCTEUR GENERAL###
                            aAssezDeRessources = self.parent.constructeurBatimentHelper.construireBatiment(p.dicRessourceParJoueur[nom], self.ressources, nomBatiment)
                            if(aAssezDeRessources):
                                batiment=self.listeSousClassesBatiment[nomBatiment](self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomBatiment, proprio = nom)
                                p.infrastructures.append(batiment)
                                self.listeBatiment.append(batiment)
                                self.parent.parent.afficherBatiment(self, systemeid, planeteid, x, y, nomBatiment, batiment.id)

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
        idsystem,idplanete,typeVaisseau =ids#,typeVaisseau=ids
        for i in self.systemesvisites:
            if i.id==idsystem:
                for p in i.planetes:
                    villeTrouvee = False
                    for infra in p.infrastructures:
                        ######################IMPORTANT!!!!!##################
                        #décommenter le if ci-dessous, et réindenter le if qui suit pour la sortie du jeu
                        if isinstance(infra, UsineVaisseau):
                            if infra.proprietaire == self.nom:
                                villeTrouvee = True
                                break
                    if villeTrouvee:
                        if idplanete==p.id:
                            
                            #a placer plus tard dans un constructeur helper
                            ressourcesTotales = Ressource()
                            ressourcesTotales.additionnerRessources(self.ressources)
                            ressourcesTotales.additionnerRessources(p.dicRessourceParJoueur[self.nom])
                            coutVaisseau = dictionnaireCoutsVaisseaux[self.listeClassesVaisseaux[typeVaisseau]][0]
                            if(ressourcesTotales.estPlusGrandOuEgal(coutVaisseau)):
                                self.ressources.soustraireRessourcesJoueurETPlanet(p.dicRessourceParJoueur[self.nom], coutVaisseau)
                            
                                if typeVaisseau == "chasseur" :
                                    v=VaisseauChasseur(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.vaisseauAttaque, self.vaisseauPortee,type)#self.niveauVaisseau)
                                    self.vaisseauxinterstellaires.append(v)
                                    
                                elif typeVaisseau == "colonisateur":
                                    v=VaisseauColonisation(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.vaisseauCargoPersonne, self.vaisseauCargoAliments,type)#self.niveauVaisseau)
                                    self.vaisseauxinterstellaires.append(v)
                                
                                elif typeVaisseau == "tank" :
                                    v=VaisseauTank(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.vaisseauAttaque, self.vaisseauPortee,type)#self.niveauVaisseau)
                                    self.vaisseauxinterstellaires.append(v)
                                elif typeVaisseau == "mere" :
                                    v=VaisseauMere(self,self.nom,i,self.parent.createurId.prochainid(),i.id,p.x,p.y,self.vaisseauAttaque, self.vaisseauPortee,type,self.maxVaisseauMere)#self.niveauVaisseau)
                                    self.vaisseauxinterstellaires.append(v)
                                #print(v.x,v.y)
                                return 1            

    def creervehiculetank(self, listeparams):
        nom,systemeid,planeteid,x,y, nomBatiment=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        if self.niveau > 0:
                            nomtank = 'vehiculetank'+str(self.niveau)
                        else:
                            nomtank = 'vehiculetank'   
                        tank=vehiculeTank(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomtank)
                        #verification du cout pour le vehicule
                        if tank.verificationRessources():
                            j.vehiculeplanetaire.append(tank)
                            self.vehiculeplanetaire.append(tank)
                            self.parent.parent.affichervehiculetank(nom,systemeid,planeteid,x,y, tank.id)
                        else:
                            self.parent.parent.nouveauMessageSystemChat("Pas assez de ressource")
                        

    def creervehiculehelicoptere(self, listeparams):
        nom,systemeid,planeteid,x,y, nomBatiment=listeparams
        for i in self.systemesvisites:
            if i.id==systemeid:
                for j in i.planetes:
                    if j.id==planeteid:
                        if self.niveau > 0:
                            nomheli = 'vehiculehelicoptere'+str(self.niveau)
                        else:
                            nomheli = 'vehiculehelicoptere'
                        heli=vehiculehelicoptere(self,nom,systemeid,planeteid,x,y,self.parent.createurId.prochainid(), nomheli)
                        if heli.verificationRessources():
                            j.vehiculeplanetaire.append(heli)
                            self.vehiculeplanetaire.append(heli)
                            self.parent.parent.affichervehiculehelicoptere(nom,systemeid,planeteid,x,y, heli.id)
                        else:
                            self.parent.parent.nouveauMessageSystemChat("Pas assez de ressource")
                            
    def ameliorerVehicule(self, maSelection, planete, systeme):
        planete = self.getPlanete(planete, systeme)
        for vehicule in planete.vehiculeplanetaire:
            if vehicule.id == maSelection[5]:
                vehicule.ameliorer()        
        
    def ciblerdestination(self,ids):
        idori,iddesti,idsyteme,xy=ids
        for i in self.vaisseauxinterstellaires:
            if i.id== idori:
                for j in self.parent.systemes:
                    if j.id == iddesti and idsyteme == None:
                        i.ciblerdestination(j)
                        return 
                for v in self.vaisseauxinterstellaires:
                    if v.id == iddesti and idori != iddesti and idsyteme == None:
                        i.ciblerdestination(v)       
                        #i.ciblerdestination(Coord(xy))
                        return          
                for j in self.parent.systemes:
                    if j.id == idsyteme:
                        for p in j.planetes:
                            if p.id== iddesti:
                                #i.cible=j
                                i.ciblerdestination(p)
                        for v in self.vaisseauxinterstellaires:
                            if v.id == iddesti and idori != iddesti:
                                i.ciblerdestination(v)       
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
                i.ciblerdestination(xy)  
                #i.ciblerdestination(Coord(xy))
                return

    def voyageGalax(self,ids):
        idpropri,idVais=ids
        for i in self.vaisseauxinterstellaires:
            if i.id == idVais:
                if isinstance(i, VaisseauMere):
                    for j in self.parent.systemes:
                        if j.id==i.idSysteme:
                            #i.x= j.x
                            # i.y=j.y
                            i.x= j.x-1
                            i.y=j.y-1
                            i.dansGalaxie=True
                            self.objetgalaxie.append(i)
                else:
                    self.parent.parent.nouveauMessageSystemChat("Ce vaisseau ne peut voyager", "dans la galaxie!")
                    

    def voyageSystem(self,ids): 
        idSystem, idVais=ids
        for i in self.vaisseauxinterstellaires:
            if i.id == idVais:
                for j in self.parent.systemes:
                    if j.id==idSystem:
                        i.idSysteme=j.id
                        i.dansGalaxie=False
                        i.x=self.parent.diametre/2-2
                        i.y=self.parent.diametre/2-2
                        self.objetgalaxie.remove(i)
                        self.visitersysteme(idSystem)
    
    def viderVaisseau (self,ids):
        idpropri,idVais=ids
        for i in self.vaisseauxinterstellaires:
            if i.id == idVais:
                if isinstance(i, VaisseauMere):
                    print("coudonc")
                    i.SortirVaisseau()
                    print ("pourtant je passe")
                else :
                    print("Seulement un vaisseau Mere peut être vider")
                        
    def recolterRessources(self, id):
        idSysteme, idPlanete = id
        for i in self.systemesvisites:
            if i.id==idSysteme:
                for p in i.planetes:
                    if idPlanete==p.id:
                        if self.nom in p.dicRessourceParJoueur:
                            self.ressources.additionnerRessources(p.dicRessourceParJoueur[self.nom])
                            self.parent.parent.nouveauMessageSystemChat("Ressources collectées")
                            p.dicRessourceParJoueur[self.nom] = Ressource()
                        else:
                            self.parent.parent.nouveauMessageSystemChat("Pas Votre planet,","stop... please...")
                        return
        
                               
    def ciblerdestinationvehicule(self, ids):
        idorigine, x, y, idplanete, idvehicule = ids
        for i in self.vehiculeplanetaire:
            if i.id == idvehicule:
                c = Coord((x,y))
                i.ciblerdestination(c)
                pass
            pass
        pass
    
 
        
    def prochaineaction(self): # NOTE : cette fonction sera au coeur de votre developpement
        for i in self.vaisseauxinterstellaires:
            if i.cible:
                rep=i.avancer()
                if rep:
                    if rep == "colonisation":
                        #si le vaisseau a colonisé, on le détruit
                        self.vaisseauxinterstellaires.remove(i)
                        continue
                    else:
                        if rep.proprietaire=="inconnu":
                            if rep not in self.systemesvisites:
                                ##placer le bouton coloniser...
                                self.systemesvisites.append(rep)
                                self.parent.changerproprietaire(self.nom,self.couleur,rep)
            if isinstance(i, VaisseauAttaque) or isinstance(i, StationSpatiale):
                for protil in i.projectile:
                    if protil.cible == None:
                        i.projectile.remove(protil)
                    else:
                        protil.avancer() 
       
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
            for protil in i.projectile:
                    if protil.cible == None:
                        i.projectile.remove(protil)
                    else:
                        protil.avancer() 
            
            
        for i in self.stationspatiaux:
                i.orbiter()
                for protil in i.projectile:
                    if protil.cible == None:
                        i.projectile.remove(protil)
                    else:
                        protil.avancer() 
                
        for i in self.listeBatiment:
            if isinstance(i, Mur):
                pass
            elif isinstance(i, BatimentDefense)  :
                for protil in i.projectile:
                    if protil.cible == None:
                        i.projectile.remove(protil)
                    else:
                        protil.avancer() 
        
        self.detecterCible()
        self.choisirCible()
        self.retirerVaiseauMort()
        
    def detecterCible(self):
        for jKey in self.parent.joueurscles:
            if jKey is self.nom:
                pass
            else:
                j=self.parent.joueurs.get(jKey)
                for vaisseau in self.vaisseauxinterstellaires:
                    if isinstance(vaisseau, VaisseauAttaque):
                        vaisseau.listeCibleAttaquer.clear()
                        for vaisseauEnnemi in j.vaisseauxinterstellaires:
                            if vaisseau.idSysteme == vaisseauEnnemi.idSysteme:
                                if not vaisseau.dansVaisseauMere and not vaisseauEnnemi.dansVaisseauMere :
                                    distance = hlp.calcDistance(vaisseau.x,vaisseau.y,vaisseauEnnemi.x,vaisseauEnnemi.y)
                                    if distance < vaisseau.range:
                                        vaisseau.listeCibleAttaquer.append(vaisseauEnnemi)
                                        #print("vaisseau detecter")
                        
                        vaisseau.listeCibleAttaquerStation.clear()                        
                        for stationEnnemi in j.stationspatiaux:
                            if vaisseau.idSysteme== stationEnnemi.systemeid:
                                distance = hlp.calcDistance(vaisseau.x,vaisseau.y,stationEnnemi.x,stationEnnemi.y)
                                if distance < vaisseau.range:
                                    vaisseau.listeCibleAttaquer.append(stationEnnemi)
                
                for station in self.stationspatiaux:
                    station.listeCibleAttaquer.clear()
                    for vaisseauEnnemi in j.vaisseauxinterstellaires:
                        if station.systemeid == vaisseauEnnemi.idSysteme:
                            if not vaisseauEnnemi.dansVaisseauMere :
                                distance = hlp.calcDistance(station.x,station.y,vaisseauEnnemi.x,vaisseauEnnemi.y)
                                if distance < station.range:
                                    station.listeCibleAttaquer.append(vaisseauEnnemi)
                                    #print("vaisseau detecter")
                
                for tank in self.vehiculeplanetaire:         
                    tank.listeCibleAttaquer.clear()
                    for tankEnnemi in j.vehiculeplanetaire:                    
                        if tank.planeteid == tankEnnemi.planeteid:                        
                            distance = hlp.calcDistance(tank.x,tank.y,tankEnnemi.x,tankEnnemi.y)                           
                            if distance < tank.range:                                
                                tank.listeCibleAttaquer.append(tankEnnemi)
                    for batiment in j.listeBatiment:
                        if tank.planeteid == batiment.planeteid: 
                            distance = hlp.calcDistance(tank.x,tank.y,batiment.x,batiment.y)                           
                            if distance < tank.range:                                
                                tank.listeCibleAttaquer.append(batiment)
                                
                for batiment in j.listeBatiment:
                    if isinstance(batiment, Mur):
                        pass
                    elif isinstance(batiment, BatimentDefense):
                        batiment.listeCibleAttaquer.clear()
                        for tankEnnemi in self.vehiculeplanetaire: 
                            if tankEnnemi.proprietaire != batiment.proprietaire:
                                if batiment.planeteid == tankEnnemi.planeteid:                        
                                    distance = hlp.calcDistance(batiment.x,batiment.y,tankEnnemi.x,tankEnnemi.y)                           
                                    if distance < tank.range:                                
                                        batiment.listeCibleAttaquer.append(tankEnnemi)

                    
    def choisirCible(self):    
        for vseau in self.vaisseauxinterstellaires:
            if isinstance(vseau, VaisseauAttaque):
                vseau.cibleAttaque=None
                if len(vseau.listeCibleAttaquer)>0:
                    vseau.cibleAttaque = vseau.listeCibleAttaquer[0]
                    vseau.attaquer()  
                elif len(vseau.listeCibleAttaquerStation)>0:
                    vseau.cibleAttaque = vseau.listeCibleAttaquerStation[0]
                    vseau.attaquer()  
                else:
                    pass      
      

        for station in self.stationspatiaux:       
            station.cibleAttaque=None
            #print(station.listeCibleAttaquer)
            if len(station.listeCibleAttaquer)>0:
                station.cibleAttaque = station.listeCibleAttaquer[0]
                station.attaquer()   
            else:
                pass  
            
        
        for tank in self.vehiculeplanetaire:
            tank.cibleAttaque=None
            if len(tank.listeCibleAttaquer)>0:
                tank.cibleAttaque = tank.listeCibleAttaquer[0]
                tank.attaquer()   
            else:
                pass  
        
        for batiment in self.listeBatiment:
            if isinstance(batiment, Mur):
                        pass
            elif isinstance(batiment, BatimentDefense):
                batiment.cibleAttaque=None
                if len(batiment.listeCibleAttaquer)>0:
                    batiment.cibleAttaque = batiment.listeCibleAttaquer[0]
                    batiment.attaquer()   
                else:
                    pass      

    def retirerVaiseauMort(self):
        for vseau in self.vaisseauxinterstellaires:
            if vseau.vie<1:
                self.vaisseauxinterstellaires.remove(vseau)
                
        for station in self.stationspatiaux:
            if station.vie<1:
                self.stationspatiaux.remove(station)    
                
        for tank in self.vehiculeplanetaire:
            if tank.vie<1:
                self.vehiculeplanetaire.remove(tank)
                for s in  self.parent.systemes:
                    for p in s.planetes:
                        if p.id == tank.planeteid:
                            p.vehiculeplanetaire.remove(tank)
        for batiment in self.listeBatiment:
            #print(batiment.vie)
            if batiment.vie<1:
                self.listeBatiment.remove(batiment)
                for s in  self.parent.systemes:
                    for p in s.planetes:
                        if p.id == batiment.planeteid:
                            p.infrastructures.remove(batiment)
                
    def nouveauMessageChat(self,txt):
        self.nouveauMessageChatTxt = txt
        #self.parent.parent.Vue.nouveauMessageChat(txt)
        
        
        
        
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