from Communication.tcp import Client as comu #knihovna komunikace from Communication.tcp import client as server
import pygame as pyp#mozna pygame
import ast
def slucovani(slovnik):



    return str(slovnik)##,len(str(slovnik)


def Parse(text):
    dic = {}
    try:
        dic = ast.literal_eval(text)
    except:
        print("Wrong dict data input.")
        return 0
    return dic
#pepa = comu('192.168.42.64',12345, encoding = 'utf8', decoding = 'utf8')
#pepa.write("Ahoj")
#pepa.timeout=10
#print(pepa.read(11))
##pepa.close()
class uzivatel:
    def __init__(self):
        self.mantisa=4

    def wait(self):#ceka na mantisu
        delka=int(pepa.read(mantisa))
        if delka==0:
        return delka
    
    def lisen(self):#ceka na prijmu a vrati prijem
        delka=0
        while not delka:
            delka=self.wait()
        
        dic = {}
        try:
            dic = ast.literal_eval(pepa.read(delka))
        except:
            print("Wrong dict data input.")
            return 0
        return dic

    def odeslani(self,slovnik):
        text=slucovani(str(slovnik))
        pepa.write(len(text))#velikoxt
        pepa.write(text)#sprava



#################################################main.10
#
#
#
#
class Grafika:
    
    def __init__(self,screen,dic):
        self.x=dick["x"]
        self.y=dick["y"]
        self.zdi=[dick["zdi"]]
        #self.mapa=dic["mapa"]
        self.screen=screen
        self.polomer=10

        self.hadove=[]
        i=0
        while i in dic:
            self.hadove.append(dic[i])#slovnik ve slovniku
            i+=1
            
    def vypis_hada(self,had):
        for i in had["body"]:
            pygame.draw.circle(self.screen, had["barva"],(i[0]*self.polomer*2+self.polomer,i[1]*self.polomer*2+self.polomer),self.polomer,0)


    def out(self):
        screen.fill(cerna)
        for obekt in self.zdi:
            pygame.draw.rect(self.screen, zluta, (obekt[0]*polomer*2,obekt[1]*polomer*2,polomer*2,polomer*2),0)
        for obekt in self.hadove:
            self.vypis_hada(obekt)
        for obekt in self.cile:
            pygame.draw.circle(screen, cervena,(obekt[0]*polomer*2+polomer,obekt[1]*polomer*2+polomer),polomer,0)
       pygame.display.flip()

    def update(self,dic):
        for obekt in dick["zdi"]:
            self.zdi.append(obekt)
                self.hadove=[]
        i=0
        while i in dic:
            self.hadove.append(dic[i])#slovnik ve slovniku
            i+=1
        return 0

    def pohyb(self):
        
        pass








    



