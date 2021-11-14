#! python3
# -*- coding: utf8 -*-

#Ce fichier contient toutes les fonctions de bases réutilisables dans les modules

def print_separator():
    print("-----------------------------")

def print_small_separator():
    print("---------------")

def print_axiome(axiome):
    print(f"axiome\t= {axiome}")


def print_regles(regles):
    print(f"regles: (nb= {len(regles)})")
    for (clé, valeur) in regles.items():
        print(f"\t{clé} = {valeur}")

    
def print_L_system(axiome, regles):
    print_axiome(axiome)
    print_regles(regles)

def print_angle(a):
    print(f"angle\t= {a}")

def print_taille(a):
    print(f"taille\t= {a}")

def print_niveau(a):
    print(f"niveau\t= {a}")
