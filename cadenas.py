from string import whitespace, punctuation
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
message=input("Ingrese una cadena de texto:\n")

def mayusculasPrincipio():
    array=list(message)
    if array[0].isupper():
        print('True')
    else:
        print('False')
        
def numeroLetras():
    count=message.split()
    print("Cantidad de palabras: ", len(count))

def crearLista(message):
    array=list(message)
    return array

def invertida():
    return message[::-1]

def mayusculasTexto():
    values=""
    for i in message:
        if i.isupper():
            values+=''.join(i)
    return values

def validarCorreo(email):
 
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")

mayusculasPrincipio()
numeroLetras()
print(crearLista(message))
print(invertida())
print(mayusculasTexto())

dataEmail=str(input("Ingrese su correo: "))
validarCorreo(dataEmail)