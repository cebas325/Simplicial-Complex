# PRÁCTICA 4

from scipy.spatial import Delaunay, Voronoi,voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib as mpl
import numpy as np
from itertools import combinations
from complejo_simplicial_class import SimplicialComplex
from practica2 import *


# Función que genera la matriz de borde generalizado
def borde_generalizado(orden):
    res = np.zeros((len(orden), len(orden)), np.int8)
    for si in orden:
        for sj in [t for t in orden if len(t) == len(si) + 1]:
            if set(si).issubset(set(sj)):
                res[orden.index(si)][orden.index(sj)]=1
    return res

# Función que realiza el algoritmo matricial sobre la matriz de borde generalizado
def algoritmo_matricial(matriz):
    for j in range(len(orden)):
        columna = matriz[:, j]
        if any(columna):
            low[j] = np.max(np.where(columna == 1))
    for j in range(len(orden)):
        if low[j] != None:
            j0 = 0
            while j0 < j:
                if low[j0] == low[j]:
                    matriz[:, j] = matriz[:, j] ^ matriz[:, j0]
                    if any(matriz[:, j]):
                        low[j] = np.max(np.where(matriz[:, j] == 1))
                    else:
                        low[j] = None
                        break
                    j0 = 0 
                else:
                    j0 += 1
    return matriz 

# Función que genera los puntos del diagrama de persistencia dada la matriz resultante de aplicar el algoritmo matricial
def puntos_diag_persistencia(matrizR):
    res = []
    for j in range(len(orden)):
        if low[j] != None:
            res.append((len(orden[low[j]]) - 1, filtrationValue(orden[low[j]]), filtrationValue(orden[j]))) 
        elif (low[j] == None):
            act = True
            for ind in np.where(matrizR[j, :] == 1)[0].tolist():
                if low[ind] == j: act = False
            if act : res.append((len(orden[j]) - 1, filtrationValue(orden[j]), 2.0))
    return res

# Función que pinta el diagrama de persistencia
def plot_diag_persistencia(points):
    for t in points:
        p = t[0]
        tx = t[1]
        ty = t[2]
        if p == 0:
            plt.plot(tx, ty, 'bo')
        elif p == 1:
            plt.plot(tx, ty, 'ro')
    plt.plot(range(3), 'k--')
    plt.plot([2, 2, 2], 'k--')
    plt.show()
    return 0

# Función que pinta el diagrama de barras
def plot_diag_barras(points):
    ptsordenado = sorted(sorted(points, key = lambda tupla : tupla[2] - tupla[1]), key = lambda tupla : tupla[0])
    for t in ptsordenado:
        p = t[0]
        inicio = t[1]
        final = t[2]
        if p == 0:
            plt.plot([inicio, final], [ptsordenado.index(t) + 1,ptsordenado.index(t) + 1], 'b-')
        elif p==1:
            plt.plot([inicio, final], [ptsordenado.index(t) + 1,ptsordenado.index(t) + 1], 'r-')
    plt.show()
    return 0



### Para visualizarlos, es necesario descomentar una de las variables 'orden', en la que hay un complejo simplicial ordenado
### Hay dos opciones, usar de ejemplos el complejo de las diapositivas del tema 3 (línea 96)
### O utilizar un alfa complejo de la práctica 2, al que se le aplica el método 'filtrationorder' para ordenarlo (línea 100)
### En cualquier caso, una vez se esté usando uno de los dos, se descomenta el bloque de líneas 103-105, donde se pintan los diagramas

################################################################ Ejemplos homología persistente ###################################################################

## 1. Ejemplo de la teoría
# orden = [(0,), (1,), (2,), (3,), (4,), (5,), (0,3), (2,4), (3,5), (4,5), (1,2), (0,1), (1,3), (1,4), (3,4), (0,1,3), (1,2,4), (3,4,5), (1,3,4)]

## 2. Ejemplo con alfa complejos: para este caso es preferible utilizar un conjunto de puntos que aproxime a una curva
## Para ello, descomentar la variable 'points' en práctica 2 de la línea 98
# orden = AlphaComplex(points).filtrationorder()
low = [None]*len(orden)

# pts = puntos_diag_persistencia(algoritmo_matricial(borde_generalizado(orden)))
# plot_diag_persistencia(pts)
# plot_diag_barras(pts)