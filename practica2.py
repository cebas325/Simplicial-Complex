# PRÁCTICA 2

from scipy.spatial import Delaunay, Voronoi,voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib as mpl
import numpy as np
from itertools import combinations
from complejo_simplicial_class import SimplicialComplex


# Función que calcula el valor de filtración de un símplice
def filtrationValue(simplex):
    if len(simplex) == 1:
        return 0.0
    elif len(simplex) == 3:
        p0 = points[simplex[0]]
        p1 = points[simplex[1]]
        p2 = points[simplex[2]]  
        d = 2 * (p0[0] * (p1[1] - p2[1]) + p1[0] * (p2[1] - p0[1]) + p2[0] * (p0[1] - p1[1]))
        if d == 0:
            return np.inf
        else:
            xc = ((p0[1]**2 + p0[0]**2) * (p1[1] - p2[1]) + (p1[1]**2 + p1[0]**2) * (p2[1] - p0[1]) + (p2[1]**2 + p2[0]**2) * (p0[1] - p1[1])) / d
            yc = -((p0[1]**2 + p0[0]**2) * (p1[0] - p2[0]) + (p1[1]**2 + p1[0]**2) * (p2[0] - p0[0]) + (p2[1]**2 + p2[0]**2) * (p0[0] - p1[0])) / d
            r2 = (p0[0] - xc)**2 + (p0[1] - yc)**2
            return np.sqrt(r2)
    elif len(simplex) == 2:
        diam = np.sqrt((points[simplex[0]][0] - points[simplex[1]][0])**2 + (points[simplex[0]][1] - points[simplex[1]][1])**2)
        centro = ((points[simplex[0]][0] + points[simplex[1]][0]) / 2, (points[simplex[0]][1] + points[simplex[1]][1]) / 2)
        for p in np.delete(points, [simplex[0], simplex[1]], 0):
            if np.sqrt((centro[0] - p[0])**2 + (centro[1] - p[1])**2) < diam / 2:
                return filtrationValue(tuple((simplex[0], simplex[1], np.where(points == p))))
        return diam/2
    return None

# Función que calcula el alfa complejo de un conjunto de puntos
def AlphaComplex(points):
    res = SimplicialComplex([])
    tri = SimplicialComplex(Delaunay(points).simplices)
    for s in tri.face_set():
        res.insert([s], filtrationValue(s))
    return res

# Función que pinta el alfa complejo
def plotalpha(points, K):
    lineas = [t for t in K.sc if len(t)==2]
    triangulos = [t for t in K.sc if len(t)==3]
    fig = voronoi_plot_2d(vor, show_vertices=False, line_width=2, line_colors='blue')
    plt.plot(points[:,0], points[:,1], 'ko')
    for l in lineas:
        plt.plot([points[l[0]][0], points[l[1]][0]], [points[l[0]][1], points[l[1]][1]],'k-', linewidth=2)
    if len(triangulos) > 0:
        c=np.ones(len(triangulos))
        cmap = matplotlib.colors.ListedColormap("limegreen")
        plt.tripcolor(points[:, 0], points[:, 1], triangulos, facecolors=c, edgecolor="k", lw=2, cmap=cmap)
    plt.show()
    return 0

# Función que calcula el valor de filtración de un símplice para un complejo de Vietoris-Rips
def filtrationValueVR (simplex):
    l = len(simplex)
    if l == 1:
        return 0.0
    elif l == 2:
        return np.sqrt((points[simplex[0]][0] - points[simplex[1]][0])**2 + (points[simplex[0]][1] - points[simplex[1]][1])**2) / 2
    else:
        return max([filtrationValueVR(arista) for arista in combinations(simplex, 2)])
    return None

# Función que pinta el complejo de Vietoris-Rips
def Vietoris_RipsComplex(points):
    res = SimplicialComplex([])
    indexes = [range(len(points))]
    complejo = SimplicialComplex(indexes)
    for s in complejo.face_set():
        res.insert([s], filtrationValueVR(s))
    return res



### Para visualizar los ejemplos, es necesario descomentar, para cada ejemplo, uno de los conjuntos de puntos (líneas 89, 92, 95, 98)
### Posteriormente, se descomenta el bloque de líneas 100-102, en las que se crea el alfa complejo
### Finalemnte, se descomenta el bloque de líneas 104-107, con las que se pinta el complejo

################################################################# Ejemplos alfa complejos #############################################################################

## 1. Ejemplo 1
# points = np.array([(0.38021546727456423, 0.46419202339598786), (0.7951628297672293, 0.49263630135869474), (0.566623772375203, 0.038325621649018426), (0.3369306814864865, 0.7103735061134965), (0.08272837815822842, 0.2263273314352896), (0.5180166301873989, 0.6271769943824689), (0.33691411899985035, 0.8402045183219995), (0.33244488399729255, 0.4524636520475205), (0.11778991601260325, 0.6657734204021165), (0.9384303415747769, 0.2313873874340855)])

## 2. Ejemplo 2
# points = np.array([[0.8957641450573793, 0.2950833519989374], [0.028621391963087994, 0.9440875759025237], [0.517621505875702, 0.1236620161847416], [0.7871047164191424, 0.7777474116014623], [0.21869796914805273, 0.7233589914276723], [0.9891035292480995, 0.6032186214942837], [0.30113764052453484, 0.613321425324272], [0.18407448222466916, 0.7868606964403773], [0.4496777667376678, 0.874366215574117], [0.08225571534539433, 0.616710205071694]])

## 3. Ejemplo 3
# points = np.array([(0.8753299639906736, 0.5452963206013219), (0.915335120559448, 0.8622822047328554), (0.9411759819184322, 0.2748278885761678), (0.7052034033196758, 0.8122389578499669), (0.9734431558329487, 0.5500672178217452), (0.101349658961157, 0.6072126518098413), (0.6099428935549683, 0.5095146187792166), (0.6810379648990679, 0.6343196355745316), (0.763747595111296, 0.6389758508715849), (0.6521290891236327, 0.28340359060768416), (0.4569706839687516, 0.5970966728571825), (0.3339042514617916, 0.7888181435443109), (0.24447615661103717, 0.18247811626397858), (0.6961254832425103, 0.9974914431850389), (0.2452860638322797, 0.2974794924024807), (0.09631846692736679, 0.2887656085651358), (0.638575556222527, 0.26034722595932536), (0.803241921795395, 0.24803894619975986), (0.8809182300057703, 0.3389661339754195), (0.3565859265456749, 0.25327819736066515)])

## Ejemplo 4, aproximación de circunferencia
points = np.array([[ 0.7649936 , -6.49105706], [-0.26047978,  3.17414802], [ 5.16486466, -2.77709227], [ 6.3630621 ,  2.08442442], [ 1.63681198,  4.95671697], [-4.47103343, -0.4944843 ], [-2.12035066,  4.80887876], [-3.44986384, -3.25828704], [-3.55428879,  3.18415674], [-0.27202076,  3.89295058], [-2.9512385 ,  5.76602403], [ 6.36747098, -1.44195299], [ 3.36400365,  4.33230353], [ 3.23972602, -3.44494391], [-3.29551494,  0.50827386], [-1.55188576,  3.42645393], [-3.62672644, -3.14264111], [ 3.54177077, -4.42486894], [-6.39734363,  1.37489294], [ 4.46578318, -0.76225718]])

# vor = Voronoi(points)
# tri = Delaunay(points)
# alpha = AlphaComplex(points)
# 
# for value in alpha.threshold_values():
    # K=alpha.sublevel(value)
    # plotalpha(points, K)
    # plt.show()
    
    
    
### Para visualizar el ejemplo, únicamente es necesario descomentar las líneas 116-117 y uno de los conjuntos de puntos (líneas 89, 92, 95, 98)
    
################################################################# Ejemplos Vietoris-Rips #############################################################################    
    
    
# VR = Vietoris_RipsComplex(points)
# print(VR.threshold_values())