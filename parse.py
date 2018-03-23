#! python3

import ast

def Parse(text):
    dic = {}
    try:
        dic = ast.literal_eval(text)
    except:
        print("Wrong dict data input.")
    return dic


