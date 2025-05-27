# -*- coding: utf-8 -*-
"""
Created on Wed May 21 15:14:30 2025

@author: Administrateur
"""
import struct 

wall = open("the_wall.wav","rb")

data = wall.read()
f = 44100

#Exercice 1 

def extraire(doc):
    
    taille = struct.unpack_from("I", doc,40)
    echantillon = taille[0]//4

    L = []
    
    for i in range(echantillon):
        t = struct.unpack_from("hh",doc,i*4+44)
        L.append(t)
        
    return L 
    
the_wall = extraire(data)

#Exercice 2 

def towav(L):
    data_taille = len(L)*4
    fichier_taille = data_taille + 36
    
    new = open("the_wallbis.wav","wb")
    
    new.write(data[0:4])
    new.write(struct.pack("I",fichier_taille))
    new.write(data[8:40])
    new.write(struct.pack("I",data_taille))
    
    for elem in L:
        new.write(struct.pack("h",elem[0]))
        new.write(struct.pack("h",elem[1]))
        
    new.close()         
    
the_wallbis = towav(the_wall)

#Exerice 3 

def towavcut(L):
    data_taille = len(L)*4//2
    fichier_taille = data_taille + 36
    
    new = open("the_wallcut.wav","wb")
    
    new.write(data[0:4])
    new.write(struct.pack("I",fichier_taille))
    new.write(data[8:40])
    new.write(struct.pack("I",data_taille))
    
    for elem in L:
        new.write(struct.pack("h",elem[0]))
        #new.write(struct.pack("h",elem[1]))
        
    new.close()

the_wallcut = towavcut(the_wall)

#Exercice 4 

def towavdoubl(L):
    taille = len(L)
    data_taille = taille*4*2
    fichier_taille = data_taille + 36
    
    new = open("the_walldoubl.wav","wb")
    
    new.write(data[0:4])
    new.write(struct.pack("I",fichier_taille))
    new.write(data[8:40])
    new.write(struct.pack("I",data_taille))
    
    for i in range(1,taille):
        val_gauche = L[i-1]
        val_droite = L[i]
        a,b = val_gauche[0],val_gauche[1]
        c,d = (a+val_droite[0])//2,(b+val_droite[1])//2
        
        new.write(struct.pack("h",a))
        new.write(struct.pack("h",b))
        
        new.write(struct.pack("h",c))
        new.write(struct.pack("h",d))
        
        
    new.close()

the_walldoubl = towavdoubl(the_wall)
    

