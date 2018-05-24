#! python3
from Communication.tcp import Client as comu #knihovna komunikace from Communication.tcp import client as server
import pygame#mozna pygame
import ast

##konstanty
tyrkysova=(50,230,180)
cervena=(255,50,50)
zluta=(150,150,0)
cerna=(0,0,0)

green=(50,250,50)

fps=(1000/30)

velikos_x=1500
velikost_y=750
pygame.init()

class uzivatel:
    def __init__(self,ip,port):
        print("Jo kolo se toci")
        self.out = comu(ip,port, encoding = 'utf8', decoding = 'ASCII',noexcept=False)
        if (self.out.connected==False):
            print("Pripojeni bylo neuspesne")
        print("A prece se toci")
        self.mantisa=4
        self.delka=0
        



        

    def wait(self):#ceka na mantisu
        cmd=self.out.read(mantisa)
        
        if cmd=={} and int(cmd)==0:
            return False
        self.delka=int(cmd)
        return True
    
    def lisen(self):#ceka na prijmu a vrati prijem
        self.delka=0
        
        if self.wait():
            dic = {}
            try:
                dic = ast.literal_eval(pepa.read(self.delka))
            except:
                print("Wrong dict data input.")
                return 0
        return dic

    def odeslani(self,slovnik):
        #print(ord(str(slovnik)))
        text=slucovani(str(slovnik))
        
        self.out.write(len(text))#velikoxt
        self.out.write(text)#sprava
        print(len(text))
        print(text)

my={'name': "Otakar","color":(50,50,50),"score":0 }
#hrac=uzivatel('127.0.0.1',1234)
#hrac=uzivatel('192.168.42.102',11111)
hrac=uzivatel('192.168.42.71',1234)
if (hrac.out.connected):
    print("pripojeno")
    

