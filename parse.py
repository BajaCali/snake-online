#! python3

import ast

def Parse(text):
    dic = {}
    try:
        dic = ast.literal_eval(text)
    except:
        print("Wrong dict data input.")
    return dic

print(to_int("{dir: 555}", "dir"))

dic ={}
text = "{'dir': 12, 'height': 6, 'map': \'blablabal\', 'a': {'name': \'Jenda\'}}"
print(Parse(text))
print(parse(dic, text, integers, strings, snakes))


