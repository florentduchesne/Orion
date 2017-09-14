import threading
from OE_objets import *
from time import sleep

class ThreadRessources(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.termine = False
    
    def run(self):
        while (not self.termine):
            try:
                self.systemes = self.parent.modele.systemes
                sleep(5)
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
            except:
                pass