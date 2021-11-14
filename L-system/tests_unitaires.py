#! python3
# -*- coding: utf8 -*-

import os
from sys import *
from load_data import *

while 1:
    test_number = 0
    print("##############################################################")
    print("TESTS UNITAIRES ")
    print("----------------")
    print("1 - Vérfication de la mise en forme pour les règles")
    print("2 - Vérfication le type des éléments")
    print("3 - Vérfication d'occurence d'éléments")
    print("4 - Vérfication de présence de lignes blanches")
    print("5 - Vérfication de la présence de tous les éléments")
    print("6 - Vérfication des éléments en début de ligne sauf regles et non un mot ou caractère perturbateur")
    print("7 - Détéction d'erreur dans le cas où un symbole de croissance n'existe pas dans les règles")
    print("8 - Détéction d'erreur dans le cas où un symbole de croissance n'a pas d'interprétation graphique")
    print("9 - Détéction d'erreur dans le cas où il y a trop de fermeture de corchet")
    try:
        test_number = int(input("Entrez le numéro du test: \n"))
    except:
        pass
    finally:
        if test_number == 1:   
            load_data_from_file("./Tests_Unitaires/ruleform.txt")
        elif test_number == 2:
            load_data_from_file("./Tests_Unitaires/checktype.txt")
        elif test_number == 3:
            load_data_from_file("./Tests_Unitaires/elt_occ.txt")
        elif test_number == 4:
            load_data_from_file("./Tests_Unitaires/noblank.txt")
        elif test_number == 5:
            load_data_from_file("./Tests_Unitaires/presence_elt.txt")
        elif test_number == 6:
            load_data_from_file("./Tests_Unitaires/carac_not_elt.txt")
        elif test_number == 7:
            os.system("py main.py -i ./Tests_Unitaires/abs_symb_crois.txt")
            exit()
        elif test_number == 8:
            os.system("py main.py -i ./Tests_Unitaires/abs_inter_symb.txt")
            exit()
        elif test_number == 9:
            os.system("py main.py -i ./Tests_Unitaires/trop_crochet_ferme.txt")
            exit()        
        else:
            print("ERREUR: vous devez entrer un des numéros de test proposé")
        
       