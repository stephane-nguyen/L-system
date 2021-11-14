#! python3
# -*- coding: utf8 -*-

from sys import *
from toolsbox import *
from load_data import *
from compute import *
from generate import *


#---------- Locals functions ------------#
# La config par defaut sera le flocon de Koch
def load_default_L_system():
    axiome = "-a++ba++a"
    regles = { "a":"a-a++a-a", "b":"bb+b-a+b-bb"}
    return axiome, regles

def load_default_parametres():
    angle = 60
    taille = 10
    niveau = 2
    return angle, taille, niveau

def print_all():
    print_L_system(axiome,regles)
    print_angle(angle)
    print_taille(taille)
    print_niveau(niveau)
    print_separator()

def print_help():
    print(f"{argv[0]} est une progrmame modélisant la croissance des plantes à partir d'un L-system.")
    print(f"Les paramètres:")
    print(f"-h : affichage de cette aide.")
    print(f"-i : permet de spécifier le fichier contenant les données d'entrée du L-system")
    print(f"-o : permet de spécifier le fichier de sortie contenant l'image resultante du L-system")
    
def parameters_analysis():
    #Index = 1 car argc[0] contient le nom du programme
    index=1
    #Recherche des options "-i" et "-o"
    while index < len(sys.argv):
        if sys.argv[index] == "-h":
            print_help()
            index = index + 1
        elif sys.argv[index] == "-i":
            global DATAFILE
            DATAFILE = sys.argv[index+1]
            index = index + 2
        elif  sys.argv[index] == "-o":
            global OUTPUTFILE
            OUTPUTFILE = sys.argv[index+1]
            index = index + 2  


#---------------- Main ------------------#

#Paramètre fichier
DATAFILE = ""
OUTPUTFILE = "./outputfile_image.py"

#Initialisation
axiome = ""
regles = {}
angle = .0
taille = 0
niveau = 0

#Analyse des paramètres d'entrée
parameters_analysis()
if DATAFILE == "":
    print(f"ERREUR: Aucun fichier d'entrée L-system, veuillez utiliser l'option -i suivi du nom du fichier")
    exit()
#Chargement du fichier d'entrée
print(f"Chargement des données du L-system à partir du fichier {DATAFILE}")
load_data_from_file(DATAFILE)
#Chargement du fichier est OK, on peut recupérer les informations
(axiome,regles) = get_L_system()
(angle, taille, niveau) = get_parametres()
#Calcul de croissance du L-system
print("Calcul de la croisssance du L-system")
axiome = compute_L_system(axiome, regles, niveau)
#Generation du fichier image
print(f"Génération du fichier python {OUTPUTFILE}")
generate_file(OUTPUTFILE, axiome, taille, angle)
#Execution du fichier pour voir le résultat
print(f"Excution du fichier python {OUTPUTFILE}")
exec(open(OUTPUTFILE).read())



