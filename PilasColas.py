#Pila y cola con lista

#Cola - el primero en entrar es el primero en salir
print("Cola")
cola = [] #tipo lista

# para agregar elementos a la cola tenemos que usar el .append

cola.append("Jhon")
cola.append("Juan")
cola.append("Pedro")
print(cola) #muestra la lista
# para elimiar datos de una cola tenemos que usar el pop que elimina el elemento
# especifico de una cola y si no se especifica una posicion se elimina el ultimo de
# la lista
cola.pop() # se elimina pedro
print(cola)
cola.pop(0) # se elimina el primer elemento de la cola
print(cola)

#Pila - el primero en entrar es el ultimo en salir
print("\nPila")
pila = []

pila.append("Jhon")
pila.append("Juan")
pila.append("Pedro")

print(pila) #muestra la lista
#para ver el tope de la pila se usa pila[-1]

print(pila[-1]) #imprime pedro

print(pila.pop()) #elimina pedro y muestra

print(pila)