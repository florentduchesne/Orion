
class TuileGazon():
    def __init__(self,x,y,image):
        self.taille = 100
        self.image=image
        self.x = x
        self.y = y
        self.estPrise = '0'
        
    def changerValeurTuile(self, t):
        t.estPrise = True