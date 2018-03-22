#! python3

integers = [
    'dir',
    'height',
    'width',
    'skore'
    ]

strings = [
    'name',
    'map'
    ]

snakes = [
    'a',
    'b'
    ]

def to_int(text, thing):
    pos = text.find(thing)
    if (pos > 0):
        end = text.find(",", pos)
        if (end == -1):
            end = text.find("}", pos)
            if (end == -1):
                return -1
        return int(text[pos + len(thing) + 2:end])
    else:
        return -1
    
def to_string(text, thing):
    pos = text.find(thing)
    if (pos > 0):
        end = text.find(",", pos)
        if (end == -1):
            end = text.find("}", pos)
            if (end == -1):
                return -1
        return text[pos + len(thing) + 3:end-1]
    else:
        return ""
    

def parse(dictionary, text, ints, strs, snakes):
    for i in ints:
        pos = text.find(i)
        if (pos > 0):
            num = to_int(text, i)
            if (num > 0):
                dictionary[i] = num
    for s in strs:
        pos = text.find(s)
        if (pos != -1):
            string = to_string(text, s)
            if (string > ""):
                dictionary[s] = string
    for snake in snakes:
        pos = text.find(snake +':')
        if (pos != -1):
            dictionary[str[snake]] = parse(dictionary, text[pos+2:text.find('}',pos)], integers, strs, snakes)        
    return dictionary

print(to_int("{dir: 555}", "dir"))

dic ={}
text = "{dir: 12, height: 6, map: \'blablabal\', a = {name: \'Jenda\'}}"
print(parse(dic, text, integers, strings, snakes))
