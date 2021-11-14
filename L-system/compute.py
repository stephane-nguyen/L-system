#! python3
# -*- coding: utf8 -*-

from toolsbox import *

#Fonction qui applique les regles de croissances
def growth_L_system(axiome, regles):
    new_axiome = ''
    for char in axiome:
        if (char.isalpha() == True):
            #Dans le cas d'une lettre, on doit trouver la regle associée
            if(char in regles):
                new_axiome = new_axiome + regles[char]
            else:
                print(f"Growth_L_system - ERREUR: '{char}' n'a pas de règle de croissance")
                exit()
        else: 
            #Dans le cas d'un caractère autre qu'une lettre, on recopie ce caractere
            new_axiome = new_axiome + char         
    return new_axiome


#Fonction qui applique les regles de croissances
def compute_L_system(ax, rules, level):
    nb_loop = 1
    # Tant que l'on n'a pas atteint le niveau demandé, on réapplique la croisssance de l'axiome
    while nb_loop <= level:
        print(f"Step n°{nb_loop}")
        ax = growth_L_system(ax, rules)
        #print_L_system(ax,rules)
        #print_small_separator()
        nb_loop +=1
    return ax
    