 # -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:44:30 2025

@author: Administrateur
"""

"""Exercice 1"""

from tkinter import Tk, Canvas, Button, Label 

import random

couleurs = ["red", "blue", "green", "yellow", "orange", "purple", "black", "brown"]

#Exerice 1 et 2 
"""
class App:
    
    def quitter(self): self.root.destroy()
    
    def __init__(self,data):
        self.root = Tk()
        self.data = data
        self.canvas = Canvas(self.root, width=500, height=300, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)
        
        label = Label(self.root, text="Croisements: " + str(self.data.entrelacs))
        label.grid(row=1, column=1)

       
        boutton = Button(self.root, text="Quitter", command=self.quitter)
        boutton.grid(row=2, column=1)
        
        
        self.redraw()
        
    
    
        
    def run_forever(self):
        self.root.mainloop()
        
        
    def redraw(self):
        
        mots = self.data.liste_mots()
        l = self.data.l
        couleur = random.sample(couleurs,self.data.nb_fils)
        
        for fil in range(self.data.nb_fils):
            mot = mots[fil]
            x = 0
            y = l * (fil + 1)
            col = couleur[fil]
            
            for c in mot:
                if c == "D":
                    self.canvas.create_line(x,y,x+l,y+l,fill=col)
                    x+=l
                    y+=l
                elif c == "H":
                    self.canvas.create_line(x,y,x+l,y,fill=col)
                    x+=l
                elif c == "U":
                    self.canvas.create_line(x,y,x+l,y-l,fill=col)
                    x+=l
                    y-=l
                    

class Data:
    

    def __init__(self,nb_fils,entrelacs):
        self.nb_fils = nb_fils
        self.entrelacs = entrelacs
        self.l= 20
        
    def liste_mots(self):
         # État initial : [0, 1, 2, ..., nb_fils-1]
        etat = list(range(self.nb_fils))
        etats = [etat.copy()]

        # Appliquer les croisements et mémoriser chaque état
        for index in self.entrelacs:
            if 0 <= index < self.nb_fils - 1:
                etat[index], etat[index + 1] = etat[index + 1], etat[index]
                etats.append(etat.copy())
            else:
                return "Erreur : index de croisement invalide"

        # Dictionnaire pour suivre l’évolution de chaque fil
        positions = {fil: [] for fil in range(self.nb_fils)}
        
        for etat in etats:
            for pos, fil in enumerate(etat):
                positions[fil].append(pos)

        # Construire les mots pour chaque fil
        mots = []
        for fil in range(self.nb_fils):
            mot = "H"
            pos_list = positions[fil]
            for i in range(len(pos_list) - 1):
                if pos_list[i+1] > pos_list[i]:
                    mot += "HDH"
                elif pos_list[i+1] < pos_list[i]:
                    mot += "HUH"
                else:
                    mot += "HHH"
            mot += "H"
            mots.append(mot)
        return mots


nb_fils = 4
entrelacs = [2, 1, 1, 0, 2]

data= Data(nb_fils,entrelacs)

app = App(data)
app.run_forever()
"""

#Exercice 3
"""
class App:
    
    def quitter(self): self.root.destroy()
    
    def __init__(self,data):
        self.root = Tk()
        self.data = data
        self.canvas = Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)    

       
        boutton = Button(self.root, text="Quitter", command=self.quitter)
        boutton.grid(row=2, column=0)
        
        mix = Button(self.root,text="Hasard",command = self.tirage)
        mix.grid(row=2,column = 2)
        
        
        self.redraw()
        
    
    
        
    def run_forever(self):
        self.root.mainloop()
        
        
    def redraw(self):
        
        mots = self.data.liste_mots()
        l = self.data.l
        couleur = random.sample(couleurs,self.data.nb_fils)
        
        for fil in range(self.data.nb_fils):
            mot = mots[fil]
            x = 0
            y = l * (fil + 1)
            col = couleur[fil]
            
            for c in mot:
                if c == "D":
                    self.canvas.create_line(x,y,x+l,y+l,fill=col,width=3)
                    x+=l
                    y+=l
                elif c == "H":
                    self.canvas.create_line(x,y,x+l,y,fill=col,width=3)
                    x+=l
                elif c == "U":
                    self.canvas.create_line(x,y,x+l,y-l,fill=col,width=3)
                    x+=l
                    y-=l
                    
        label = Label(self.root, text="Croisements: " + str(self.data.entrelacs))
        label.grid(row=1, column=1)
                    
    def tirage(self):
        
        self.data= Data(nb_filsmax,croisements)
        self.canvas.delete("all")
        self.redraw()
        
        
                    

class Data:
    

    def __init__(self,nb_filsmax,croisements):
        
        nb_fils = random.randint(4,nb_filsmax)
        self.nb_fils = nb_fils
        self.entrelacs = random.choices(range(self.nb_fils-1),k=croisements)
        self.l= 20
        
    def liste_mots(self):
         # État initial : [0, 1, 2, ..., nb_fils-1]
        etat = list(range(self.nb_fils))
        etats = [etat.copy()]

        # Appliquer les croisements et mémoriser chaque état
        for index in self.entrelacs:
            if 0 <= index < self.nb_fils - 1:
                etat[index], etat[index + 1] = etat[index + 1], etat[index]
                etats.append(etat.copy())
            else:
                return "Erreur : index de croisement invalide"

        # Dictionnaire pour suivre l’évolution de chaque fil
        positions = {fil: [] for fil in range(self.nb_fils)}
        
        for etat in etats:
            for pos, fil in enumerate(etat):
                positions[fil].append(pos)

        # Construire les mots pour chaque fil
        mots = []
        for fil in range(self.nb_fils):
            mot = "H"
            pos_list = positions[fil]
            for i in range(len(pos_list) - 1):
                if pos_list[i+1] > pos_list[i]:
                    mot += "HDH"
                elif pos_list[i+1] < pos_list[i]:
                    mot += "HUH"
                else:
                    mot += "HHH"
            mot += "H"
            mots.append(mot)
        return mots


nb_filsmax = 8
croisements = 10 

data= Data(nb_filsmax,croisements)

app = App(data)
app.run_forever()
"""

#Exercice 4 


class App:
    
    def quitter(self): self.root.destroy()
    
    def souris(self,e): 
        
            
    def Reidemeister(self,positions):
        
        L = len(next(iter(positions.values()))) - 1  # nombre d'étapes
        nb_fils = len(positions)
        noeuds = [False] * L
    
        # Reconstituer l'ordre des fils à chaque instant t
        etats = []
        for t in range(L + 1):
            etat = [0] * nb_fils
            for fil, pos_list in positions.items():
                etat[pos_list[t]] = fil
            etats.append(etat)
    
        # Enregistrer les croisements (t, fil1, fil2)
        croisements = []
        for t in range(L):
            e1 = etats[t]
            e2 = etats[t + 1]
            for i in range(nb_fils - 1):
                if e1[i] == e2[i + 1] and e1[i + 1] == e2[i]:
                    fil1, fil2 = sorted([e1[i], e1[i + 1]])
                    croisements.append((t, fil1, fil2))
    
        # Chercher les paires (t1, t2) pour les mêmes fils
        for i in range(len(croisements)):
            t1, f1, f2 = croisements[i]
            for j in range(i + 1, len(croisements)):
                t2, f3, f4 = croisements[j]
                if f1 == f3 and f2 == f4:
                    # Vérifier qu’aucun autre croisement n’implique f1 ou f2 entre t1 et t2
                    autres = [c for c in croisements if t1 < c[0] < t2 and (f1 in c[1:] or f2 in c[1:])]
                    if not autres:
                        noeuds[t1] = True
                    break  # on ne veut que la première paire
        return noeuds

            
            
            

    
    def __init__(self,data):
        self.root = Tk()
        self.data = data
        self.canvas = Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.grid(row=0, column=0, columnspan=3)    

       
        boutton = Button(self.root, text="Quitter", command=self.quitter)
        boutton.grid(row=2, column=0)
        
        mix = Button(self.root,text="Hasard",command = self.tirage)
        mix.grid(row=2,column = 2)
        
        self.root.bind("<Button>",souris)
        
        self.redraw()
        
    
    
        
    def run_forever(self):
        self.root.mainloop()
        
        
    def redraw(self):
        
        mots = self.data.liste_mots()[0]
        l = self.data.l
        couleur = random.sample(couleurs,self.data.nb_fils)
        
        for fil in range(self.data.nb_fils):
            mot = mots[fil]
            x = 0
            y = l * (fil + 1)
            col = couleur[fil]
            
            for c in mot:
                if c == "D":
                    self.canvas.create_line(x,y,x+l,y+l,fill=col,width=3)
                    x+=l
                    y+=l
                elif c == "H":
                    self.canvas.create_line(x,y,x+l,y,fill=col,width=3)
                    x+=l
                elif c == "U":
                    self.canvas.create_line(x,y,x+l,y-l,fill=col,width=3)
                    x+=l
                    y-=l
                    
        label = Label(self.root, text="Croisements: " + str(self.data.entrelacs))
        label.grid(row=1, column=1)
                    
    def tirage(self):
        
        self.data= Data(nb_filsmax,croisements)
        self.canvas.delete("all")
        self.redraw()
        
        
                    

class Data:
    

    def __init__(self,nb_filsmax,croisements):
        
        nb_fils = random.randint(4,nb_filsmax)
        self.nb_fils = nb_fils
        self.entrelacs = random.choices(range(self.nb_fils-1),k=croisements)
        self.l= 20
        
    def liste_mots(self):
         # État initial : [0, 1, 2, ..., nb_fils-1]
        etat = list(range(self.nb_fils))
        etats = [etat.copy()]

        # Appliquer les croisements et mémoriser chaque état
        for index in self.entrelacs:
            if 0 <= index < self.nb_fils - 1:
                etat[index], etat[index + 1] = etat[index + 1], etat[index]
                etats.append(etat.copy())
            else:
                return "Erreur : index de croisement invalide"

        # Dictionnaire pour suivre l’évolution de chaque fil
        positions = {fil: [] for fil in range(self.nb_fils)}
        
        for etat in etats:
            for pos, fil in enumerate(etat):
                positions[fil].append(pos)
        print(positions)
        # Construire les mots pour chaque fil
        mots = []
        for fil in range(self.nb_fils):
            mot = "H"
            pos_list = positions[fil]
            for i in range(len(pos_list) - 1):
                if pos_list[i+1] > pos_list[i]:
                    mot += "HDH"
                elif pos_list[i+1] < pos_list[i]:
                    mot += "HUH"
                else:
                    mot += "HHH"
            mot += "H"
            mots.append(mot)
        return [mots,positions]


nb_filsmax = 8
croisements = 10 

data= Data(nb_filsmax,croisements)

app = App(data)
app.run_forever()