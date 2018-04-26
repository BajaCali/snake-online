from Communication.tcp import Client as comu #knihovna komunikace from Communication.tcp import client as server
import pygame as pyp#mozna pygame
import ast

##konstanty
tyrkysova=(50,230,180)
cervena=(255,50,50)
zluta=(150,150,0)
cerna=(0,0,0)

green=(50,250,50)
fps=(1000/30)


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
        self.delka=0

    def wait(self):#ceka na mantisu
        cmd=pepa.read(mantisa)
        
        if cmd=={} and int(cmd)==0:
            return False
        self.delka=int(cmd)
        return True
    
    def lisen(self):#ceka na prijmu a vrati prijem
        self.delka=0
        
        
        dic = {}
        try:
            dic = ast.literal_eval(pepa.read(self.delka))
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
        self.x=dic["x"]
        self.y=dic["y"]
        self.mapa=dic["map"]
        self.screen=screen#Jde to
        self.polomer=10

        self.hadove=[]
        i=0
        self.pocet=dic["snakes"]
        for i in range(self.pocet):
            self.hadove.append(dic[i])#slovnik ve slovniku

        self.barva_zdi
        self.barva_cil
        
    def kresli(self):
        screen.fill(cerna)
        for y in range(self.y):
            for x in range(self.y):
                if self.mapa[x][y]==chr(0):
                    pass
                if self.mapa[x][y]==chr(1):
                    pygame.draw.rect(self.screen, self.barva_zdi, (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
                if self.mapa[x][y]==chr(2):
                    pygame.draw.circle(self.screen, self.barva_cil, (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
                if chr(pocet+100)=>self.mapa[x][y]>chr(100):  
                    pygame.draw.circle(self.screen, self.hadove[ord(self.mapa[x][y]-101)]["color"], (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
        pygame.display.flip()##mozna ma byt v mainu

        
 
                    


    def update(self,dic):
        self.mapa=dic["map"]
        self.screen=screen#Jde to
        self.polomer=10

        self.hadove=[]
        i=0
        self.pocet=dic["snakes"]
        for i in range(self.pocet):
            self.hadove.append(dic[i])#slovnik ve slovniku
        
        return 

    def pohyb(self):
        
        
        pass

#main

screen = pygame.display.set_mode((width, height),)#pamatuje si obrazovku surface - screen -cokoli do ni zapisu se da prikazem vykreslit
konec=1

pygame.time.set_timer(pygame.USEREVENT+1,int(fps))
klavesy=[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]


while(konec==1):
    novy_smer
    smer
    event=pygame.event.wait()

    if(event.type==pygame.QUIT):
        konec=0
        print("By")
        break
    if(event.type==pygame.KEYDOWN):
        a=event.key
            if(button==klavesy[0] or button==klavesy[4]):
            if(smer!=2):
                novy_smer=1
                #print("jsem tu")
        elif(button==(klavesy[1] or button==klavesy[4])):
            if(smer!=1):
                novy_smer=2
                #print("jsem tu")
        elif(button==(klavesy[2] or button==klavesy[4])):
            if(smer!=4):
                novy_smer=3
                #print("jsem tu")
        elif(button==(klavesy[3] or button==klavesy[4])):
            if(smer!=3):
                novy_smer=4
                #print("jsem tu")
                #[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]



    odeslani(chr(novy_smer))
    smer=novy_smer



        if konec==0:
            break





    



