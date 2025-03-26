# Créé par Administrateur, le 26/03/2025 en Python 3.7
from itertools import combinations

f = open("frenchssaccent.dic",'r')
dico = []
for ligne in f:
    dico.append(ligne[0:len(ligne)-1])
f.close()



#Exercice 1 & 2

n = 8


tirage1 = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']

mots_possibles1 = ['bis', 'bd']
solution = "bis"

tirage2 = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
mots_possibles2 = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']
solution = "sacre"



def algo1(tirage,dico):
    ensemble = set(tirage)
    L=[]
    mot_possible = []
    n = len(tirage)

    for mot in dico:
        tiragebis = tirage.copy()
        valide = True
        for lettre in mot:
            if lettre not in tiragebis:
                valide = False
                break
            tiragebis.remove(lettre)
        if valide:
            mot_possible.append(mot)

    max = len(mot_possible[0])
    maxi = mot_possible[0]
    for mot in mot_possible:
        long= len(mot)
        if long>max:
            max = long
            maxi = mot
    return maxi
#print(algo1(tirage2,dico))

#Exercice 3
Valeurs  = {"":0,"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":10,"l":1,"m":2,"n":1,"o":1,"p":3,"q":8,"r":1,"s":1,"t":1,"u":1,"v":4,"w":10,"x":10,"y":10,"z":10}

def calcul(mot):
    liste = list(mot)
    val = 0
    for lettre in mot:
        val+=Valeurs[lettre]
    return val

def algo2(tirage,dico):
    ensemble = set(tirage)
    L=[]
    mot_possible = []
    n = len(tirage)

    for mot in dico:
        tiragebis = tirage.copy()
        valide = True
        for lettre in mot:
            if lettre not in tiragebis:
                valide = False
                break
            tiragebis.remove(lettre)
        if valide:
            mot_possible.append(mot)

    max = calcul(mot_possible[0])
    maxi = mot_possible[0]
    for mot in mot_possible:
        long= calcul(mot)
        if long>max:
            max = long
            maxi = mot
    return maxi

#print(algo2(tirage2,dico))

#Exercice 4


def algo3(tirage,dico):
    ensemble = set(tirage)
    mot_possible = {}

    for mot in dico:
        tiragebis = tirage.copy()
        valide = 0
        joker  = None
        if len(mot)>len(tiragebis):continue

        for lettre in mot:
            if lettre in tiragebis:
                tiragebis.remove(lettre)
            elif "?" in tiragebis:
                if valide == 0:
                    joker = lettre
                valide +=1
                if valide >1:
                    break
            else:
                valide = 2
                break
        if valide < 2 : mot_possible[mot] = joker if joker else ""

    if not mot_possible: return ""

    def calcul2(mot):
        score = sum(Valeurs[lettre] for lettre in mot)
        if mot_possible[mot]:
            score -= Valeurs[mot_possible[mot]]
        return score

    meilleur_mot = max(mot_possible,key = calcul2,default = "")
    return meilleur_mot

#print(algo3(tirage2 + ["?"],dico))
#print(algo3(["o","o","?"],dico))
dico2 = ["bonjour", "oui", "non", "on", "oo", "ou", "ouvert"]
#print(algo3(["o","o","?"],dico2))
dico3 = ["bonjour","ooz", "oui", "non", "on", "oo", "ou", "ouvert"]
#print(algo3(["o","o","?"],dico3))
