# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import os,os.path
from collections import OrderedDict
from helper import Helper as hlp
from OE_vueGalaxie import VueGalaxie
from OE_vueSysteme import VueSysteme
from OE_vuePlanete import VuePlanete
from OE_objetsRessource import *

class Vue():
    def __init__(self,parent,ip,nom,largeur=800,hauteur=600):
        self.root=Tk()
        self.root.title("Apocalypse Orion")
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.dictionnaireLabelsJoueur = OrderedDict()
        self.dictionnaireLabelsPlanete = OrderedDict()
        self.parent=parent
        self.modele=None
        self.nom=None
        self.largeur=largeur
        self.hauteur=hauteur
        self.images={}
        self.modes={}
        self.modecourant=None
        self.cadreactif=None
        self.creercadres(ip,nom)
        self.changecadre(self.cadresplash)
        
    def changemode(self,cadre):
        if self.modecourant:
            self.modecourant.pack_forget()
        self.modecourant=cadre
        self.modecourant.pack(expand=1,fill=BOTH)            

    def changecadre(self,cadre,etend=0):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        if etend:
            self.cadreactif.pack(expand=1,fill=BOTH)
        else:
            self.cadreactif.pack()
    
    def creercadres(self,ip,nom):
        self.creercadresplash(ip, nom)
        self.creercadrelobby()
        self.modecourant=None
        self.creercadreJeu()
    
    def creercadreJeu(self):
        self.cadrejeu=Frame(self.root,bg="blue")
        self.couleurJoueur = "#16c0ff"
        self.couleurPlanet = "#0c9cd2"
        
        self.cadreRessourcesJoueur = Frame(self.cadrejeu,height=40,bg=self.couleurJoueur)
        self.cadreRessourcesJoueur.pack(fill=X)
        
        self.cadreRessourcesPlanete = Frame(self.cadrejeu,height=40,bg=self.couleurPlanet)
        self.cadreRessourcesPlanete.pack(fill=X)
        
        self.envoyerRessourcesVersCadreJoueur()
        self.envoyerRessourcesVersCadrePlanete()
        
    def envoyerRessourcesVersCadreJoueur(self):
        
        self.chargerImagesRes()
        i = 0
        
        cadre = self.cadreRessourcesJoueur
        
        self.titreJoueur = (Label(cadre,image=self.images["joueur"],bg=self.couleurJoueur), Label(cadre,text="Joueur: ",bg=self.couleurJoueur))
        self.titreJoueur[0].grid(row=0,column=i)
        i = 1
        self.titreJoueur[1].grid(row=0,column=i)
        
        self.dictionnaireLabelsJoueur["humain"] = (Label(cadre,image=self.images["humain"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["electricite"] = (Label(cadre,image=self.images["electricite"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["moral"] = (Label(cadre,image=self.images["moral"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["nourriture"] = (Label(cadre,image=self.images["nourriture"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["eau"] = (Label(cadre,image=self.images["eau"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["bois"] = (Label(cadre,image=self.images["bois"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["bronze"] = (Label(cadre,image=self.images["bronze"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["charbon"] = (Label(cadre,image=self.images["charbon"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["titanium"] = (Label(cadre,image=self.images["titanium"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        self.dictionnaireLabelsJoueur["metasic"] = (Label(cadre,image=self.images["metasic"],bg=self.couleurJoueur), Label(cadre,text="0",bg=self.couleurJoueur))
        
        i = 2
        
        for d in self.dictionnaireLabelsJoueur:
            self.dictionnaireLabelsJoueur[d][0].grid(row=0, column = i)
            i += 1
            self.dictionnaireLabelsJoueur[d][1].grid(row=0, column = i)
            i += 1
        
    def envoyerRessourcesVersCadrePlanete(self):
        i = 0
        cadre = self.cadreRessourcesPlanete
        self.titrePlanete = (Label(cadre,image=self.images["planet"],bg=self.couleurPlanet), Label(cadre,text="Planète: ",bg=self.couleurPlanet))
        self.titrePlanete[0].grid(row=0,column=i)
        i = 1
        self.titrePlanete[1].grid(row=0,column=i)
        
        self.dictionnaireLabelsPlanete["humain"] = (Label(cadre,image=self.images["humain"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["electricite"] = (Label(cadre,image=self.images["electricite"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["moral"] = (Label(cadre,image=self.images["moral"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["nourriture"] = (Label(cadre,image=self.images["nourriture"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["eau"] = (Label(cadre,image=self.images["eau"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["bois"] = (Label(cadre,image=self.images["bois"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["bronze"] = (Label(cadre,image=self.images["bronze"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["charbon"] = (Label(cadre,image=self.images["charbon"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["titanium"] = (Label(cadre,image=self.images["titanium"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        self.dictionnaireLabelsPlanete["metasic"] = (Label(cadre,image=self.images["metasic"],bg=self.couleurPlanet), Label(cadre,text="0",bg=self.couleurPlanet))
        
        i = 2
        for d in self.dictionnaireLabelsPlanete:
            self.dictionnaireLabelsPlanete[d][0].grid(row=0, column = i)
            i += 1
            self.dictionnaireLabelsPlanete[d][1].grid(row=0, column = i)
            i += 1
            
    def miseAJourLabelsRessources(self):
        for i in self.parent.modele.joueurscles:
            if self.parent.modele.joueurs[i].nom == self.parent.monnom:
                for j in self.dictionnaireLabelsJoueur: 
                    if j == "humain":
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(int(self.parent.modele.joueurs[i].ressources.dictRess["allocation humain"]))+" / "+str(int(self.parent.modele.joueurs[i].ressources.dictRess[j])))
                    elif j == "electricite":
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(int(self.parent.modele.joueurs[i].ressources.dictRess["allocation electricite"]))+" / "+str(int(self.parent.modele.joueurs[i].ressources.dictRess[j])))
                    else:
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(self.parent.modele.joueurs[i].ressources.dictRess[j]))
        if(isinstance(self.modecourant, VuePlanete)):
            for systeme in self.parent.modele.systemes:
                for planete in systeme.planetes:
                    if(planete.id == self.modecourant.planeteid):
                        for j in self.dictionnaireLabelsPlanete: 
                            if self.parent.monnom in planete.dicRessourceParJoueur:
                                if j == "humain":
                                    self.dictionnaireLabelsPlanete[j][1].config(text = str(int(planete.dicRessourceParJoueur[self.parent.monnom].dictRess["allocation humain"]))+" / "+str(int(planete.dicRessourceParJoueur[self.parent.monnom].dictRess[j])))
                                elif j == "electricite":
                                    self.dictionnaireLabelsPlanete[j][1].config(text = str(int(planete.dicRessourceParJoueur[self.parent.monnom].dictRess["allocation electricite"]))+" / "+str(int(planete.dicRessourceParJoueur[self.parent.monnom].dictRess[j])))
                                else:
                                    self.dictionnaireLabelsPlanete[j][1].config(text = str(planete.dicRessourceParJoueur[self.parent.monnom].dictRess[j]))
                            else:
                                planete.dicRessourceParJoueur[self.parent.monnom] = Ressource()
                        return
        
    def chargerImagesRes(self):
        l = 18
        h = 18
        im = Image.open("./images/icone_Ressources/planet.png").resize((int(l),int(h)))
        self.images["planet"] = ImageTk.PhotoImage(im) 
        im = Image.open("./images/icone_Ressources/user.png").resize((l,h))
        self.images["joueur"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/uranium.png").resize((int(l),int(h)))
        self.images["uranium"] = ImageTk.PhotoImage(im) 
        im = Image.open("./images/icone_Ressources/titanium.png").resize((l,h))
        self.images["titanium"] = ImageTk.PhotoImage(im)
        #im = Image.open("./images/icone_Ressources/lacrima.png").resize((l,h))
        #self.images["lacrima"] = ImageTk.PhotoImage(im)"""
        #im = Image.open("./images/icone_Ressources/sante.png").resize((l,h))
        #self.images["sante"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/point_Science.png").resize((l,h))
        self.images["point_science"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/nourriture.png").resize((l,h))
        self.images["nourriture"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/humain.png").resize((l,h))
        self.images["humain"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/electricite.png").resize((l,h))
        self.images["electricite"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/eau.png").resize((l,h))
        self.images["eau"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/bronze.png").resize((l,h))
        self.images["bronze"] = ImageTk.PhotoImage(im)
        #im = Image.open("./images/icone_Ressources/biohazard.png").resize((l,h))
        #self.images["biohazard"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/charbon.png").resize((l,h))
        self.images["charbon"] = ImageTk.PhotoImage(im)
        #im = Image.open("./images/icone_Ressources/argent.png").resize((l,h))
        #self.images["argent"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/bois.png").resize((l,h))
        self.images["bois"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/metasic.png").resize((l,h))
        self.images["metasic"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/moral.png").resize((l,h))
        self.images["moral"] = ImageTk.PhotoImage(im)
        
             
    def creercadresplash(self,ip,nom):
        self.nwin = Toplevel()
        self.nwin.title("Intro")
        self.cadreIntro=Frame(self.nwin,bg="blue")

        self.photoIntro = ImageTk.PhotoImage(file = 'images/intro.jpg')
        self.canevasIntro=Canvas(self.cadreIntro,width=1400,height=787,bg="black")
        self.canevasIntro.create_image(0, 0, image = self.photoIntro, anchor = NW)
        
        self.lbl2 = Label(self.nwin, image = self.photoIntro)
        self.lbl2.pack()
        
        self.cadresplash=Frame(self.root)
        self.imageBackG = ImageTk.PhotoImage(file = "images/IntroGalaxy.jpg")
        self.imageBackG2 = ImageTk.PhotoImage(file = "images/IntroGalaxy2.jpg")
        self.imageTitre = ImageTk.PhotoImage(file = "images/Titre.png")
        self.canevasplash=Canvas(self.cadresplash,width=640,height=480,bg="black")
        self.canevasplash.create_image(0, 0, image = self.imageBackG, anchor = NW)
        self.ItemimageTitre = self.canevasplash.create_image(80, 60, image = self.imageTitre, anchor = NW)
        
        self.canevasplash.pack()
        self.nomsplash=Entry(bg="#18c0ff")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="#18c0ff")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="#50a2c1",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Creer partie",bg="#0092ca",command=self.creerpartie)
        btnconnecterpartie=Button(text="Connecter partie",bg="#0092ca",command=self.connecterpartie)
        self.canevasplash.create_window(500,200,window=self.nomsplash,width=100,height=30)
        self.canevasplash.create_window(500,250,window=self.ipsplash,width=100,height=30)
        self.canevasplash.create_window(500,300,window=labip,width=100,height=30)
        self.canevasplash.create_window(500,350,window=btncreerpartie,width=100,height=30)
        self.canevasplash.create_window(500,400,window=btnconnecterpartie,width=100,height=30) 
        
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.root)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="black")
        self.canevaslobby.create_image(0, 0, image = self.imageBackG2, anchor = NW)
        self.canevaslobby.pack()
        self.listelobby=Listbox(bg="#84d4f1",borderwidth=0,relief=FLAT)
        
        self.diametre=Entry(bg="#18c0ff")
        self.diametre.insert(0, 50)        
        
        self.densitestellaire=Entry(bg="#18c0ff")
        self.densitestellaire.insert(0, 50)
        
        self.qteIA=Entry(bg="#18c0ff")
        self.qteIA.insert(0, 0)
        
        self.btnlancerpartie=Button(text="Lancer partie",bg="#0092ca",command=self.lancerpartie,state=DISABLED)
        self.canevaslobby.create_window(480,240,window=self.listelobby,width=200,height=300)
        
        labDiametre=Label(text="Diametre en annee lumiere:",bg="#50a2c1",borderwidth=0,relief=RIDGE)
        self.canevaslobby.create_window(120,105,window=labDiametre,width=150,height=30)
        self.canevaslobby.create_window(260,105,window=self.diametre,width=100,height=30)
        
        labNBsys=Label(text="Nb systeme/AL cube:",bg="#50a2c1",borderwidth=0,relief=RIDGE)
        self.canevaslobby.create_window(120,175,window=labNBsys,width=150,height=30)
        self.canevaslobby.create_window(260,175,window=self.densitestellaire,width=100,height=30)
        
        labnbIA=Label(text="Nb d'IA:",bg="#50a2c1",borderwidth=0,relief=RIDGE)
        self.canevaslobby.create_window(120,245,window=labnbIA,width=150,height=30)
        self.canevaslobby.create_window(260,245,window=self.qteIA,width=100,height=30)
        
        self.canevaslobby.create_window(260,375,window=self.btnlancerpartie,width=100,height=30)
        
        #RENDRE LES TEXTBOX NON ACCESSIBLE POUR CHANGER LEUR VALEURS
        self.diametre.config(state=NORMAL)
        self.densitestellaire.config(state=NORMAL)
        self.qteIA.config(state=DISABLED)

    def voirgalaxie(self):
        # A FAIRE comme pour voirsysteme et voirplanete, tester si on a deja la vuegalaxie
        #         sinon si on la cree en centrant la vue sur le systeme d'ou on vient
        s=self.modes["galaxie"]
        self.changemode(s) 
        s.remplirChatBoxChangementVue()
       
    def voirsysteme(self,systeme=None):
        if systeme:
            sid=systeme.id
            if sid in self.modes["systemes"].keys():
                s=self.modes["systemes"][sid]
                s.remplirChatBoxChangementVue()
            else:
                s=VueSysteme(self)
                self.modes["systemes"][sid]=s
                s.initsysteme(systeme)
                s.remplirChatBoxChangementVue()
            self.changemode(s)
        
    def voirplanete(self,maselection=None):
        s=self.modes["planetes"]
        
        if maselection:
            sysid=maselection[5]
            planeid=maselection[2]
            if planeid in self.modes["planetes"].keys():
                s=self.modes["planetes"][planeid]
                self.cadreRessourcesPlanete.pack(fill=X)
                s.remplirChatBoxChangementVue()
            else:
                s=VuePlanete(self,sysid,planeid)
                self.modes["planetes"][planeid]=s
                s.initplanete(sysid,planeid)
                self.cadreRessourcesPlanete.pack(fill=X)
                s.remplirChatBoxChangementVue()
            self.changemode(s)
        else:
            self.modecourant.nouveauMessageSystemChat("Aucune planete selectionnée", "pour l'atterrissage")
     
        
        
    def creerpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.creerpartie()
            self.btnlancerpartie.config(state=NORMAL)
            self.connecterpartie()
          
    def connecterpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.inscrirejoueur()
            if self.parent.egoserveur == 0:
                self.diametre.config(state="disable")
                self.densitestellaire.config(state="disable")
                self.qteIA.config(state="disable")
            self.changecadre(self.cadrelobby)
            self.parent.boucleattente()
            
    def lancerpartie(self):
       
        diametre= self.diametre.get()
        densitestellaire=self.densitestellaire.get()
        qteIA=self.qteIA.get()  # IA
        if diametre :
            diametre=float(diametre)
        else:
            diametre=None
        if densitestellaire :
            densitestellaire=float(densitestellaire)
        else:
            densitestellaire=None
        self.parent.lancerpartie(diametre,densitestellaire,qteIA)  #IA
        
    def affichelisteparticipants(self,lj):
        self.listelobby.delete(0,END)
        for i in lj:
            self.listelobby.insert(END,i)
    
    def initialiserVuePlanete(self):
        pass
    
    def afficherinitpartie(self,mod):
        self.nom=self.parent.monnom
        self.modele=mod
        
        self.modes["galaxie"]=VueGalaxie(self)
        self.modes["systemes"]={}
        #self.modes["systemes"]=VueSysteme(self)
        self.modes["planetes"]={}
               
        #s = VuePlanete(self,systeme,planeteInit)
        #self.modes["planetes"] = s
        #s.initplanete(systeme.id,planeteInit.id)
               
        g=self.modes["galaxie"]
        #g=self.modes["planetes"]
        #g = self.modes["planetes"]
        g.labid.config(text=self.nom)
        g.labid.config(fg=mod.joueurs[self.nom].couleur)
        
        g.chargeimages()
        g.afficherdecor() #pourrait etre remplace par une image fait avec PIL -> moins d'objets
        self.changecadre(self.cadrejeu,1)
        self.changemode(self.modes["galaxie"])
        #self.changemode(self.modes["planetes"])
        
        for j in mod.joueurs: #pour chaque joueurs
            planeteDuJoueur = mod.joueurs[j].maplanete #planete du joueur
            systeme = planeteDuJoueur.parent #Systeme de la planete du joueur.
            self.voirsysteme(systeme) #création de la vue systeme
            if planeteDuJoueur.id in self.modes["planetes"].keys():
                s=self.modes["planetes"][planeteDuJoueur.id]
            else:
                s=VuePlanete(self,systeme.id,planeteDuJoueur.id)
                self.modes["planetes"][planeteDuJoueur.id]=s
                s.initplanete(systeme.id,planeteDuJoueur.id)
        
        planeteInit = mod.joueurs[self.nom].maplanete
        systeme = planeteInit.parent
        self.voirsysteme(systeme)
        
        sysid=systeme.id
        planeid=planeteInit.id
        if planeid in self.modes["planetes"].keys():
            s=self.modes["planetes"][planeid]
        else:
            s=VuePlanete(self,sysid,planeid)
            self.modes["planetes"][planeid]=s
            s.initplanete(sysid,planeid)
        self.changemode(s)
        
    def effacerBatiment(self,planeteid,nom,batimentid):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images[nom]
                self.modes["planetes"][i].effacerBatiment(batimentid)
      
    def afficherBatiment(self,nomjoueur,systemeid,planeteid,x,y,nom,batimentid):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images[nom]
                self.modes["planetes"][i].afficherBatiment(x, y, im, (nomjoueur, planeteid,x ,y ,nom, batimentid))
                
    def affichervehiculetank(self,joueur,systemeid,planeteid,x,y,idvehicule):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["vehiculetankhaut"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,"vehiculetank",idvehicule) ) 
    
    def affichervehiculehelicoptere(self,joueur,systemeid,planeteid,x,y,idvehicule):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["vehiculehelicopterebas"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,"vehiculehelicoptere",idvehicule) ) 

    def afficherbouclier(self,joueur,systemid,planeteid,x,y,couleur, nomBatiment):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                self.modes["planetes"][i].canevas.create_oval(x-250,y-250,x+250,y+250,outline= couleur, width = 5)
                im = self.modes["planetes"][i].images["Bouclier"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,nomBatiment))


    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        self.parent.fermefenetre()
        
if __name__ == '__main__':
    m=Vue(0,"jmd","127.0.0.1")
    m.root.mainloop()
