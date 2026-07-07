"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            cols = line.strip().split("\t")
            letter = cols[0]
            val = int(cols[1])
            if letter not in data:
                data[letter] = [val, val]
            else:
                data[letter][0] = max(data[letter][0], val)
                data[letter][1] = min(data[letter][1], val)
    return [(k, v[0], v[1]) for k, v in sorted(data.items())]