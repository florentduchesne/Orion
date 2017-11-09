# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import os,os.path
from collections import OrderedDict
from helper import Helper as hlp
from OE_vueGalaxie import VueGalaxie
from OE_vueSysteme import VueSysteme
from OE_vuePlanete import VuePlanete

class Vue():
    def __init__(self,parent,ip,nom,largeur=800,hauteur=600):
        self.root=Tk()
        self.root.title(os.path.basename(sys.argv[0]))
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
        
        self.cadreRessourcesJoueur = Frame(self.cadrejeu,height=40,bg="LightSteelBlue4")
        self.cadreRessourcesJoueur.pack(fill=X)
        
        self.cadreRessourcesPlanete = Frame(self.cadrejeu,height=40,bg="SkyBlue4")
        self.cadreRessourcesPlanete.pack(fill=X)
        
        self.envoyerRessourcesVersCadreJoueur()
        self.envoyerRessourcesVersCadrePlanete()
        
    def envoyerRessourcesVersCadreJoueur(self):
        
        self.chargerImagesRes()
        i = 0
        couleur = "LightSteelBlue4"
        cadre = self.cadreRessourcesJoueur
        
        self.titreJoueur = (Label(cadre,image=self.images["joueur"],bg=couleur), Label(cadre,text="Joueur: ",bg=couleur))
        self.titreJoueur[0].grid(row=0,column=i)
        i = 1
        self.titreJoueur[1].grid(row=0,column=i)
        
        self.dictionnaireLabelsJoueur["humain"] = (Label(cadre,image=self.images["humain"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["electricite"] = (Label(cadre,image=self.images["electricite"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["moral"] = (Label(cadre,image=self.images["moral"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["nourriture"] = (Label(cadre,image=self.images["nourriture"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["eau"] = (Label(cadre,image=self.images["eau"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["bois"] = (Label(cadre,image=self.images["bois"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["bronze"] = (Label(cadre,image=self.images["bronze"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["charbon"] = (Label(cadre,image=self.images["charbon"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["uranium"] = (Label(cadre,image=self.images["uranium"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["titanium"] = (Label(cadre,image=self.images["titanium"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["metasic"] = (Label(cadre,image=self.images["metasic"],bg=couleur), Label(cadre,text="0",bg=couleur))
        #self.dictionnaireLabelsJoueur["sante"] = (Label(cadre,image=self.images["sante"],bg=couleur), Label(cadre,text="0",bg=couleur))   
        #self.dictionnaireLabelsJoueur["argent"] = (Label(cadre,image=self.images["argent"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsJoueur["point_science"] = (Label(cadre,image=self.images["point_science"],bg=couleur), Label(cadre,text="0",bg=couleur))
        
        i = 2
        
        for d in self.dictionnaireLabelsJoueur:
            self.dictionnaireLabelsJoueur[d][0].grid(row=0, column = i)
            i += 1
            self.dictionnaireLabelsJoueur[d][1].grid(row=0, column = i)
            i += 1
        
    def envoyerRessourcesVersCadrePlanete(self):
        i = 0
        couleur = "SkyBlue4"
        cadre = self.cadreRessourcesPlanete
        self.titrePlanete = (Label(cadre,image=self.images["planet"],bg=couleur), Label(cadre,text="Planète: ",bg=couleur))
        self.titrePlanete[0].grid(row=0,column=i)
        i = 1
        self.titrePlanete[1].grid(row=0,column=i)
        
        self.dictionnaireLabelsPlanete["humain"] = (Label(cadre,image=self.images["humain"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["electricite"] = (Label(cadre,image=self.images["electricite"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["moral"] = (Label(cadre,image=self.images["moral"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["nourriture"] = (Label(cadre,image=self.images["nourriture"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["eau"] = (Label(cadre,image=self.images["eau"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["bois"] = (Label(cadre,image=self.images["bois"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["bronze"] = (Label(cadre,image=self.images["bronze"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["charbon"] = (Label(cadre,image=self.images["charbon"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["uranium"] = (Label(cadre,image=self.images["uranium"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["titanium"] = (Label(cadre,image=self.images["titanium"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["metasic"] = (Label(cadre,image=self.images["metasic"],bg=couleur), Label(cadre,text="0",bg=couleur))
        #self.dictionnaireLabelsPlanete["sante"] = (Label(cadre,image=self.images["sante"],bg=couleur), Label(cadre,text="0",bg=couleur))
        #self.dictionnaireLabelsPlanete["argent"] = (Label(cadre,image=self.images["argent"],bg=couleur), Label(cadre,text="0",bg=couleur))
        self.dictionnaireLabelsPlanete["point_science"] = (Label(cadre,image=self.images["point_science"],bg=couleur), Label(cadre,text="0",bg=couleur))
        
        
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
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(self.parent.modele.joueurs[i].ressources.dictRess["allocation humain"])+" / "+str(self.parent.modele.joueurs[i].ressources.dictRess[j]))
                    elif j == "electricite":
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(self.parent.modele.joueurs[i].ressources.dictRess["allocation electricite"])+" / "+str(self.parent.modele.joueurs[i].ressources.dictRess[j]))
                    else:
                        self.dictionnaireLabelsJoueur[j][1].config(text = str(self.parent.modele.joueurs[i].ressources.dictRess[j]))
        if(isinstance(self.modecourant, VuePlanete)):
            for systeme in self.parent.modele.systemes:
                for planete in systeme.planetes:
                    if(planete.id == self.modecourant.planeteid):
                        for j in self.dictionnaireLabelsPlanete: 
                            if j == "humain":
                                self.dictionnaireLabelsPlanete[j][1].config(text = str(planete.ressource.dictRess["allocation humain"])+" / "+str(planete.ressource.dictRess[j]))
                            elif j == "electricite":
                                self.dictionnaireLabelsPlanete[j][1].config(text = str(planete.ressource.dictRess["allocation electricite"])+" / "+str(planete.ressource.dictRess[j]))
                            else:
                                self.dictionnaireLabelsPlanete[j][1].config(text = str(planete.ressource.dictRess[j]))
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
        self.cadresplash=Frame(self.root)
        self.canevasplash=Canvas(self.cadresplash,width=640,height=480,bg="red")
        self.canevasplash.pack()
        self.nomsplash=Entry(bg="pink")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="pink")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="red",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Creer partie",bg="pink",command=self.creerpartie)
        btnconnecterpartie=Button(text="Connecter partie",bg="pink",command=self.connecterpartie)
        self.canevasplash.create_window(200,200,window=self.nomsplash,width=100,height=30)
        self.canevasplash.create_window(200,250,window=self.ipsplash,width=100,height=30)
        self.canevasplash.create_window(200,300,window=labip,width=100,height=30)
        self.canevasplash.create_window(200,350,window=btncreerpartie,width=100,height=30)
        self.canevasplash.create_window(200,400,window=btnconnecterpartie,width=100,height=30) 
        
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.root)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="lightblue")
        self.canevaslobby.pack()
        self.listelobby=Listbox(bg="red",borderwidth=0,relief=FLAT)
        self.diametre=Entry(bg="pink")
        self.diametre.insert(0, 50)
        self.densitestellaire=Entry(bg="pink")
        self.densitestellaire.insert(0, 25)
        self.qteIA=Entry(bg="pink")
        self.qteIA.insert(0, 0)
        self.btnlancerpartie=Button(text="Lancer partie",bg="pink",command=self.lancerpartie,state=DISABLED)
        self.canevaslobby.create_window(440,240,window=self.listelobby,width=200,height=400)
        self.canevaslobby.create_window(250,200,window=self.diametre,width=100,height=30)
        self.canevaslobby.create_text(90,200,text="Diametre en annee lumiere")
        
        self.canevaslobby.create_window(250,250,window=self.densitestellaire,width=100,height=30)
        self.canevaslobby.create_text(90,250,text="Nb systeme/AL cube")
        
        self.canevaslobby.create_window(250,300,window=self.qteIA,width=100,height=30)
        self.canevaslobby.create_text(90,300,text="Nb d'IA")
        
        self.canevaslobby.create_window(250,450,window=self.btnlancerpartie,width=100,height=30)

    def voirgalaxie(self):
        # A FAIRE comme pour voirsysteme et voirplanete, tester si on a deja la vuegalaxie
        #         sinon si on la cree en centrant la vue sur le systeme d'ou on vient
        s=self.modes["galaxie"]
        self.changemode(s) 
       
    def voirsysteme(self,systeme=None):
        if systeme:
            sid=systeme.id
            if sid in self.modes["systemes"].keys():
                s=self.modes["systemes"][sid]
            else:
                s=VueSysteme(self)
                self.modes["systemes"][sid]=s
                s.initsysteme(systeme)
            self.changemode(s)
        
    def voirplanete(self,maselection=None):
        s=self.modes["planetes"]
        
        if maselection:
            sysid=maselection[5]
            planeid=maselection[2]
            if planeid in self.modes["planetes"].keys():
                s=self.modes["planetes"][planeid]
                self.cadreRessourcesPlanete.pack(fill=X)
            else:
                s=VuePlanete(self,sysid,planeid)
                self.modes["planetes"][planeid]=s
                s.initplanete(sysid,planeid)
                self.cadreRessourcesPlanete.pack(fill=X)
            self.changemode(s)
        else:
            print("aucune planete selectionnee pour atterrissage")
     
        
        
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
       
        diametre=self.diametre.get()
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
      
    def afficherBatiment(self,joueur,systemeid,planeteid,x,y,nom):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images[nom]
                self.modes["planetes"][i].afficherBatiment(x, y, im, (joueur, planeteid,x ,y ,nom))
                
    def affichervehiculetank(self,joueur,systemeid,planeteid,x,y,idvehicule):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["vehiculetank"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,"vehiculetank",idvehicule) ) 
    
    def affichervehiculecharassaut(self,joueur,systemeid,planeteid,x,y,idvehicule):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["vehiculecharassaut"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,"vehiculecharassaut",idvehicule) ) 

    def afficherbouclier(self,joueur,systemid,planeteid,x,y,couleur, nomBatiment):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                print("creation bouclier")
                self.modes["planetes"][i].canevas.create_oval(x-250,y-250,x+250,y+250,outline= couleur, width = 5)
                im = self.modes["planetes"][i].images["Bouclier"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (joueur, planeteid,x ,y ,nomBatiment))


    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        self.parent.fermefenetre()
        
if __name__ == '__main__':
    m=Vue(0,"jmd","127.0.0.1")
    m.root.mainloop()
