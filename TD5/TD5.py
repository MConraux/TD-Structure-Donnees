# -*- coding: utf-8 -*-
"""
Editeur de Spyder

Ceci est un script temporaire.
""" 
from tkinter import Tk, Canvas, Button, Label
"""
root = Tk("Hello")

canvas = Canvas(root)
canvas.grid(column = 1, row = 1)

root.mainloop()
"""
#Exercice 1 

mot = "HUHHDUH"

canvas = Canvas()
def read_word(canvas, mot, h, w,x,y,col):
    

    
    for c in mot:
        if c == "D":
            canvas.create_line(x,y,x+w,y+h,fill=col)
            x+=w
            y+=h
        elif c == "H":
            canvas.create_line(x,y,x+h,y,fill=col)
            x+=h
        elif c == "U":
            canvas.create_line(x,y,x+w,y-h,fill=col)
            x+=w
            y-=h
        else:
            return"Une erreur s'est glissee dans le mot"
    
    return "Dessin avec succs! "
"""""
 # Cration de la fentre
 
fenetre = Tk()
canvas = Canvas(fenetre, width=300, height=300, bg="white")
canvas.pack()

# Dessiner le mot
resultat = read_word(canvas, mot, 20, 20,0,30)
print(resultat)

fenetre.mainloop()
"""

def entrelacs(nb_fils, croisements):
     # État initial : [0, 1, 2, ..., nb_fils-1]
    etat = list(range(nb_fils))
    etats = [etat.copy()]

    # Appliquer les croisements et mémoriser chaque état
    for index in croisements:
        if 0 <= index < nb_fils - 1:
            etat[index], etat[index + 1] = etat[index + 1], etat[index]
            etats.append(etat.copy())
        else:
            return "Erreur : index de croisement invalide"

    # Dictionnaire pour suivre l’évolution de chaque fil
    positions = {fil: [] for fil in range(nb_fils)}
    
    for etat in etats:
        for pos, fil in enumerate(etat):
            positions[fil].append(pos)

    # Construire les mots pour chaque fil
    motsbis = []
    for fil in range(nb_fils):
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
        motsbis.append(mot)
    return motsbis

# Paramètres
tableau = [2, 1, 1, 0, 2]
cs = ["black","red","blue","green"]
fils = 4
l = 20

fenetre = Tk()
fenetre.title("Entrelacs")

canvas = Canvas(fenetre, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=3)

# Génération des mots et dessin
mots = entrelacs(fils, tableau)
for fil in range(fils):
    read_word(canvas, mots[fil], l, l, 0, l * (fil + 1), cs[fil])

# Label avec les croisements
label = Label(fenetre, text="Croisements: " + str(tableau))
label.grid(row=1, column=1)

# Bouton
but = Button(fenetre, text="Quitter", command=quit)
but.grid(row=2, column=1)


fenetre.mainloop()
