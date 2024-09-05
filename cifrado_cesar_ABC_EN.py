
#CONSIDERANDO EL ABECEdaro INGLÉS
import string

abecedario = string.ascii_lowercase  # ABECEDARIO COMPLETO



abed = abecedario[3:] + abecedario[:3]  # AQUI SE PUEDE DESPLAZAR A TUS NECESIDADES, POR DEFECTO ES 3

nuevoAbecedario = dict(zip(abed, abecedario))  # DICCIONARIO CESAR

print(nuevoAbecedario)
palabra = input("Ingresa palabra: ").lower()  # CONVERSION A MINUSCULAS

letras = list(palabra)  # SEPARAR POR LETRA

#print(letras)
lista = []

for i in letras:
    if i in nuevoAbecedario:
        lista.append(nuevoAbecedario[i])
    else:
        lista.append(i)  # SI EL CARACTER NO SE ENCUENTRA EN EL ABECEDARIO SE AGREGA TAL CUAL 

print("".join(lista))  # Imprimir la lista como una palabra
