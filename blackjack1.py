

import random
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
}

lista_cartas = list(cartas) #creo una nueva lista con unicamente los valores de las cartas del diccionario
random.shuffle(lista_cartas)#mezclo las cartas
print(lista_cartas)


#PARTE DEL JUGADOR
carta1=random.choice(lista_cartas)  #Carta1 aleatoria de la lista
carta2=random.choice(lista_cartas)  #Carta2 aletoria de la lista
valorcarta1=cartas[carta1]
valorcarta2=cartas[carta2]
sumacartasjugador=valorcarta1+valorcarta2


print(f"Tus primera carta es {carta1} --> su puntuacion es {valorcarta1}\n tu segunga carta es {carta2} -->su puntuacion es {valorcarta2}")
print(f">>>La suma de sus puntaciones es {sumacartasjugador}<<<")

#Elimino las dos cartas que  la banca le ha dado al jugador  de mi lista
lista_cartas.remove(carta1)
lista_cartas.remove(carta2)
print("Las cartas de la banca son ahora ➤ :",lista_cartas)



#PARTE DE LA BANCA
cartabanca1=random.choice(lista_cartas)
cartabanca2=random.choice(lista_cartas)
valor_cartabanca1=cartas[cartabanca1]
valor_cartabanca2=cartas[cartabanca2]
sumacartasbanca=valor_cartabanca1+valor_cartabanca2
print(f"La primera carta de la banca es {cartabanca1} --> su puntuacion es {valor_cartabanca1} \n la segunda carta de la banca carta es {cartabanca2} -->su puntuacion es {valor_cartabanca2}")
print(f">>>La suma de sus puntaciones es {sumacartasbanca}<<<")
#¿Quién gana la partida?
if sumacartasbanca>sumacartasjugador:
    print("🅾 🅷 🆅 🅰 🆈 🅰, 🅻 🅰   🅱 🅰 🅽 🅲 🅰   🅷 🅰   🅶 🅰 🅽 🅰 🅳 🅾")
elif sumacartasbanca<sumacartasjugador:
    print("🅴 🅻   🅹 🆄 🅶 🅰 🅳 🅾 🆁     🅷 🅰    🅶 🅰 🅽 🅰 🅳 🅾")
else:
    print("🅴 🅼 🅿 🅰 🆃 🅴")













