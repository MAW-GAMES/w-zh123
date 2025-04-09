from projet_2d import *
from projet_fltk import *

j1 = [0,"X","#3368ff",False] # compteur de pion, valeur du pion, couleur pour fltk
j2 = [0,"O","#f31414",False]

joueur = j1
joueur_adverse = j2

def affichage() :
    efface_tout()
    affichage_plateau(plateau,taille_case,taille,mid_case,diag)
    affichage_pion(plateau,taille_case,mid_case)
        
        
def clic() : #renvoie la case correspondant à l'endroit clicker
    lst = []
    ev = attend_ev()
    ty = type_ev(ev)
    
    if ty == "ClicGauche" : #prend uniquement un clic gauche
        x = abscisse(ev)
        y = ordonnee(ev)
        lst = [x,y]
    else : #si pas clic gauche
        lst = clic()
    #converti en coorodonnées pour le plateau
    co = pixel_vers_case(lst[0],lst[1],taille_case)
    return co

def alterne(joueur,j1,j2) :
    
    lst = []
    #alterne les joueurs
    if joueur == j1 :
        lst.append(j2)
        lst.append(j1)
    else :
        lst.append(j1)
        lst.append(j2)
    return lst


if __name__ == "__main__" :
    
    #initialisation
    largeur = 6
    cree_fenetre(largeur * 105 , #pour obtenir un centre parfait peu importe la largeur choisie
                 largeur * 105 ) # 3 * 7 * 5 = 105
    #choix du plateau
    choix_liste = choix(largeur)
    taille = choix_liste[0]
    plateau = choix_liste[1]
    taille_case = choix_liste[2]
    mid_case = choix_liste[3]
    diag = choix_liste[4]
    nb_pion = choix_liste[5]
    #affiche le plateau
    affichage()
    
    #phase 1
    while (j1[0] != nb_pion or j2[0] != nb_pion) :
        
        co = clic()
        x = co[0]
        y = co[1]
        p = placement(x,y,plateau,joueur)
        while not p :
            co = clic()
            x = co[0]
            y = co[1]
            p = placement(x,y,plateau,joueur)
        
        affichage()
        mise_a_jour()
        
        if moulin(x,y,plateau,joueur,diag) :
            co = clic()
            x = co[0]
            y = co[1]
            retirer_pion(x,y,plateau,joueur_adverse,diag)
            print(plateau)
        
        affichage()
        
        mise_a_jour()
        
        j = alterne(joueur,j1,j2)
        joueur = j[0]
        joueur_adverse = j[1]
    
    joueur = j1
    joueur_adverse = j2
    print("fin p1")
    
    ff = perdu(plateau,joueur,diag)
    while not ff :
        if j1[0] == 3 :
            j1[3] = True
        if j2[0] == 3 :
            j2[3] = True

        
        co1 = clic()
        x1 = co1[0]
        y1 = co1[1]
        
        co2 = clic()
        x2 = co2[0]
        y2 = co2[1]
        
        
        if deplacement(x1,y1,x2,y2,plateau,joueur,diag) :
            affichage()
            mise_a_jour()
            
            if moulin(x2,y2,plateau,joueur,diag) :
                co = clic()
                x = co[0]
                y = co[1]
                retirer_pion(x,y,plateau,joueur_adverse,diag)
                
            affichage()
            mise_a_jour()
            if plateau[y1][x1] :
                
                ff = perdu (plateau,joueur_adverse,diag)
                j = alterne(joueur,j1,j2)
                joueur = j[0]
                joueur_adverse = j[1]



