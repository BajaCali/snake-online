#! python 3

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

slovnik={}
slovnik["a"]="b"
slovnik[slovnik["a"]]="c"
slovnik[slovnik["b"]]="abc"
Parse(slucovani(slovnik))
