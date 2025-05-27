# -*- coding: utf-8 -*-
"""
Created on Wed May 14 13:28:18 2025

@author: Administrateur
"""
from tkinter import Tk, Canvas, Button, Label
import numpy as np 
import random

#Exercice 1 


graph = [[2,7,3],[3,4,9,10],[5,8,0],[10,1,4,6,0],[3,1,6],[2],[3,10,4],[0],[2],[10,1],[3,1,6,9]]

class App:
    def posi(self):
        return np.array([(random.randint(20,580),random.randint(20,580)) for i in range(len(self.graph))])
    
    def quitter(self): self.root.destroy()
    
    def force_elas(self):
        L = np.array([(None,None) for i in range(len(self.graph))])
        
        for i in range(len(self.graph)):
            (xA,yA) = self.pos[i]
            force_i = np.array([0,0])
            
            for j in self.graph[i]:
                
                (xB,yB) = self.pos[j]
                dx,dy = xA-xB,yA-yB
                
                dist = (dx**2+dy**2)**0.5
                
                if dist == 0:
                    continue

                direction = np.array([dx, dy]) / dist
                allongement = dist - 50  
                force = allongement * direction  

                force_i = force_i - force 

            L[i] = force_i*0.1
            
        return L
        
    def vit(self):
        return np.array([((random.random()-0.5)*10,(random.random()-0.5)*10) for i in range(len(self.graph))])
    
    def tirage(self,e):
            self.pos = self.pos  + self.force_elas()*0.1
            self.draw()
    
    def __init__(self,graph):
        self.root = Tk()
        self.graph = graph
        self.can = Canvas(self.root, width=600, height=600, bg="white")
        self.can.grid(row=0, column=0, columnspan=3)
        
        self.pos = self.posi()
        
        boutton = Button(self.root, text="Quitter", command=self.quitter)
        boutton.grid(row=2, column=0)
        

        self.root.bind("<f>", self.tirage)
        
        self.draw()
 
    
    def draw(self):
        self.can.delete("all")
        for i in range(len(self.graph)):
            (x,y) = self.pos[i]
            for j in self.graph[i]:
                self.can.create_line(x,y,self.pos[j][0],self.pos[j][1])
            self.can.create_oval(x-8,y-8,x+8,y+8,fill="#f3e1d4")
        for i in range(len(self.graph)):
            (x,y) = self.pos[i]
            self.can.create_text(x,y,text=f"{i}")
        
            
    
    def run_forever(self):
        self.root.mainloop()
        
app = App(graph)
app.run_forever()