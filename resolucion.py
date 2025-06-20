laberinto = [
    ['F',1,1,3,0,1,1,1,4],
    [3,0,0,1,0,1,0,0,1],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,3,1,1],
    [3,0,1,0,0,0,1,0,1],
    [1,1,1,1,3,1,1,1,1],
    [1,0,0,1,0,1,0,0,4],
    ['I',1,3,1,0,1,1,1,1]
]
# tomar 'F' e 'I' como camino 1 
for i in range(9):
    for j in range(9):
        if laberinto[i][j]=='I' or laberinto[i][j]=='F':
            laberinto[i][j]=1
caminoCorrecto=[]
encontrado=False

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]


for i in range(10-1):
    for j in range(10-1):
        if laberinto[i][j] == 'I' or laberinto[i][j] == 'F':
            laberinto[i][j] = 1


def buscarCamino(x, y, puntos, camino):
    if x == 0 and y == 0 and puntos >= 23:
        return camino  
   
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in direcciones:
        nx = x + dx
        ny = y + dy

       
        if 0 <= nx < 9 and 0 <= ny < 9:
            if laberinto[nx][ny] != 0:  
                valor = laberinto[nx][ny]
                laberinto[nx][ny] = 0  

                nuevos_puntos = puntos
                if valor == 3 or valor == 4:
                    nuevos_puntos += valor

                nuevoCamino = camino + [(nx, ny)]
                resultado = buscarCamino(nx, ny, nuevos_puntos, nuevoCamino)

                if resultado is not None:
                    return resultado  

                laberinto[nx][ny] = valor 

    return None  


laberinto[8][0] = 0


camino = buscarCamino(8, 0, 0, [(8, 0)])


if camino:
    print("Camino encontrado ")
    print("Pasos del camino:")
    for paso in camino:
        print(paso)
else:
    print(" No se encontró un camino ")

