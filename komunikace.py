#! python 3

def slucovani(slovnik):
    
    return str(slovnik),len(str(slovnik))

def deleni(text):
    slovnik={}
    a=''
    b=''
    move=0
    ##print("\n\n")   
    for i in range(len(text)):
        ##print(text[i],end="")
        if(move!=1):
            if text[i]==':':
                b=a
                a=""
            elif text[i]==',':
                slovnik[b]=a
                a=''
                b=''
            elif text[i]=='{' and a=="":
                a = deleni(text[i+1:-1])
                move=1
            elif text[i]=='}':
                slovnik[b]=a
                return slovnik
            else:
                a+=text[i]
        elif(text[i]=="}"):
            move=0

print(deleni("{'ahoj': 'ahojky', 'kolo': 'helma', 'helma': 'kolo', 'b': 'a', 'he': {'pole': 'Brno', 'metropole': 'kurim'}, 'she': 'nothing'}"))
