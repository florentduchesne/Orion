# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageDraw, ImageTk
import os,os.path
from helper import Helper as hlp
from OE_vueGalaxie import VueGalaxie
from OE_vueSysteme import VueSysteme
from OE_vuePlanete import VuePlanete

class Vue():
    def __init__(self,parent,ip,nom,largeur=800,hauteur=600):
        self.root=Tk()
        self.root.title(os.path.basename(sys.argv[0]))
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
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
        
        self.cadreRessourcesJoueur = Frame(self.cadrejeu,height=40,bg="SpringGreen3")
        self.cadreRessourcesJoueur.pack(fill=X)
        
        self.cadreRessourcesPlanete = Frame(self.cadrejeu,height=40,bg="SpringGreen4")
        self.cadreRessourcesPlanete.pack(fill=X)
        self.titrePlanete = Label(self.cadreRessourcesPlanete,text="Planete",bg="SpringGreen4")
        self.titrePlanete.grid(row=0,column=0)
        self.envoyerRessourcesVersCadreJoueur()
        
    def envoyerRessourcesVersCadreJoueur(self):
        self.chargerImagesRes()
        i = 0
        self.titreJoueur = Label(self.cadreRessourcesJoueur,text="Joueur: ",bg="SpringGreen3")
        self.titreJoueur.grid(row=0,column=i)
        i+=1
        self.imgUra = Label(self.cadreRessourcesJoueur,image=self.images["uranium"],bg="SpringGreen3")
        self.imgUra.grid(row=0,column=i)
        i+=1
        self.imgTita = Label(self.cadreRessourcesJoueur,image=self.images["titanium"],bg="SpringGreen3")
        self.imgTita.grid(row=0,column=i)
        i+=1
        self.imgLac = Label(self.cadreRessourcesJoueur,image=self.images["lacrima"],bg="SpringGreen3")
        self.imgLac.grid(row=0,column=i)
        i+=1
        self.imgSante = Label(self.cadreRessourcesJoueur,image=self.images["sante"],bg="SpringGreen3")
        self.imgSante.grid(row=0,column=i)
        i+=1
        self.imgptScience = Label(self.cadreRessourcesJoueur,image=self.images["point_Science"],bg="SpringGreen3")
        self.imgptScience.grid(row=0,column=i)
        i+=1
        self.imgNourr = Label(self.cadreRessourcesJoueur,image=self.images["nourriture"],bg="SpringGreen3")
        self.imgNourr.grid(row=0,column=i)
        i+=1
        self.imgHum = Label(self.cadreRessourcesJoueur,image=self.images["humain"],bg="SpringGreen3")
        self.imgHum.grid(row=0,column=i)
        i+=1
        self.imgElec = Label(self.cadreRessourcesJoueur,image=self.images["electricite"],bg="SpringGreen3")
        self.imgElec.grid(row=0,column=i)
        i+=1
        self.imgEau = Label(self.cadreRessourcesJoueur,image=self.images["eau"],bg="SpringGreen3")
        self.imgEau.grid(row=0,column=i)
        i+=1
        self.imgBr = Label(self.cadreRessourcesJoueur,image=self.images["bronze"],bg="SpringGreen3")
        self.imgBr.grid(row=0,column=i)
        i+=1
        self.imgBio = Label(self.cadreRessourcesJoueur,image=self.images["biohazard"],bg="SpringGreen3")
        self.imgBio.grid(row=0,column=i)
        i+=1
        self.imgChar = Label(self.cadreRessourcesJoueur,image=self.images["charbon"],bg="SpringGreen3")
        self.imgChar.grid(row=0,column=i)
        i+=1
        self.imgAr = Label(self.cadreRessourcesJoueur,image=self.images["argent"],bg="SpringGreen3")
        self.imgAr.grid(row=0,column=i)
        i+=1
        self.imgBois = Label(self.cadreRessourcesJoueur,image=self.images["bois"],bg="SpringGreen3")
        self.imgBois.grid(row=0,column=i)
        i+=1
        self.imgMet = Label(self.cadreRessourcesJoueur,image=self.images["metasic"],bg="SpringGreen3")
        self.imgMet.grid(row=0,column=i)
        i+=1
        self.imgMoral = Label(self.cadreRessourcesJoueur,image=self.images["moral"],bg="SpringGreen3")
        self.imgMoral.grid(row=0,column=i)
        i+=1
    
    def chargerImagesRes(self):
        l = 18
        h = 18
        im = Image.open("./images/icone_Ressources/uranium.png").resize((int(l),int(h)))
        self.images["uranium"] = ImageTk.PhotoImage(im) 
        im = Image.open("./images/icone_Ressources/titanium.png").resize((l,h))
        self.images["titanium"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/lacrima.png").resize((l,h))
        self.images["lacrima"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/sante.png").resize((l,h))
        self.images["sante"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/point_Science.png").resize((l,h))
        self.images["point_Science"] = ImageTk.PhotoImage(im)
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
        im = Image.open("./images/icone_Ressources/biohazard.png").resize((l,h))
        self.images["biohazard"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/charbon.png").resize((l,h))
        self.images["charbon"] = ImageTk.PhotoImage(im)
        im = Image.open("./images/icone_Ressources/argent.png").resize((l,h))
        self.images["argent"] = ImageTk.PhotoImage(im)
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
                self.modes["planetes"][i].afficherBatiment(x, y, im)
                
    """def affichermine(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["mine"]
                self.modes["planetes"][i].afficherMine(x, y, im)
                #self.modes["planetes"][i].canevas.create_image(x,y,image=im)
                #self.modes["planetes"][i].minimap.create_oval(minix-2,miniy-2,minix+2,miniy+2,fill="white")
                """
    def affichervehiculetank(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["vehiculetank"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im, tags = (x ,y ,"vehiculetank"))   
    """
    def affichertour(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["tour"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im)
    
    def affichermur(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["mur"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im)
                
    def affichercanon(self,joueur,systemeid,planeteid,x,y):
        for i in self.modes["planetes"].keys():
            if i == planeteid:
                im=self.modes["planetes"][i].images["canon"]
                self.modes["planetes"][i].canevas.create_image(x,y,image=im)"""
                                
    def fermerfenetre(self):
        # Ici, on pourrait mettre des actions a faire avant de fermer (sauvegarder, avertir etc)
        self.parent.fermefenetre()
        
if __name__ == '__main__':
    m=Vue(0,"jmd","127.0.0.1")
    m.root.mainloop()
