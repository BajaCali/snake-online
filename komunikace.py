from Communication.tcp import Client as comu #knihovna komunikace from Communication.tcp import client as server
import pigame as pyp
#pepa = comu('192.168.42.64',12345, encoding = 'utf8', decoding = 'utf8')
#pepa.write("Ahoj")
#pepa.timeout=10
#print(pepa.read(11))
##pepa.close()
class uzivatel:
    def __init__(self):
        self.mantisa=4


    def del_max(self):
        return 10^(self.mantisa+1)-1
        
    def wait(self):
        delka int(pepa.read(mantisa))
        if(delka==self.del_max()):
            self.mantisa=self.mantisa*2
            delka=self.wait()
            self.mantisa=self.mantisa/2
        return delka
    
    def lisen(self):
        delka=self.wait()
        dic = {}
        try:
            dic = ast.literal_eval(pepa.read(delka))
        except:
            print("Wrong dict data input.")
            return 0
        return dic

    def odeslani(self,slovnik):
    {
        text=slucovani(str(slovnik))
        pepa.write(len(text))#velikoxt
        pepa.write(text)#sprava
    }

    



