import itertools as it
import numpy as np


class SimplicialComplex():
    
    
    ##### Project 1 #####

    def __init__(self, sc):
        self.sc = sc
        sc2 = list()
        self.filtorder = {}
        for s in sc: 
            sc2.append((s, 0.0))
        self.orderedList = sorted(sorted(sc2, key = lambda tupla : len(tupla[0])), key = lambda tupla : tupla[1])

    def __str__(self):
        return str(self.sc)

    def face_set(self):
        faces = set()
        for s in self.sc:
            for i in range(1, len(s) + 1):
                for c in it.combinations(s, i):
                    faces.add(c)
        return faces

    def dimension(self):
        n = 0
        for s in self.sc:
            l = len(s) - 1
            if n < l:
                n = l
        return n

    def n_faces(self, n):
        n_faces = set()
        faces = self.face_set()
        for s in faces:
            l = len(s) - 1
            if l == n:
                n_faces.add(s)
        return sorted(n_faces)

    def skeleton(self, n):
        sk = set()
        for i in range(0, n + 1):
            aux = self.n_faces(i)
            for s in aux:
                sk.add(s)
        return sk

    def st(self, s):
        star = set()
        s_set = set(s)
        faces = self.face_set()
        for face in faces:
            face_set = set(face)
            if s_set.issubset(face_set):
                star.add(face)
        return star

    def closed_st(self, s):
        star = list(self.st(s))
        c_star = self.st(s)
        sc1 = SimplicialComplex(star)
        faces = sc1.face_set()
        for face in faces:
            c_star.add(face)
        return c_star

    def lk(self, s):
        link = set()
        s_set = set(s)
        c_star = self.closed_st(s)
        for elem in c_star:
            elem_set = set(elem)
            if elem_set.isdisjoint(s_set):
                link.add(elem)
        return link

    def Euler_characteristic(self):
        d = self.dimension() 
        e = 0
        for i in range(0, d + 1):
            e = e + (-1)**(i)*len(self.n_faces(i))
        return e

    def connected_components(self):
        cc = list()
        for s in self.sc:
            disjunto = True
            for c in cc:
                if not set(s).isdisjoint(c):
                    disjunto = False
                    cc.remove(c)
                    c = c.union(set(s))
                    cc.append(c)
                    self.merge_components(cc)
                    break
            if disjunto:
                cc.append(set())
                for i in s:
                    cc[len(cc)-1].add(i)
        return len(cc)

    def merge_components(self, cc):
        done = False
        while not done:
            done = True
            for c1 in cc:
                for c2 in cc:
                    if c1 != c2 and not c1.isdisjoint(c2):
                        cc.remove(c1)
                        cc.remove(c2)
                        c1 = c1.union(c2)
                        cc.append(c1)
                        done = False
                        break
                if not done:
                    break
                
                
    ##### Project 2 #####
            
    def insert(self, simplex, f):
        self.sc += simplex
        for s in simplex:
            self.orderedList.append((s, f))
        self.orderedList = sorted(sorted(self.orderedList, key = lambda tupla : len(tupla[0])), key = lambda tupla : tupla[1])     
         
    def threshold(self, simplex):
        sSet = set(simplex)
        fl = 0.0
        for item in self.orderedList:
            itemSet = set(item[0])
            if sSet.issubset(itemSet):
                fl = item[1]
                break
        return fl
    
    def filtration(self,flotante):
        return SimplicialComplex([tupla[0] for tupla in self.orderedList if tupla[1] <= flotante])
    
    def filtrationorder(self):
        res = list()
        for t in self.orderedList:
            for s in sorted(sorted(self.filtration(t[1]).face_set()), key = lambda tupla : len(tupla)):
                if s not in res:
                    res.append(s)
        return res
    
    def threshold_values(self):
        result = list()
        for t in self.orderedList:
            if t[1] not in result:
                    result.append(t[1])
        return result
    
    def sublevel(self,r):
        return self.filtration(r)
    
    
    ##### Project 3 #####
    
    def boundaryMatrix(self, p):
        if p == 0:
            n_columns = len(self.n_faces(p))
            n_rows = 1
            BM = np.zeros((n_rows, n_columns))
        else:
            Sp = self.n_faces(p)
            Sp1 = self.n_faces(p - 1)
            n_rows = len(Sp1)
            n_columns = len(Sp)
            BM = np.zeros((n_rows, n_columns))
            for j in range(0, len(Sp)):
                for i in range(0, len(Sp1)):
                    if set(Sp1[i]).issubset(set(Sp[j])):
                        BM[i][j] = 1
        return BM
    
    def smith_form(self, p):
        BM = self.boundaryMatrix(p)
        n_rows = len(BM)
        n_columns = len(self.n_faces(p))
        n = min(n_rows, n_columns)
        for i in range(0, n):
            found = False
            if BM[i][i] == 1:
                found = True
            else:
                for i1 in range(i, n_rows):
                    for j1 in range(i, n_columns):
                        if BM[i1][j1] == 1:
                            if i1 != i:
                                self.swap_rows(BM, i, i1)
                            if j1 != i:
                                self.swap_columns(BM, i, j1)
                            found = True
                            break
                    if found: 
                        break
            if not found:
                break
            for i1 in range(i + 1, n_rows):
                if BM[i1][i] == 1:
                    self.sum_rows(BM, i, i1)
            for j1 in range(i + 1, n_columns):
                if BM[i][j1] == 1:
                    self.sum_columns(BM, i, j1)
        return BM
                
    def sum_rows(self, BM, i, iresult):
        for j in range(len(BM[i])):
            BM[iresult][j] = (BM[iresult][j] + BM[i][j]) % 2
    
    def sum_columns(self, BM, j, jresult):
        for i in range(len(BM)):
            BM[i][jresult] = (BM[i][jresult] + BM[i][j]) % 2
                            
    def swap_columns(self, BM, ja, jb):
        for row in BM:
            column_aux = row[ja]
            row[ja] = row[jb]
            row[jb] = column_aux
    
    def swap_rows(self, BM, ia, ib):
        row_aux = BM[ia]
        BM[ia] = BM[ib]
        BM[ib] = row_aux
        
    def betti_number(self, p):
        smith = self.smith_form(p)
        zp = self.obtain_z(smith)
        if p < 3:
            smith1 = self.smith_form(p + 1)
            bp = self.obtain_b(smith1)
        else:
            bp = 0
        return zp - bp
        
    def obtain_z(self, smith):
        n_columns = len(smith[0])
        return n_columns - self.range_smith(smith)
    
    def obtain_b(self, smith):
        return self.range_smith(smith)
    
    def range_smith(self, smith):
        result = 0
        n_rows = len(smith)
        n_columns = len(smith[0])
        n = min(n_rows, n_columns)
        for i in range(0, n):
            if smith[i][i] == 1:
                result += 1
            else:
                break
        return result
    
    def incremental_algorithm(self):
        vertices = self.n_faces(0)
        faces_aux = list()
        b0 = 0
        b1 = 0
        for vertex in vertices:
            faces_aux.append(vertex)
            b0 += 1
        edges = self.n_faces(1)
        for edge in edges:
            sc1 = SimplicialComplex(faces_aux)
            n1 = sc1.connected_components()
            faces_aux.append(edge)
            sc2 = SimplicialComplex(faces_aux)
            n2 = sc2.connected_components()
            if n1 != n2:
                b0 -= 1
            else:
                b1 += 1
        triangles = self.n_faces(2)
        for triangle in triangles:
            b1 -= 1
        tetrahedra = self.n_faces(3)
        for tetrahedron in tetrahedra:
            b1 += 1
        return b0, b1