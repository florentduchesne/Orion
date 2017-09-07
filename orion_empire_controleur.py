# -*- coding: utf-8 -*-

import os,os.path
import sys
import Pyro4
import socket
import random
from subprocess import Popen 
import math
import time # IA
from orion_empire_modele import *
from orion_empire_vue import *
from helper import Helper as hlp
from IdMaker import Id


class Controleur():
    def __init__(self):
        print("IN CONTROLEUR")
        self.createurId=Id
        self.attente=0
        self.cadre=0 # le no de cadre pour assurer la syncronisation avec les autres participants
        self.egoserveur=0 
        self.actions=[]    # la liste de mes actions a envoyer au serveur pour qu'il les redistribue a tous les participants
        self.monip=self.trouverIP() # la fonction pour retourner mon ip
        self.monnom=self.generernom() # un generateur de nom pour faciliter le deboggage (comme il genere un nom quasi aleatoire et on peut demarrer plusieurs 'participants' sur une meme machine pour tester)
        self.modele=None
        self.serveur=None
        self.vue=Vue(self,self.monip,self.monnom)
        self.vue.root.mainloop()
        
    def trouverIP(self): # fonction pour trouver le IP en 'pignant' gmail
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # on cree un socket
        s.connect(("gmail.com",80))    # on envoie le ping
        monip=s.getsockname()[0] # on analyse la reponse qui contient l'IP en position 0 
        s.close() # ferme le socket
        return monip
    
    def generernom(self):  # generateur de nouveau nom - accelere l'entree de nom pour les tests - parfois a peut generer le meme nom mais c'est rare
        monnom="jmd_"+str(random.randrange(1000))
        return monnom

    def creerpartie(self):
        if self.egoserveur==0:
            pid = Popen(["C:\\Python34\\Python.exe", "./orion_empire_serveur.py"],shell=1).pid # on lance l'application serveur
            self.egoserveur=1 # on note que c'est soi qui, ayant demarre le serveur, aura le privilege de lancer la simulation

    ## ----------- FONCTION POUR CELUI QUI A CREE LA PARTIE SEULEMENT
    def lancerpartie(self,diametre=5,densitestellaire=5,qteIA=0): # reponse du bouton de lancement de simulation (pour celui qui a parti le serveur seulement)
        rep=self.serveur.lancerpartie(diametre,densitestellaire,qteIA) 
   ## ----------- FIN --

    def inscrirejoueur(self):
        ipserveur=self.vue.ipsplash.get() # lire le IP dans le champ du layout
        nom=self.vue.nomsplash.get() # noter notre nom
        if ipserveur and nom:
            ad="PYRO:controleurServeur@"+ipserveur+":9999" # construire la chaine de connection
            self.serveur=Pyro4.core.Proxy(ad) # se connecter au serveur
            self.monnom=nom
            rep=self.serveur.inscrireclient(self.monnom)    # on averti le serveur de nous inscrire
            #tester retour pour erreur de nom
            #random.seed(rep[2])
            random.seed(1171)

    def boucleattente(self):
        rep=self.serveur.faireaction([self.monnom,0,0])
        if rep[0]:
            print("Recu ORDRE de DEMARRER")
            self.initierpartie(rep[2])
        elif rep[0]==0:
            self.vue.affichelisteparticipants(rep[2])
            self.vue.root.after(50,self.boucleattente)
        
    def initierpartie(self,rep):  # initalisation locale de la simulation, creation du modele, generation des assets et suppression du layout de lobby
        if rep[1][0][0]=="lancerpartie":
            #print("REP",rep)
            self.modele=Modele(self,rep[1][0][1],rep[1][0][2]) # on cree le modele
            self.vue.afficherinitpartie(self.modele)
            #print(self.monnom,"LANCE PROCHAINTOUR")
            self.prochaintour()
        
    def prochaintour(self): # la boucle de jeu principale, qui sera appelle par la fonction bouclejeu du timer
        if self.serveur: # s'il existe un serveur
            self.cadre=self.cadre+1 # increment du compteur de cadre
            if self.actions: # si on a des actions a partager 
                rep=self.serveur.faireaction([self.monnom,self.cadre,self.actions]) # on les envoie 
            else:
                rep=self.serveur.faireaction([self.monnom,self.cadre,0]) # sinon on envoie rien au serveur on ne fait que le pigner 
                                                                        # (HTTP requiert une requete du client pour envoyer une reponse)
            self.actions=[] # on s'assure que les actions a envoyer sont maintenant supprimer (on ne veut pas les envoyer 2 fois)
            if rep[1]=="attend":
                self.cadre=self.cadre-1 # increment du compteur de cadre
                print("J'attends")
            else:
                self.modele.prochaineaction(self.cadre)    # mise a jour du modele
                self.vue.modecourant.afficherpartie(self.modele) # mise a jour de la vue
            if rep[0]: # si le premier element de reponse n'est pas vide
                for i in rep[2]:   # pour chaque action a faire (rep[2] est dictionnaire d'actions en provenance des participants
                                   # dont les cles sont les cadres durant lesquels ses actions devront etre effectuees
                    if i not in self.modele.actionsafaire.keys(): # si la cle i n'existe pas
                        self.modele.actionsafaire[i]=[] #faire une entree dans le dictonnaire
                    for k in rep[2][i]: # pour toutes les actions lies a une cle du dictionnaire d'actions recu
                        self.modele.actionsafaire[i].append(k) # ajouter cet action au dictionnaire sous l'entree dont la cle correspond a i
            self.vue.root.after(50,self.prochaintour)
        else:
            print("Aucun serveur connu")

            
    def fermefenetre(self):
        if self.serveur:
            self.serveur.jequitte(self.monnom)
        self.vue.root.destroy()
        
    # FONCTIONS DE COUP DU JOUEUR A ENVOYER AU SERVEUR
    def creervaisseau(self,systeme):
        self.modele.creervaisseau(systeme)
        #self.actions.append([self.monnom,"creervaisseau",""])
        
    def ciblerdestination(self,idorigine,iddestination):
        self.actions.append([self.monnom,"ciblerdestination",[idorigine,iddestination]])
        
    def visitersysteme(self,systeme_id):
        self.actions.append([self.monnom,"visitersysteme",[systeme_id]])
        
    def atterrirdestination(self,joueur,systeme,planete):
        self.actions.append([self.monnom,"atterrirplanete",[self.monnom,systeme,planete]])
        
    
    def creermine(self,joueur,systeme,planete,x,y):
            self.actions.append([self.monnom,"creermine",[self.monnom,systeme,planete,x,y]])
        
    def affichermine(self,joueur,systemeid,planeteid,x,y):
        self.vue.affichermine(joueur,systemeid,planeteid,x,y)
        
    def voirplanete(self,idsysteme,idplanete):
        pass
    
    def changerproprietaire(self,nom,couleur,systeme):
        self.vue.modes["galaxie"].changerproprietaire(nom,couleur,systeme)
        
if __name__=="__main__":
    c=Controleur()
    print("End Orion_empire")