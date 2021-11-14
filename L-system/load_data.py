#! python3
# -*- coding: utf8 -*-
import sys 
from toolsbox import *

#---------- Locals variables ------------#

loaded_axiome = ""
loaded_regles = {}
loaded_angle = .0
loaded_taille = 0
loaded_niveau = 0

def check_file_existence(filename):
    """vérif de l'existence du fichier"""
    try:
        open(filename, "r")  #ouverture fichier mode lecture 
    except FileNotFoundError:
        print("ERREUR: le fichier " + filename + " n'existe pas")
        sys.exit()

def no_blank_in_file(file_in_list):
    """seek for a blank line in the file"""
    #delete blank at the end of the file 
    while not "=" in file_in_list[len(file_in_list)-1]:
        del file_in_list[len(file_in_list)-1]
    for k in range(len(file_in_list)):
        if file_in_list[k] == "" or file_in_list[k] == "\t":
            print("ERREUR: il y a une ligne vide, le fichier n'est pas de la bonne forme")
            sys.exit()
            
def check_presence_occurence_elt(file_in_list, elt_list, isHere):
    """"vérif des éléments du fichier: on cherche si élt bien présents
    et cherche si pas occurence d'elt """
    for element in elt_list:
        occ = 0
        for k in range(len(file_in_list)):
            if element in file_in_list[k]:
                occ += 1
                isHere.append(element)
            if occ > 1: 
                print("ERREUR: occurence d'élément")           
                sys.exit()
    if len(isHere) < 5:
        print("ERREUR: le fichier ne contient pas tous les éléments d'un L-system")
        sys.exit()

def check_axiome_type(split_line):
    global loaded_axiome
    try:
        str(split_line[2])
    except ValueError:
        print("ERREUR: " + split_line[0] + " a un mauvais type")
        sys.exit()
    else:
        loaded_axiome = split_line[2]

def check_niveau_type(split_line):
    global loaded_niveau
    try:
        if split_line[2] == 0: #int ne prend pas en compte 0... bizarre 
            pass
        else:
            loaded_niveau = int(split_line[2])
    except ValueError:
        print("ERREUR: " + split_line[0] + " a un mauvais type")
        sys.exit()
  

def check_taille_type(split_line):
    global loaded_taille
    try:
        if split_line[2] == 0:
            pass
        else:
            loaded_taille = int(split_line[2])
    except ValueError:
        print("ERREUR: " + split_line[0] + " a un mauvais type")
        sys.exit()

def check_angle_type(split_line):
    global loaded_angle
    try:
        loaded_angle = float(split_line[2])
    except ValueError:
        print("ERREUR: " + split_line[0] + " a un mauvais type")
        sys.exit()


def treat_keyword(line, state):
    #Nettoyage des caractères
    clean_line = line.strip()
    #Suppression double cote
    clean_line = clean_line.replace("\"","")
    #Split de la chaine
    split_line = clean_line.split()
    if (split_line[0].upper() == "AXIOME"):
        state = "Keyword treated"
        check_axiome_type(split_line)
    elif (split_line[0].upper() == "REGLES"):
        state = "Rules sequence"     
        treat_rule(line, state)  
    elif (split_line[0].upper() == "ANGLE"):
        state = "Keyword treated"
        check_angle_type(split_line)
    elif (split_line[0].upper() == "TAILLE"):
        state = "Keyword treated"
        check_taille_type(split_line)
    elif (split_line[0].upper() == "NIVEAU"):
        state = "Keyword treated"
        check_niveau_type(split_line)
    else:
        print("ERREUR: fichier pas sous la bonne mise en forme; il y a des caractères situés à la place des éléments")
        sys.exit()
    return state


def treat_rule(line, state):
    #Nettoyage des caractères
    clean_line = line.strip()
    #Suppression double cote
    clean_line = clean_line.replace("\"","")
    #Split avec le = pour obtenir la cle (symbole) et sa valeur (information de croissance)
    split_line = clean_line.split("=")
    split_line[0] = split_line[0].strip()
    keyword_upper = split_line[0].upper()
    if (keyword_upper == 'REGLES'):
        if split_line[1] != "":
            print("ERREUR: Les règles sont attendues après la ligne \"Regles =\"")
            sys.exit()
    else:
        #ajout de clef si n'existe pas et valeur dans dictionnaire 
        loaded_regles.update( {split_line[0] : split_line[1]} )
    return state


def decode_line(line:str, state):
    #Test si le premier caractere est un alphabet
    if (line[0].isalpha() == True):
        state = treat_keyword(line, state)
    else:
        #Test si le premier caractere est un espace ou une tabulation
        if (line[0].isspace() == True) or "\t" in line[0]:
            #On teste si on est en état attente de règles
            if (state == "Rules sequence"):
                #On traite la ligne 
                state = treat_rule(line, state)               
            else:
                print("ERREUR: (regles) espace blanc, fichier pas de la bonne forme")
                sys.exit()
        else:
            print("ERREUR: (regles) espace blanc, fichier pas de la bonne forme")
            sys.exit()
    return state



#Fonction qui lit le fichier en paramètres et extrait l'ensemble des informations
#return True sir le chargement c'est bien passé sinon False
def load_data_from_file(filename: str): 
    #filename = input("Entrez le fichier d'entrée : \n")
    check_file_existence(filename)
    with open(filename, "r") as input_file:
        #init var for functions 
        elt_list = ["AXIOME", "ANGLE", "TAILLE", "NIVEAU", "REGLES"]
        isHere = []
        #transfère toutes les lignes du fichier (restantes) dans une liste de chaînes
        file_in_list = input_file.readlines()
        #Leading and trailing whitespaces are removed 
        file_in_list = [elt.strip() for elt in file_in_list]
        file_in_list = [elt.upper() for elt in file_in_list]
        #mise en forme du fichier 
        no_blank_in_file(file_in_list)
        check_presence_occurence_elt(file_in_list, elt_list, isHere)
        #Go back to the beginning of a file (because of readlines(), we are at the end of the file)
        input_file.seek(0, 0)
        state = "Init"    
        for line in input_file:
            #suppresion du retour à la ligne
            line = line.strip('\n')
            state = decode_line(line, state)


#Fonction qui retourne l'axiome et les règles
def get_L_system():
    axiome = loaded_axiome
    regles = loaded_regles
    return axiome, regles


#Fonction qui retourne les paramètres complémentaires au calcul
def get_parametres():
    angle = loaded_angle
    taille = loaded_taille
    niveau = loaded_niveau
    return angle, taille, niveau



