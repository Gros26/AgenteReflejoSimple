"""
La estructura general de los agentes es :
Sensores, Comportamiento (mapeo de percepciones a aciones), Actuadores

ambiente    -------> el agente tiene percepcion del ambiente con los sensores ----->  agente

con el mapeo de percepciones a acciones entonces:

ambiente <---------- el agente ejecuta una accion sobre el ambiente con los actuadores <--------- agente


"""

"""
Queremos solucionar el caso de un raton que quiere encontrar el queso en una 4x4 incialmente y con algunos obstaculos, ya despues se hace general,
entocnes nos dan la tabla de comportamientos , el mapeo, el ejemplo es la imagen en esta carpeta
image.png

"""

# 0 -> empty cell
# 1 -> obstacle
# 2 -> mouse
# 3 -> cheese

def create_matrix():
    #esto seria bueno que fuera aleatorio, que se le pasen medidas y ponga las cosas aleatoriamente 
    matrix = [
        [0,0,0,0],
        [1,0,0,1],
        [3,0,0,0],
        [0,0,1,2]
    ]

    return matrix

print(len(create_matrix()))

matrix = create_matrix()
print(len(matrix))
print(len(matrix[0]))

def print_matrix(matrix):
    rows = len(matrix)
    string = ""
    for i in range(rows):
        string += "| "
        columns = len(matrix[i])
        for j in range(columns):
            string += str(matrix[i][j]) + " "
        string += "|\n"

    print(string)

print_matrix(matrix)


""" 
Como se que el raton tiene una posicion y va a tener 5 sensores, que serian:
Sensor izquierdo, arriba, derecho, abajo y sensor si huele a queso
"""

class Mouse:
    def __init__(self, x, y, matrix):
        self.row = x
        self.column = y
        self.matrix = matrix
        self.update_sensors()

    def position(self):
        return (self.row, self.column) 
    
    def update_sensors(self):
        self.left = self.column - 1 >= 0 and self.matrix[self.row][self.column - 1] != 1
        self.up = self.row - 1 >= 0 and self.matrix[self.row - 1][self.column] != 1
        self.right = self.column + 1 <= (len(self.matrix[self.row]) - 1) and self.matrix[self.row][self.column + 1] != 1
        self.down = self.row + 1 <= (len(self.matrix) - 1) and self.matrix[self.row + 1][self.column] != 1
        self.smells_cheese = self._is_cheese_adjacent()

    #funcion auxiliar privada
    def _is_cheese_adjacent(self):
        if(self.column - 1 >= 0 and self.matrix[self.row][self.column - 1] == 3):
            return True
        elif(self.row - 1 >= 0 and self.matrix[self.row - 1][self.column] == 3):
            return True
        elif(self.column + 1 <= (len(self.matrix[self.row]) - 1) and self.matrix[self.row][self.column + 1] == 3):
            return True
        elif(self.row + 1 <= (len(self.matrix) - 1) and self.matrix[self.row + 1][self.column] == 3):
            return True
        else:
            return False
        
    def move(self, x, y):
        self.matrix[self.row][self.column] = 0
        self.matrix[x][y] = 2
        self.row = x
        self.column = y
        self.update_sensors()
        
        
    def decide_action(self):
        if self.smells_cheese:
            self.eat_cheese()
        # libre, libre, libre, libre -> ir arriba
        elif self.left and self.up and self.right and self.down:
            self.move(*(self._go_up())) #* signo de desempaquetado para la tupla
        # libre, libre, libre, no libre -> ir arriba
        elif self.left and self.up and self.right and not self.down:
            self.move(*(self._go_up()))
        # libre, libre, no libre, libre -> ir arriba
        elif self.left and self.up and not self.right and self.down:
            self.move(*(self._go_up()))
        # libre, libre, no libre, no libre -> ir izquierda
        elif self.left and self.up and not self.right and not self.down:
            self.move(*(self._go_left()))
        # libre, no libre, libre, libre -> ir izquierda
        elif self.left and not self.up and self.right and self.down:
            self.move(*(self._go_left()))
        # libre, no libre, libre, no libre -> ir derecha
        elif self.left and not self.up and self.right and not self.down:
            self.move(*(self._go_right()))
        # libre, no libre, no libre, libre -> ir izquierda
        elif self.left and not self.up and not self.right and self.down:
            self.move(*(self._go_left()))
        # libre, no libre, no libre, no libre -> ir izquierda
        elif self.left and not self.up and not self.right and not self.down:
            self.move(*(self._go_left()))
        # no libre, libre, libre, libre -> ir arriba
        elif not self.left and self.up and self.right and self.down:
            self.move(*(self._go_up()))
        # no libre, libre, libre, no libre -> ir derecha
        elif not self.left and self.up and self.right and not self.down:
            self.move(*(self._go_right()))
        # no libre, libre, no libre, libre -> ir abajo
        elif not self.left and self.up and not self.right and self.down:
            self.move(*(self._go_down()))
        # no libre, libre, no libre, no libre -> ir arriba
        elif not self.left and self.up and not self.right and not self.down:
            self.move(*(self._go_up()))
        # no libre, no libre, libre, libre -> ir derecha
        elif not self.left and not self.up and self.right and self.down:
            self.move(*(self._go_right()))
        # no libre, no libre, libre, no libre -> ir derecha
        elif not self.left and not self.up and self.right and not self.down:
            self.move(*(self._go_right()))
        # no libre, no libre, no libre, libre -> ir abajo
        elif not self.left and not self.up and not self.right and self.down:
            self.move(*(self._go_down()))

    def eat_cheese(self):
        return "delicious"

    # def __str__(self):
    #     return "2"
    
    def _go_left(self):
        return (self.row, self.column - 1)

    def _go_up(self):
        return (self.row - 1, self.column)
    
    def _go_right(self):
        return (self.row, self.column + 1)
    
    def _go_down(self):
        return (self.row + 1, self.column)



#este seria el caso donde no termina, porque sus acciones lo dejan en bucle
# mouse = Mouse(3, 3, matrix)
# while(mouse.smells_cheese != True):
#     mouse.decide_action()
#     print_matrix(matrix)
    
#aqui siguiendo la image2.png

matrix2 = [
    [3,0,0,0],
    [0,1,2,0],
    [0,1,0,0],
    [0,0,0,1]
]
print("--------------------")
print_matrix(matrix)

mouse = Mouse(1, 2, matrix2)
while(mouse.smells_cheese != True):
    mouse.decide_action()
    print_matrix(matrix2)
    


