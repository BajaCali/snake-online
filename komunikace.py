from Communication.tcp import Tcp as comu #knihovna komunikace
##pepa = comu('192.168.42.64',12345, encoding = 'utf8', decoding = 'utf8')
##pepa.write("Ahoj")
##pepa.timeout=10
##print(pepa.read(11))
##pepa.close()

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

