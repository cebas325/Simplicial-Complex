# PRÁCTICA 3

from complejo_simplicial_class import SimplicialComplex
from practica2 import *



### Para visualizar los ejemplos, es necesario descomentar el ejemplo que se desee probar y descomentar el bloque de prints de las líneas 64-69
### Algunos ejemplos dependen del anterior. En esos casos, es necesario descomentar ambos y cambiar la variable 'sc' de los prints por 'sc1'
### Además, para probar el alfa complejo, hay que descomentar las 4 líneas de la práctica 2 correspondientes a la creación de cualquier 'points' y 'vor', 'tri' y 'alpha'

################################################################# Ejemplos homología simplicial #############################################################################


# 1. Tetraedro
# sc = SimplicialComplex([(0, 1, 2, 3)])

# 2. Borde del tetraedro
# sc1 = SimplicialComplex(list(sc.n_faces(2)))

# 3. Ejemplo 3
# sc = SimplicialComplex([(0,1),(1,2,3,4),(4,5),(5,6),(4,6),(6,7,8),(8,9)])

# 4. Ejemplo 4
# sc1 = SimplicialComplex(list(sc.n_faces(1)))

# 5. Ejemplo 5
# sc = SimplicialComplex([(0, 1, 2), (2, 3), (3, 4)])

# 6. Triangulación del anillo cerrado
# sc = SimplicialComplex([(1,2,4),(1,3,6),(1,4,6),(2,3,5),(2,4,5),(3,5,6)])

# 7. 1-esqueleto del anillo
# sc1 = SimplicialComplex(list(sc.n_faces(1)))

# 8. Toro
# sc = SimplicialComplex([(1,2,4), (2,4,5), (2,3,5), (3,5,6), (1,3,6), (1,4,6), (4,5,7), (5,7,8),(5,6,8),(6,8,9), (4,6,9), (4,7,9), (1,7,8), (1,2,8), (2,8,9), (2,3,9), (3,7,9), (1,3,7)])

# 9. 1-esqueleto del toro
# sc1 = SimplicialComplex(list(sc.n_faces(1)))

# 10. Plano proyectivo
# sc = SimplicialComplex([(1,2,6), (2,3,4), (1,3,4), (1,2,5), (2,3,5), (1,3,6), (2,4,6), (1,4,5), (3,5,6), (4,5,6)])

# 11. Ejemplo 10
# sc = SimplicialComplex([(0,), (1,), (2,3), (4,5), (5,6), (4,6), (6,7,8,9)])

# 12. Alfa complejo generado en la práctica 2. Para ello, es necesario descomentar las líneas de la práctica 2 que generan el aplfa complejo (points, vor, tri, alpha)
# sc = alpha

# 13. Sombrero del Asno
# sc = SimplicialComplex([(1,3,5), (1,5,6), (1,3,6), (2,3,5), (3,6,7), (2,3,7), (1,2,7), (1,7,8), (1,2,8), (2,3,8), (6,7,8), (4,6,8), (4,5,6), (2,4,5), (1,2,4), (1,3,4), (3,4,8)])

# 14. Botella de Klein
# sc = SimplicialComplex([(0,1,5), (0,3,5), (1,2,5), (2,5,6), (0,2,6), (0,4,6), (3,4,5), (4,5,7), (5,6,7), (6,7,8), (4,6,8), (3,4,8), (0,4,7), (0,1,7), (1,7,8), (1,2,8), (0,2,8), (0,3,8)])

# 15. Doble toro
# sc = SimplicialComplex([(1,2,3), (1,2,4), (2,4,5), (2,3,5), (1,3,5), (1,4,5)])

# 16. Toro 2.0
# sc = SimplicialComplex([(1,3,7), (1,2,3), (2,3,6), (3,4,6), (4,6,7), (1,6,7), (1,5,6), (2,5,6), (2,5,7), (3,5,7), (3,4,5), (1,4,5), (1,2,4), (2,4,7)])


# print("Matriz de borde dimensión 1: \n", sc.boundaryMatrix(1), "\n")
# print("Forma de Smith dimensión 1: \n", sc.smith_form(1), "\n")
# print("Matriz de borde dimensión 2: \n", sc.boundaryMatrix(2), "\n")
# print("Forma de Smith dimension 2: \n", sc.smith_form(2), "\n")
# print("Números de Betti:")
# print((sc.betti_number(0), sc.betti_number(1), sc.betti_number(2)))



################################################################ Ejemplos algoritmo incremental ###################################################################

# 1. Complejo simplicial en el plano
# sc = SimplicialComplex([[0,1,2],[0,2,3],[5,6,7],[6,7,8],[6,8,9],[0,9,6],[3,5],[3,4],[4,5]])
# print("Números de Betti con el algortimo incremental:")
# print(sc.incremental_algorithm())

# 2. Alfa complejo
# sc = alpha
# print("Números de Betti con el algortimo incremental:")
# print(sc.incremental_algorithm())