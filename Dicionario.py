# Un diccionario tiene a = {“key”:”value”} #dictionary dynamic data type

dict = {"apple": "red", "banana": "yellow", "cherry": "red"}

print(dict["apple"]) #imprime el value de la key apple

print(dict)

# Para agregar una nueva key

dict["pinneaple"] = {"orange"}

print(dict) #imprime toda la lista+


# Diccionarios con listas

equipos = {
    "futbol": ["Real Madrid", "Barcelona", "Atlético de Madrid"],
    "baloncesto": ["Real Madrid", "Barcelona", "Valencia Basket"],
    "voleibol": ["CV Teruel", "Unicaja Almería", "Ushuaïa Ibiza Vóley"],
}

print(equipos["futbol"])  # Imprime ["Real Madrid", "Barcelona", "Atlético de Madrid"]
print(equipos["baloncesto"][1])  # Imprime "Barcelona"
 # y todo quedaria listo

