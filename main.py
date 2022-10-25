from calendar import month
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Union
import json
from datetime import date

oficio ="oficio.txt"

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def getDocs():
    data = open('people.json')
    people = json.load(data)
    docsArray = []
    for person in people:
        with open(oficio, 'r') as file :
            filedata = file.read()

            filedata = filedata.replace('${nombre}', person['nombre'])
            filedata = filedata.replace('${apellido1}', person['apellido1'])
            filedata = filedata.replace('${apelldo2}', person['apelldo2'])
            filedata = filedata.replace('${cargo}', person['cargo'])
            filedata = filedata.replace('${empresa}', person['empresa'])
            filedata = filedata.replace('${calle}', person['calle'])
            filedata = filedata.replace('${numCalle}', str(person['numCalle']))
            filedata = filedata.replace('${colonia}', person['colonia'])
            filedata = filedata.replace('${municipio}', person['municipio'])
            filedata = filedata.replace('${estado}', person['estado'])
            filedata = filedata.replace('${codigoPostal}', str(person['codigoPostal']))
            filedata = filedata.replace('${telefono}', str(person['telefono']))
            filedata = filedata.replace('${email}', person['email'])

            def age(birthdate):
                today = date.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                return age

            filedata = filedata.replace('${edad}', str(age(date(person['yearNacimiento'], person['monthNacimiento'], person['dayNacimiento']))))

            docsArray.append(filedata)
            data.close()
    return docsArray



def getDocByName(name):
    data = open('people.json')
    people = json.load(data)
    for person in people:
        with open(oficio, 'r') as file :
            if person['nombre'].lower() == name:
                filedata = file.read()
            
                filedata = filedata.replace('${nombre}', person['nombre'])
                filedata = filedata.replace('${apellido1}', person['apellido1'])
                filedata = filedata.replace('${apelldo2}', person['apelldo2'])
                filedata = filedata.replace('${cargo}', person['cargo'])
                filedata = filedata.replace('${empresa}', person['empresa'])
                filedata = filedata.replace('${calle}', person['calle'])
                filedata = filedata.replace('${numCalle}', str(person['numCalle']))
                filedata = filedata.replace('${colonia}', person['colonia'])
                filedata = filedata.replace('${municipio}', person['municipio'])
                filedata = filedata.replace('${estado}', person['estado'])
                filedata = filedata.replace('${codigoPostal}', str(person['codigoPostal']))
                filedata = filedata.replace('${telefono}', str(person['telefono']))
                filedata = filedata.replace('${email}', person['email'])

                def age(birthdate):
                    today = date.today()
                    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                    return age

                filedata = filedata.replace('${edad}', str(age(date(person['yearNacimiento'], person['monthNacimiento'], person['dayNacimiento']))))

                data.close()
                return filedata

def getMultDocs(names):
    data = open('people.json')
    people = json.load(data)
    array = []
    for name in names:
        for person in people:
            with open(oficio, 'r') as file :
                if person['nombre'].lower() == name:
                    filedata = file.read()
                
                    filedata = filedata.replace('${nombre}', person['nombre'])
                    filedata = filedata.replace('${apellido1}', person['apellido1'])
                    filedata = filedata.replace('${apelldo2}', person['apelldo2'])
                    filedata = filedata.replace('${cargo}', person['cargo'])
                    filedata = filedata.replace('${empresa}', person['empresa'])
                    filedata = filedata.replace('${calle}', person['calle'])
                    filedata = filedata.replace('${numCalle}', str(person['numCalle']))
                    filedata = filedata.replace('${colonia}', person['colonia'])
                    filedata = filedata.replace('${municipio}', person['municipio'])
                    filedata = filedata.replace('${estado}', person['estado'])
                    filedata = filedata.replace('${codigoPostal}', str(person['codigoPostal']))
                    filedata = filedata.replace('${telefono}', str(person['telefono']))
                    filedata = filedata.replace('${email}', person['email'])

                    def age(birthdate):
                        today = date.today()
                        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                        return age

                    filedata = filedata.replace('${edad}', str(age(date(person['yearNacimiento'], person['monthNacimiento'], person['dayNacimiento']))))

                    array.append(filedata)
    data.close()
    return array

def deleteDoc(name):
    data = open('people.json')
    people = json.load(data)
    for idx, person in enumerate(people):
            if person['nombre'].lower() == name:
                people.pop(idx)

    with open('people.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(people, indent=2))

    data.close()
    return "item deleted"

def changeDoc(id, name, apellido1, apellido2, cargo, empresa, calle, 
numCalle, colonia, municipio, estado, codigoPostal, telefono, email, 
yearNacimiento, monthNacimiento, dayNacimiento):
    data = open('people.json')
    people = json.load(data)
    for person in people:
            if person['id'] == id:
                person['nombre'] = name
                person['apellido1'] = apellido1
                person['apelldo2'] = apellido2
                person['cargo'] = cargo
                person['empresa'] = empresa
                person['calle'] = calle
                person['numCalle'] = numCalle
                person['colonia'] = colonia
                person['municipio'] = municipio
                person['estado'] = estado
                person['codigoPostal'] = codigoPostal
                person['telefono'] = telefono
                person['email'] = email
                person['yearNacimiento'] = yearNacimiento
                person['monthNacimiento'] = monthNacimiento
                person['dayNacimiento'] = dayNacimiento
                

                with open('people.json', 'w', encoding='utf-8') as f:
                    f.write(json.dumps(people, indent=2))
    
    data.close()                
    return "item changed"

def newDoc(name, apellido1, apellido2, cargo, empresa, calle, 
numCalle, colonia, municipio, estado, codigoPostal, telefono, email, 
yearNacimiento, monthNacimiento, dayNacimiento):
    data = open('people.json')
    people = json.load(data)
    newPerson = {
        "id": len(people) + 1,
        "nombre": name,
        "apellido1": apellido1,
        "apelldo2": apellido2,
        "cargo": cargo,
        "empresa": empresa,
        "calle": calle,
        "numCalle": numCalle,
        "colonia": colonia,
        "municipio": municipio,
        "estado": estado,
        "codigoPostal": codigoPostal,
        "telefono": telefono,
        "email": email,
        "yearNacimiento": yearNacimiento,
        "monthNacimiento": monthNacimiento,
        "dayNacimiento": dayNacimiento
    }
    
    people.append(newPerson)

    with open('people.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(people, indent=2))

    data.close()                
    return "item added"

@app.get("/items")
async def root():
    return getDocs()

@app.get("/item/{name}")
async def read_item(name: str):
    return getDocByName(name)

@app.get("/item/multiple/")
async def read_items(names: List[str] = Query(default=None)):
    return getMultDocs(names) 

@app.get("/item/delete/{name}")
def read_item(name: str):
    return deleteDoc(name) 

@app.get("/item/change/{id}")
def read_item(id: int, name: Union[str, None], apellido1: Union[str, None], apellido2: Union[str, None], cargo: Union[str, None], 
empresa: Union[str, None], calle: Union[str, None], numCalle: Union[int, None], colonia: Union[str, None], 
municipio: Union[str, None], estado: Union[str, None], 
codigoPostal: Union[int, None], telefono: Union[int, None], email: Union[str, None], yearNacimiento: Union[int, None], 
monthNacimiento: Union[int, None], dayNacimiento: Union[int, None] ):
    return changeDoc(id, name, apellido1, apellido2, cargo, empresa, calle, 
    numCalle, colonia, municipio, estado, codigoPostal, telefono, email, 
    yearNacimiento, monthNacimiento, dayNacimiento)    

@app.get("/item/add/")
def read_item(name: Union[str, None], apellido1: Union[str, None], apellido2: Union[str, None], cargo: Union[str, None], 
empresa: Union[str, None], calle: Union[str, None], numCalle: Union[int, None], colonia: Union[str, None], 
municipio: Union[str, None], estado: Union[str, None], 
codigoPostal: Union[int, None], telefono: Union[int, None], email: Union[str, None], yearNacimiento: Union[int, None], 
monthNacimiento: Union[int, None], dayNacimiento: Union[int, None] ):
    return newDoc(name, apellido1, apellido2, cargo, empresa, calle, 
    numCalle, colonia, municipio, estado, codigoPostal, telefono, email, 
    yearNacimiento, monthNacimiento, dayNacimiento)  

