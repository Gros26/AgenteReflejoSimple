"""
La estructura general de los agentes es :
Sensores, Comportamiento (mapeo de percepciones a aciones), Actuadores

ambiente    -------> el agente tiene percepcion del ambiente con los sensores ----->  agente

con el mapeo de percepciones a aciones entonces:

ambiente <---------- el agente ejecuta una accion sobre el ambiente con los actuadores <--------- agente


"""

"""
Queremos solucionar el caso de un raton que quiere encontrar el queso en una 4x4 incialmente y con algunos obstaculos, ya despues se hace general,
entocnes nos dan la tabla de comportamientos , el mapeo, el ejemplo es la imagen en esta carpeta
image.png

"""

# 0 -> casilla vacia
# 1 -> obstaculo
# 2 -> ratón
# 3 -> queso

def createMatrix(): 
    matrix = [
        [0,0,0,0],
        [1,0,0,1],
        [3,0,0,0],
        [0,0,1,2]
    ]

    return matrix

print(len(createMatrix()))

matrix = createMatrix()
print(len(matrix))
print(len(matrix[0]))

def printMatrix(matrix):
    rows = len(matrix)
    string = ""
    for i in range(rows):
        string += "| "
        columns = len(matrix[i])
        for j in range(columns):
            string += str(matrix[i][j]) + " "
        string += "|\n"

    print(string)

printMatrix(matrix)




