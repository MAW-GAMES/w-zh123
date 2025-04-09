#Depaoli Ugo
#Bergeot Loïc

from fltk import *
from projet_2d import cree_plateau

   
def grille(taille,taille_case) :
    for y in range(0,taille* taille_case, taille_case) :
        for x in range(0,taille* taille_case,taille_case) :
            rectangle(x,y,x+taille_case,y+taille_case)
        

def pixel_vers_case(x,y,taille_case) :
    #fais correspondre la case par rapport aux coordonnées du clic
    x = (x-1)//taille_case
    y = (y-1)//taille_case
    
    return[x,y]
    
    
def case_vers_pixel(x,y,taille_case,mid_case) :
    #fais correspondre le milieu de la case
    x=((x+1)* taille_case)-mid_case
    y= ((y+1)* taille_case)-mid_case
    
    return [x,y]


def couleur(joueur) :
    #donne le code de la couleur selon la valeur
    valeur = joueur [1]
    
    if valeur == "X" :
        couleur ="#3368ff"
    elif valeur == "O" :
        couleur = "#f31414"
    else :
        couleur = "black"
        
    return couleur

    
def affichage_pion(plateau,taille_case,mid_case) :
    #prend des coordonnées et affiche la valeur correspondante de ce point
    long = len(plateau)
    
    for b in range (long) :
        for a in range (long) :
            if plateau[b][a] != False and plateau[b][a] != True :
                 co = case_vers_pixel(a,b,taille_case,mid_case)
                 x = co[0]
                 y = co[1]
                 joueur = [0,plateau[b][a]]
                 remplis = couleur(joueur)
                 cercle(x,y,12,remplissage = remplis)


def affichage_plateau(plateau,taille_case,taille,mid_case,diag) :
    #affiche le plateau en entier
    taille_f = taille_case*taille
    mid = (taille-1)//2
    
    if taille != 3 :
        for b in range(0,taille) :
            for a in range(0,taille) :
                lst = case_vers_pixel(a,b,taille_case,mid_case)
                y = lst[1]
                x = lst[0]
                x1 = x-mid_case
                y1 = y-mid_case
                x2 = x+ mid_case
                y2 = y+mid_case
                if plateau[b][a] != False :
                    cercle(x,y,9,remplissage = "black")
                        
                if a<mid and a == b:
                    #bord haut droit
                    ligne(x,y,x,y2,epaisseur = 3)
                    ligne(y,x,y2,x,epaisseur = 3)
                if a>mid and a == b :
                    #bord haut gauche
                    ligne(x1,taille_f - y,x,taille_f - y,epaisseur = 3)
                    ligne(y,taille_f - x1,y,taille_f - x,epaisseur = 3)
                    #bord bas droit
                    ligne(x1,y,x,y,epaisseur = 3)
                    ligne(y,x1,y,x,epaisseur = 3)
                if a>mid and a == b:
                    #bord bas gauche
                    ligne(taille_f - x1,y,taille_f - x,y,epaisseur = 3)
                    ligne(taille_f - y,x1,taille_f - y,x,epaisseur = 3)
                    
                if (a== 0 or a == mid+1) and b == mid :
                    #croix vers droite
                    ligne(x,y1,x,y2,epaisseur = 3)
                    ligne(x2,y,x,y,epaisseur = 3)
                if (a== taille-1 or a == mid-1) and b == mid :
                    #croix vers gauche
                    ligne(x,y1,x,y2,epaisseur = 3)
                    ligne(x,y,x1,y,epaisseur = 3)
                if (b== taille-1 or b == mid-1) and a == mid :
                    #croix vers haut
                    ligne(x1,y,x2,y,epaisseur = 3)
                    ligne(x,y1,x,y,epaisseur = 3)
                if (b== 0 or b == mid+1) and a == mid :
                    #croix vers bas
                    ligne(x,y2,x,y,epaisseur = 3)
                    ligne(x1,y,x2,y,epaisseur = 3)
                    
                if b !=mid and ((0<b<(taille-1) and (a==0 or a == (taille-1))) or (1<b<5 and (a==1 or a == 5)) and taille == 7) :
                    #ligne entiere
                    ligne(y1,x,y2,x,epaisseur = 3)
                if a !=mid and ((0<a<(taille-1) and (b==0 or b == (taille-1))) or (1<a<5 and (b==1 or b == 5)) and taille == 7) : 
                    #colonne entiere 
                    ligne(y,x1,y,x2,epaisseur = 3)
                if taille == 7 and (((b== 1 or b == 5) and a == mid) or ((a== 1 or a == 5) and b == mid)) :
                    #croix
                    ligne(x,y1,x,y2,epaisseur = 3)
                    ligne(y1,x,y2,x,epaisseur = 3)

                
                
                if diag and (a != 3 or b !=3):
                    
                    #diag de (0,0) a (6,6)
                    if (a == b == 0) or (a == b == 4) :
                        #moitié droite diag gauche haut
                        ligne(x,y,x2,y2,epaisseur = 3)
                    if (a == b == 2) or (a == b == 6) :
                        #moitié gauche diag gauche haut
                        ligne(x1,y1,x,y,epaisseur = 3)
                    if  (a == b == 1) or (a == b == 5) :
                        #diag gauche haut
                        ligne(x1,y1,x2,y2,epaisseur = 3)
                        
                    #diag de (0,6) a (6,0)
                    if (b == 0 and a == 6) or (b == 4 and a == 2) :
                        #moitié droite diag droite haut
                        ligne(x1,y2,x,y,epaisseur=3)
                    if (a == 0 and b == 6) or (a == 4 and b == 2) :
                        #moitié gauche diag droite haut
                        ligne(x,y,x2,y1,epaisseur=3)
                    if (a == 5 and b == 1) or (a == 1 and b == 5) :
                        #diag droite haut
                        ligne(x1,y2,x2,y1,epaisseur=3)
    else :
        #cercles
        for a in range(1,6,2) :
            for b in range(1,6,2) :
                cercle(b*mid_case,a*mid_case,9,remplissage = "black")
        #diagonales
        ligne(mid_case,mid_case,taille_f-mid_case,taille_f-mid_case,epaisseur = 3)
        ligne(mid_case,taille_f-mid_case,taille_f-mid_case,mid_case,epaisseur = 3)
        #carré
        ligne(mid_case,mid_case,mid_case,taille_f-mid_case,epaisseur = 3)
        ligne(taille_f-mid_case,mid_case,mid_case,mid_case,epaisseur = 3)
        ligne(taille_f-mid_case,taille_f-mid_case,taille_f-mid_case,mid_case,epaisseur = 3)
        ligne(mid_case,taille_f-mid_case,taille_f-mid_case,taille_f-mid_case,epaisseur = 3)
        #croix centrale
        ligne(3*mid_case,mid_case,3*mid_case,taille_f-mid_case,epaisseur = 3)
        ligne(mid_case,3*mid_case,taille_f-mid_case,3*mid_case,epaisseur  = 3)


def choix (largeur):
    #creer les parametres selon le plateau choisis
    taille_f = largeur*105
    mid_f = taille_f/2
    case_f = taille_f/5
    espace_f = case_f/5
    lst = []
    
    texte(mid_f-102,espace_f,"Mühle",taille=51)
    texte(mid_f-(2*case_f),case_f,"veuillez choisir votre nombre de pions", taille = 22)
    #affichage des options
    
    #3 pions
    rectangle(espace_f,mid_f - (case_f//2),espace_f+case_f,mid_f + (case_f//2))
    texte(espace_f + 30,mid_f-16,"3")
    cercle(espace_f + 70,mid_f,9,remplissage="black")
    
    #5 pions
    rectangle(2*espace_f + case_f ,mid_f - (case_f//2),2*espace_f+2*case_f,mid_f + (case_f//2))
    texte(2*espace_f+case_f + 30,mid_f-16,"6")
    cercle(2*espace_f+case_f + 70,mid_f,9,remplissage="black")
    
    #7 pions
    rectangle(3*espace_f + 2*case_f ,mid_f - (case_f//2),3*espace_f+3*case_f,mid_f + (case_f//2))
    texte(3*espace_f+2*case_f + 30,mid_f-16,"9")
    cercle(3*espace_f+2*case_f + 70,mid_f,9,remplissage="black")
    
    #9 pions
    rectangle(4*espace_f + 3*case_f ,mid_f - (case_f//2),4*espace_f+4*case_f,mid_f + (case_f//2))
    texte(4*espace_f+3*case_f + 30,mid_f-16,"12")
    cercle(4*espace_f+3*case_f + 75,mid_f,9,remplissage="black")
    
    #attend le choix
    ev = attend_ev()
    ty = type_ev(ev)
    if ty == "ClicGauche" :
        i = abscisse(ev)
        j = ordonnee(ev)
    
    #renvoie la liste correspondant aux options choisies
    if mid_f-(case_f/2)< j < mid_f+(case_f/2) :
        if espace_f<i<espace_f+case_f :
            taille = 3
            diag = True
            nb_pion = 3
        if 2*espace_f+case_f<i<2*espace_f+2*case_f :
            taille = 5
            diag = False
            nb_pion = 6
        if 3*espace_f+2*case_f<i<3*espace_f+3*case_f :
            taille = 7
            diag = False
            nb_pion = 9
        if 4*espace_f+3*case_f<i<4*espace_f+4*case_f :
            taille = 7
            diag = True
            nb_pion = 12
        
        
        plateau =cree_plateau(taille)
        taille_case = largeur * 105//taille
        mid_case = taille_case//2
        lst.append(taille)
        lst.append(plateau)
        lst.append(taille_case)
        lst.append(mid_case)
        lst.append(diag)
        lst.append(nb_pion)
        efface_tout()
    else :
        efface_tout()
        lst = choix(largeur)
        
    return lst