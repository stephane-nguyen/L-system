#! python3
# -*- coding: utf8 -*-

#Fonction qui genere l'entete du fichier de python
def insert_header_file():
    header = "#! python3\n"
    header += "# -*- coding: utf8 -*\n"
    header += "from turtle import *\n"
    header += "title(\"L-system image\")\n"
    header += "color(\"black\")\n"
    header += "speed(0)\n"
    return header


#Fonction qui enregistre dans un fichier l'interpretation de l'axiome
def generate_file(filename:str, axiome, taille, angle):
    nb_crochet = 0
    #Ouverture fichier et initialisation turtle
    fichier = open(filename, "w")
    #Insertion de l'entete du fichier de sortie
    fichier.write(insert_header_file())
    # Traitement caractère un à un
    for char in axiome:
        if( char == 'a'):
            fichier.write(f"pd(); fd({taille})\n") 
        elif( char =='b') :
            fichier.write(f"pu(); fd({taille})\n") 
        elif( char == '-'):
            fichier.write(f"left({angle})\n") 
        elif( char == '+'):
            fichier.write(f"right({angle})\n")
        elif( char == '*'):
            fichier.write("right(180)\n")
        elif( char == '['):
            fichier.write(f"pos_{nb_crochet} = pos(); ang_{nb_crochet} = heading()\n")
            nb_crochet = nb_crochet+1
        elif( char == ']'):
            nb_crochet = nb_crochet-1
            if(nb_crochet >= 0):
                fichier.write(f"pu(); setpos(pos_{nb_crochet}); setheading(ang_{nb_crochet})\n")      
            else :
                print(f"generate_file - ERREUR: ] est en trop.")
                exit()
        else:
            print(f"generate_file - ERREUR: '{char}' n'a pas d'interpretation graphique.")
            exit()
    fichier.write("exitonclick();\n")    
    fichier.close()    


