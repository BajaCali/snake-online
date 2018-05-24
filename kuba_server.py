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
    def __init__(self,ip,port):
        print("Jo kolo se toci")
        self.out = comu(ip,port, encoding = 'utf8', decoding = 'utf8',noexcept=False)
        if (self.out.connected==False):
            print("Pripojeni bylo neuspesne")
        print("A prece se toci")
        self.mantisa=4
        self.delka=0



        

    def wait(self):#ceka na mantisu
        cmd=self.out.read(self.mantisa)
        
        if cmd=={} and int(cmd)==0:
            return False
        self.delka=int(cmd)
        return True
    
    def lisen(self):#ceka na prijmu a vrati prijem
        self.delka=0
        pole[]
        i=0
        pole.append()
        while(i=='!'):
            i=
        
        return 

    def odeslani(self,slovnik):
        #print(ord(str(slovnik)))
        #text=slucovani(str(slovnik))
        
        #self.out.write(len(text))#velikoxt
        self.out.write(text)#sprava



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

        self.barva_zdi=(150,150,0)
        self.barva_cil=(250,50,50)
        
    def kresli(self):
        screen.fill(cerna)
        print(self.mapa)



        
##        for y in range(self.y):
##            for x in range(self.y):
##                if self.mapa[x][y]==chr(0):
##                    pass
##                if self.mapa[x][y]==chr(1):
##                    pygame.draw.rect(self.screen, self.barva_zdi, (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
##                if self.mapa[x][y]==chr(2):
##                    pygame.draw.circle(self.screen, self.barva_cil, (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
##                if chr(pocet+100)>=self.mapa[x][y]>chr(100):  
##                    pygame.draw.circle(self.screen, self.hadove[ord(self.mapa[x][y])-101]["color"], (x*polomer*2,y*polomer*2,polomer*2,polomer*2),0)
##        pygame.display.flip()##mozna ma byt v mainu

        
 
                    


    def update(self,dic):
        self.mapa=dic#["map"]
        self.screen=screen#Jde to
        self.polomer=10

        #self.hadove=[]
        #i=0
        #self.pocet=dic["snakes"]
        #for i in range(self.pocet):
        #    self.hadove.append(dic[i])#slovnik ve slovniku

        return 


#main
print("Jmeno hada:",end="")
jmeno=input()
print (jmeno)

screen = pygame.display.set_mode((velikos_x,velikost_y))#(width, height)pamatuje si obrazovku surface - screen -cokoli do ni zapisu se da prikazem vykreslit
konec=0

pygame.time.set_timer(pygame.USEREVENT+1,100)
text = pygame.font.SysFont('arial', 50)#
r=0
g=0
b=0
event=pygame.event.wait()
while(konec==0):
    event=pygame.event.wait()
    print("kolo")
    if(event.type==pygame.KEYDOWN):
        a=event.key
        konec=1
    pygame
    r+=17
    g+=19
    b+=23
    r=r%255
    g=g%255
    b=b%255
    pygame.draw.circle(screen, (r,b,g), (int(velikos_x/2),int(velikost_y/2)),500)
    pygame.display.flip()

konec=1
pygame.time.set_timer(pygame.USEREVENT+1,int(fps))

klavesy=[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]
hrac=uzivatel('192.168.42.71',1234)
#hrac=uzivatel('192.168.42.103',11111) # 2 michal
#hrac=uzivatel('192.168.42.71',1234)#kuba -1
#hrac=uzivatel('127.0.0.1',1234)#sobe
#init pro michamla nize
#my={'name': jmeno,"color":(r,g,b),"score":0 }


#hrac.odeslani(my)
novy_smer=0
hrac.odeslani("w")
smer=0
malovani=Grafika(screen,hrac.lisen())
while(konec==1):
    
    event=pygame.event.wait()

    if(event.type==pygame.QUIT):
        konec=0
        print("By")
        break
    #print("kolot")
    if(event.type==pygame.KEYDOWN):
        print("kolo")
        button=event.key##??buton<--a
        if(button==klavesy[0] or button==klavesy[4]):
            if(smer!=2):
                novy_smer="w"
                #print("jsem tu")
        elif(button==(klavesy[1] or button==klavesy[4])):
            if(smer!=1):
                novy_smer="s"
                #print("jsem tu")
        elif(button==(klavesy[2] or button==klavesy[4])):
            if(smer!=4):
                novy_smer="a"
                #print("jsem tu")
        elif(button==(klavesy[3] or button==klavesy[4])):
            if(smer!=3):
                novy_smer="d"
                #print("jsem tu")
                #[pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]

        hrac.odeslani(chr(smer))
        smer=novy_smer
    #print("kolo")
    #print("k")
    malovani.update(screen,hrac.lisen())
    malovani.kresli()

    if konec==0:
        break

pygame.quit()



    



