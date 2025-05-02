# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import matplotlib.pyplot as plt

#Exercice 2
Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z"]
 
#J'ai créé alpha au cas où j'en avais besoin pour faire mes tests mais je n'en ai finalement pas eu besoin 
f = open("frenchssaccent.dic",'r')
dico = []
for ligne in f:
    dico.append(ligne[0:len(ligne)-1])
f.close()

def naive(key):
    "Fonction faisant la somme des valeurs ODC pour chaque lettre du mot"
    return sum(ord(c) for c in key)


class Hashtable:
    "But: recréer une table de hachage (sorte de dictionnaire)"
    def __init__(self, hash_function=None, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_function = hash_function

    def taille(self):
        return self.size

    def put(self, key, value):
        "Permet d'ajouter une clé et une valeur dans notre table de hachage celle-ci change automatiquement sa taille à partir d'un certain nombre de valeur codée au même index"
        index = self.hash_function(key) % self.size
        
        if len(self.table[index])+1>1.2 * self.size:
            self.resize()
            
        index = self.hash_function(key) % self.size  
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        "Renvoie la valeur associée à une clé"
        index = self.hash_function(key) % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def repartition(self):
        "Permets de créer un graphique permettant de montrer le nombre de clé associée à un index précis"
        y = [len(self.table[i]) for i in range(self.size)]
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
    
    def resize (self):        
        "Double la taille du tableau puis réindexe tous ses éléments"
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        for couple in old_table:
            for key, value in couple:
                self.put(key, value)
        
            
        
        
        
           
    

"""      
h = Hashtable(naive,10)

h.put('abc', 3)
print(h.get( 'aaa'))
print(h.get( 'abc'))

h.put('cba', 5)
h.put('abc', 7)
print(h.get( 'abc'))
print(h.get( 'cba'))
"""

h2 = Hashtable(naive,100)

for i in range(len(dico)-1):
    val = dico[i]
    h2.put(val,len(val))

h2.repartition()

"""
h3 = Hashtable(naive,10000)

for i in range(len(dico)-1):
    val = dico[i]
    h3.put(val,len(val))

h3.repartition()
"""
