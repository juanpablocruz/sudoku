from numpy import *
def read(direc):
    sudoku = open(direc)

    matrx=[]
    for i in range(9):
        row=[]
        for j in range(9):
            row.append(0)
        matrx.append(row)
    
    a = 0
    while a == 0:
        fichero = sudoku.readline()
    
        if not fichero:
            a = 1    
        else:
            i = int(fichero[0])
            j = int(fichero[2])
            val = int(fichero[4])
        
            matrx[i-1][j-1] = val  
    return matrx    
    sudoku.close()
def readresult(sol):
    respuesta = fromfile(sol, sep=' ', dtype=int)
    solucion = respuesta.reshape(9,9)
    return solucion
    respuesta.close()
