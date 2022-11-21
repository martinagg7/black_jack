
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
lista_cartas = list(cartas) 
random.shuffle(lista_cartas)
print(lista_cartas)
def pedircarta():
    carta=int(input("Escoge una carta del 1 al trece:"))
    carta2=int(input("Escoge una carta del 1 al trece:"))
    while carta==carta2:
        carta2=int(input("Esa ya la pediste,escoge otra!!:"))
    carta=carta-1
    carta2=carta2-1
    return lista_cartas[carta],lista_cartas[carta2]
print(pedircarta())



