import re

def ab(text):
    pattern = 'ab*'
    return re.findall(pattern, text)
def ab23(text):
    pattern = 'ab{2,3}'
    return re.findall(pattern, text)
def lowercasesequences(text):
    pattern = '[a-z]+_[a-z]+'
    return re.findall(pattern, text)
def ubl(text):
    pattern = '[A-Z][a-z]+'
    return re.findall(pattern, text)
def endb(text):
    pattern = 'a.*b$'
    return re.findall(pattern, text)
def dcolon(text):
    return re.sub('[ ,.]', ':', text)
def snaketocamel(text):
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
def split(text):
    return re.findall('[A-Z][^A-Z]*', text)
def insert(text):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)
def cameltosnake(text):
    return re.sub(r'(?<=\w)([A-Z])', r'_\1', text).lower()  

def readfile(x):
    with open(x, 'r', encoding='utf-8') as file:
        return file.read()


file_path = 'C:/Users/HVNAERO/Desktop/labspp2/labs5/ew.txt'

text = readfile(file_path)

a = ab(text)
b = ab23(text)
c = lowercasesequences(text)
d = ubl(text)
e = endb(text)
f = dcolon(text)
g = split(text)
h = insert(text)
i = snaketocamel(text)
j = cameltosnake(text)

print(a,b,c,d,e,f,g,h,i,j)