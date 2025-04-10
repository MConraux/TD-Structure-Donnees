# Créé par Administrateur, le 09/04/2025 en Python 3.7
import unittest
#Exercice 1

### Un arbre de classe Tree doit pouvoir avoir des fils ou non

#Exercice 2

class Tree:

    def __init__(self,label,*children):
        self.__label = label
        self.__children = children

    def label(self):
        t = self.__label
        return str(t)

    def children(self):
        fils = tuple(self.__children)
        return fils

    def nb_children(self):
        nb_fils = len(self.children())
        return nb_fils

    def child(self,i:int):
        if 0<=i<self.nb_children():
            fils = self.children()[i]
            return fils
        return "Mais c'est foireux ça"

    def is_leaf(self):
        return self.nb_children() == 0

    def depth(self):
        if self.is_leaf():
            val = 0
            return val
        else:
            maxi = 0
            L = []
            for i in range(self.nb_children()):
                L.append(self.child(i).depth())
                maxi = max(L)
            val = maxi + 1
        return val

    def __str__(self):
        if self.is_leaf():
            return self.label()
        else:
            val = self.label()+"("
            for i in range(self.nb_children()):
                if i==self.nb_children()-1:
                    val += str(self.child(i))
                else:
                    val += str(self.child(i)) +","
        return val+")"

    def __eq__(self,B):
        for fils in self.children():
            if fils not in B.children(): return False
            else:
                val2 = []
                for filsB in B.children():
                    val2.append(filsB.__eq__(fils))
                if True not in val2: return False
        return True

a = Tree('a')
b=Tree('b')
f=Tree('f',a,b)
g = Tree('g',a)

h = Tree('h',f,g)
k = Tree('k',f,g)
l = Tree('l',g,f)
m = Tree('m',f)
n = Tree('n',g)

#print(Tree.label(a))
#print(Tree.children(f))
#print(Tree.children(a))
#print(f.is_leaf())
#print(a.is_leaf())
#print(Tree.nb_children(f))
#print(Tree.nb_children(a))
#print(Tree.child(f,1))
#print(Tree.child(f,12))
#print(f.depth())
#print(a.depth())
#print(f.__str__())
#print(a.__str__())
#print(g.__str__())
print(h.__eq__(k))
print(h.__eq__(l))
print(h.__eq__(h))
print(h.__eq__(m))
print(h.__eq__(n))
