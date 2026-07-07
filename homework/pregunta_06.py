"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    data = {}
    with open("files/input/data.csv", "r") as f:
        for line in f:
            pairs = line.strip().split("\t")[4].split(",")
            for pair in pairs:
                k, v = pair.split(":")
                val = int(v)
                if k not in data:
                    data[k] = [val, val]
                else:
                    data[k][0] = min(data[k][0], val)
                    data[k][1] = max(data[k][1], val)
    return [(k, v[0], v[1]) for k, v in sorted(data.items())]