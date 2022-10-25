import json
from datetime import date

data = open('people.json')
oficio ="oficio.txt"

people = json.load(data)

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

    with open("./oficios/%s_oficio.txt" % person['nombre'], 'w') as file:
        file.write(filedata)

data.close()