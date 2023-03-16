# PRÁCTICA 1

from complejo_simplicial_class import SimplicialComplex



### Para visualizar los ejemplos, es necesario descomentar el ejemplo que se desee probar y descomentar el bloque de prints de las líneas 61-70.
### Algunos ejemplos dependen del anterior. En esos casos, es necesario descomentar ambos y cambiar la variable 'sc' de los prints por 'sc1'

############################################################### Ejemplos complejos simpliciales ###########################################################################


# 1. Tetraedro 
# sc = SimplicialComplex([(0, 1, 2, 3)])
# print("\nTetraedro: ", sc, "\n")

# 2. Borde del tetraedro
# sc1 = SimplicialComplex(list(sc.skeleton(2)))
# (print("\nBorde del tetraedro: ", sc1, "\n"))

# 3. Ejemplo 3
# sc = SimplicialComplex([(0, 1), (1, 2, 3, 4), (4, 5), (5, 6), (4, 6), (6, 7, 8), (8, 9)])
# print("\nEjemplo 3: ", sc, "\n")

# 4. 1-esqueleto del ejemplo 3
# sc1 = SimplicialComplex(list(sc.skeleton(1)))
# print("\n1-esqueleto del ejemplo 3: ", sc1, "\n")

# 5. Ejemplo 5
# sc = SimplicialComplex([(0, 1, 2), (2, 3), (3, 4)])
# print("\nEjemplo 5: ", sc, "\n")

# 6. Triangulación del anillo cerrado
# sc = SimplicialComplex([(1, 2, 4), (1, 3, 6), (1, 4, 6), (2, 3, 5), (2, 4, 5), (3, 5, 6)])
# print("\nTriangulación del anillo cerrado: ", sc, "\n")

# 7. 1-esqueleto del anillo
# sc1 = SimplicialComplex(list(sc.skeleton(1)))
# print("\n1-esqueleto del anillo: ", sc1, "\n")

# 8. Toro
sc = SimplicialComplex([(1, 2, 4), (2, 4, 5), (2, 3, 5), (3, 5, 6), (1, 3, 6), (1, 4, 6), (4, 5, 7), (5, 7, 8), (5, 6, 8), (6, 8, 9), (4, 6, 9), (4, 7, 9), (1, 7, 8), (1, 2, 8), (2, 8, 9), (2, 3, 9), (3, 7, 9), (1, 3, 7)])
print("\nToro: ", sc, "\n")

# 9. 1-esqueleto del toro
# sc1 = SimplicialComplex(list(sc.skeleton(1)))
# print("\n1-esqueleto del toro: ", sc1, "\n")

# 10. Triangulación del plano proyectivo
# sc = SimplicialComplex([(1, 2, 6), (2, 3, 4), (1, 3, 4), (1, 2, 5), (2, 3, 5), (1, 3, 6), (2, 4, 6), (1, 4, 5), (3, 5, 6), (4, 5, 6)])
# print("\nTriangulación del plano proyectivo: ", sc, "\n")

# 11. 1-esqueleto del plano proyectivo 
# sc1 = SimplicialComplex(list(sc.skeleton(1)))
# print("\n1-esqueleto del plano proyectivo :", sc1, "\n")

# 12. Ejemplo 10
# sc = SimplicialComplex([(0,), (1,), (2, 3), (4, 5), (4, 6), (6, 7, 8, 9)])
# print("\nEjemplo 12: ", sc, "\n")

print("Conjunto de todas sus caras: ", sc.face_set())
print("Dimensión: ", sc.dimension())
print("Conjunto de vértices: ", sc.n_faces(0))
print("Conjunto de aristas: ", sc.n_faces(1))
print("Conjunto de 2-símplices: ", sc.n_faces(2))
print("Conjunto de 3-símplices: ", sc.n_faces(3))
print("Característica de Euler: ", sc.Euler_characteristic())
print("Estrella de la arista (0, 1): ", sc.st((6,)))
print("Link de la arista (0, 1): ", sc.lk((6,)))
print("Número de componentes conexas: ", sc.connected_components())



### Únicamente hay un ejemplo. Para visualizarlo, hay que descomentar el bloque de líneas 76-92

############################################################### Ejemplos filtración ###########################################################################


# sc = SimplicialComplex([])
# sc.insert([(0, 1)], 1.0)
# sc.insert([(1, 2), (2, 3), (2, 4)], 2.0)
# sc.insert([(3, 4)], 3.0)
# sc.insert([(2, 3, 4)], 4.0)
# 
# print("\nConjunto de caras: ", sc.face_set())
# print("Umbral del vértice (3,): ", sc.threshold((3,)))
# K1 = sc.filtration(1.0)
# K2 = sc.filtration(2.0)
# K3 = sc.filtration(3.0)
# K4 = sc.filtration(4.0) 
# print(K1.face_set())
# print(K2.face_set())
# print(K3.face_set())
# print(K4.face_set())
# print("Complejo ordenado según la filtración: ", sc.filtrationorder())
         
