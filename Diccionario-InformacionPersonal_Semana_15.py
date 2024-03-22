# Crear un diccionario con información personal

# Diccionario
informacion_personal = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Ciudad Palanda",
    "provincia": "Zamora Chimchipe",
}
print(informacion_personal)

# Modificar cuidad
informacion_personal["ciudad"] = "Cuenca"
print(informacion_personal)

# Agregar provincia
informacion_personal["profesion"] = "Bachillerato"
print(informacion_personal)

if "telefono" in informacion_personal:
    print("Telefono existe")
else:
    print("Telefono no existe")

# Eliminar edad
informacion_personal.pop("edad")
print(informacion_personal)