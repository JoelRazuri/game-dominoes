"""
     Dominó:
        a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
        recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
        b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
        recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
        cadenas.
"""

# Aclaración: se usa ciclo while en las dos funciones para no hacer iteraciones de mas. Con ciclo for se recorreria hasta el final aunque ya se sepa si coinciden las fichas.

def encajan_domino_tuplas(tupla1, tupla2):
    # Recibe dos fichas de domino e indica si encajan o no.

    condicion = False
    i = 0

    while not condicion and i<2:
        j = 0

        while not condicion and j<2:
            if tupla1[i]==tupla2[j]:
                condicion = True
            j+=1
        
        i+=1

    if condicion:
        print(f"Las piezas {tupla1} {tupla2} coinciden")
    else:
        print(f"Las piezas {tupla1} {tupla2} no coinciden")

print("EJERCICIO CON TUPLAS:")
encajan_domino_tuplas((3,4),(5,4))
encajan_domino_tuplas((3,2),(5,4))
encajan_domino_tuplas((3,3),(3,5))


print("-------------------------------------------------------------------------")

def encajan_domino_cadena(cadena):
    # Recibe una cadena de caracteres con dos fichas de domino e indica si encajan o no.

    fichas = cadena.split(" ")

    condicion = False
    ficha_1 = 0
    ficha_2 = 1
    i = 0
    
    while not condicion and i<3:
        
        j = 0
        while not condicion and j<3:
            if fichas[ficha_1][i]==fichas[ficha_2][j]:
                condicion = True
            j+=2
        
        i+=2

    if condicion:
        print(f"Las piezas {fichas[ficha_1]} {fichas[ficha_2]} coinciden")
    else:
        print(f"Las piezas {fichas[ficha_1]} {fichas[ficha_2]} no coinciden")

print("EJERCICIO CON CADENA DE CARACTERES:")
encajan_domino_cadena("3-4 2-5")
encajan_domino_cadena("3-4 1-4")
