"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sums = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letter = cols[0]
            pairs = cols[4].split(",")
            total = sum(int(p.split(":")[1]) for p in pairs)
            sums[letter] = sums.get(letter, 0) + total
    return dict(sorted(sums.items()))