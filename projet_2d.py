#Depaoli Ugo
#Bergeot Loïc
def cree_plateau (taille) :
    """
    Reçoit une taille (3, 5 ou 7) qui renvoie une liste de listes de la longueur de cette taille.
    Les False correspondes aux aux endroits non jouable, et les True des case jouables
    
    >>> taille = 5
    >>> cree_plateau (taille)
    [[True, False, True, False, True],[False, True, True, True, False],[True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    """
    
    #cree un plateau et les emplacements jouables
    plateau = []
    mid = (taille-1)//2
    
    #cree le plateau
    for x in range(0,taille) :#rajoute le nombre de ligne necessaire
        lst =[]
        for x in range(0,taille) :#cree une ligne
            lst.append(False)
        plateau.append(lst)
    
    #cree les cases jouables
    for a in range(0,taille) :
        plateau[a][a] = True
        plateau[a][taille-1-a] =True
        plateau[a][mid] = True
        plateau[mid][a] = True
    
    #retire le centre sauf pour la plus petite version
    if taille != 3 :
        plateau[mid][mid] = False
        
    return plateau


def placement(x,y,plateau,joueur) :
    """
    Reçoit les coordonnées correspondant a une case dans le plateau, un plateau,
    regarde si cette case est jouable puis place le pion du joueur.
    joueur correspond à une liste contennant le nombre de pion ainsi que la valeur de ces pionts
    return True si un coup est joué, False sinon
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> placement(0,0,plateau,[0,"X"])
    >>> plateau
    [['X', False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    """
    
    #place le pion lors de la phase 1
    val = joueur[1]
    
    if plateau[y][x] == True:
        plateau[y][x] = val
        joueur[0] +=1
        return True
    else :
        return False


def moulin(x,y,plateau,joueur,diag): 
    """
    Reçoit les coordonnées d'un pion du joueur, un plateau, regarde si ce pion se trouve dans un moulin
    en fonction de sa position et des diagonales si elles sont activées.
    Elle renvoit True si le pion se trouve dans un moulin, et False sinon.
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> placement (0,0,plateau,[0,"X"])
    >>> placement (0,2,plateau,[1,"X"])
    >>> placement (0,4,plateau,[2,"X"])
    >>> plateau
    [["X", False, True, False, True], [False, True, True, True, False], ["X", True, False, True, True], [False, True, True, True, False], ["X", False, True, False, True]]
    >>> Moulin (0,0,plateau,[2,"X"])
    True
    """
    
    #verifie si un moulin est "effectue"
    val = joueur[1]
    long = len(plateau)
    gagne= []
    lst1 = []
    lst2 = []
    mid = (long-1)//2
    
    #le plus grand carré
    if x == 0 or y == 0 or x == mid or y == mid or x==long-1 or y ==long-1:
        for a in range(0,long,mid) :
            lst1.append(plateau[y][a])
            lst2.append(plateau[a][x])
        gagne.extend((lst1,lst2))
        lst1 = []
        lst2 = []
    
    #le plus petit carré
    bord_droit = long-mid
    bord_gauche = mid-1    
    if x == bord_gauche or y == bord_gauche or x == mid or y == mid or x==bord_droit or y ==bord_droit :
        for a in range(bord_gauche,bord_droit+1) :
            lst1.append(plateau[y][a])
            lst2.append(plateau[a][x])
        gagne.extend((lst1,lst2))
        lst1 = []
        lst2 = []
    
    if long == 7 : #le carré entre pour la plus grade taille de plateau
        if x == 1 or y == 1 or x == mid or y == mid or x==long-2 or y ==long-2:
            for a in range(1,long-1,2) :
                lst1.append(plateau[y][a])
                lst2.append(plateau[a][x])
        gagne.extend((lst1,lst2))
        lst1 = []
        lst2 = []
        
    if diag :
        if x < 3 :
            for a in range(0,3) :
                if x == y :
                    lst1.append(plateau[a][a])
                if x+y == long-1 :
                    lst1.append(plateau[a][long-1-a])
        if x > 3 :
            for a in range(4,long) :
                if x == y :
                    lst1.append(plateau[a][a])
                if x+y == 6 :
                    lst1.append(plateau[a][long-1-a])
        gagne.append(lst1)
            
    for trio in gagne : #verifie si un moulin a bien lieu
        if len(trio) == 3 :
            if trio[0] == trio[1] == trio[2] == val :
                return True
    return False


def moulin_pion(plateau,joueur,diag) :
    """
    Reçoit un plateau, regarde combien de pions se trouvent dans des moulins.
    Elle renvoit True si tout les pions sont dans des moulins, et False sinon.
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> placement (0,0,plateau,[0,"X"])
    >>> placement (0,2,plateau,[1,"X"])
    >>> placement (0,4,plateau,[2,"X"])
    >>> moulin_pion(plateau,[3,"X"],False])
    True
    >>> placement (2,0,plateau,[3,"X"])
    >>> moulin_pion (plateau,[4,"X"],,False)
    False
    """
    
    #regarde si tout les pions d'un joueur sont dans un moulin ou non
    compteur_moulin = 0
    compteur_pion = joueur[0]
    val = joueur[1]
    
    for b in range(len(plateau)) :
        for a in range(len(plateau)) :
            if plateau[b][a] == val and moulin(a,b,plateau,joueur,diag) :
                compteur_moulin +=1
    
    if compteur_moulin == compteur_pion :
        return True
    else :
        return False


def retirer_pion(x,y,plateau,joueur_adverse,diag) : #a modifier
    """
    Reçoit les coordonnées d'un pion du joueur adverse, retire ce pion en fonction
    d'où il se trouve, si il est dans un moulin mais que tout les pions ne sont pas
    dans des moulins alors le pions n'est pas retieré. Si tout les pions sont dans un
    moulin alors il est peut importe où il se trouve. Et si le pion n'est pas dans un moulin
    alors il est retiré.
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> placement (0,0,plateau,[0,"X"])
    >>> plateau
    [["X", False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> retirer_pion(0,0,plateau,[0,"X"],False)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    """
   #retire un pion suite a un moulin
    pions = joueur_adverse[0]
    
    if pions > 3 :
        if moulin_pion(plateau,joueur,diag) :
            plateau[y][x] = True
            joueur_adverse[0] -= 1
        elif not moulin(x,y,plateau,joueur_adverse,diag) :#verifie que le pion n'est pas dans un moulin
            plateau[y][x] = True #retire le pion
            joueur_adverse[0] -= 1
    else :
        plateau[y][x] = True
        joueur_adverse[0] -= 1


def perdu (plateau,joueur_adverse,diag) :
    """
    Reçoit un plateau, regarde si un joueur possède moins de 3 pions, si c'est
    le cas alors elle renvoit True, de plus si il est impossible de se déplacer
    elle renvoit aussi True car dans ce cas la on a aussi perdue. Dans les autres
    cas elle renvoit False : personnes n'a encore perdue.
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> placement (0,0,plateau,[0,"X"])
    >>> placement (0,2,plateau,[1,"X"])
    >>> perdu (plateau,[1,"X"],False)
    True
    """
    
    #renvoie True si on a perdu, False si ce n'est pas le cas
    val = joueur_adverse[1]
    lst=[]
    test=[]
    
    #parcours la liste pour regarder s'il y a moins de 3 pion pour un joueur
    if joueur_adverse[0] < 3:
        return True
    #impossible de se deplacer
    else :
        for b in range(len(plateau)) :
            for a in range(len(plateau)) :
                if plateau[b][a] == val :
                    lst.append([a,b])
        for co in lst :
            x = co[0]
            y = co[1]
            voisins_co = voisins(x,y,plateau,diag)
            for voisin in voisins_co :
                a=voisin[0]
                b=voisin[1]
                if plateau[b][a]== True :
                    test.append(1)
        if len(test) == 0 :
            return True
        
    return False


def voisins(x,y,plateau,diag):
    """
    reçoit les coordonnées d'un case du plateau, regarde les emplacements de jouables autours de
    ce pion en fonction de l'avancement de la partie. La fonction renvoit une liste de tout ces emplacement
    jouables.
    >>> taille = 5
    >>> plateau = cree_plateau (taile)
    >>> voisins(0,0,plateau,False)
    [[2, 0], [0, 2]]
    """
    
    #renvoie la liste des coordonnées des emplacement jouable voisins
    lst = []
    long = len(plateau)
    mid = (long-1)//2
    
    #lignes
    if x == 0 or x == long-1 : #grand carré
        if (y == 0 or y == long-1) and y != mid :
            lst.append([x,mid])
        if y == mid :
            lst.extend(([x,0],[x,long -1]))

    if long == 7 and (x == 1 or x == 5) : # carré du milieu
        if y == 1 or y == long -2 :
            lst.append([x,mid])
        if y == mid :
            lst.extend(([x,1],[x,long -2]))

    if long != 3 and (x == mid-1 or x == mid+1) : #plus petit carré
        if y == mid-1 or y == mid+1 :
            lst.append([x,mid])
        if y == mid :
            lst.extend(([x,mid-1],[x,mid+1]))

    if x == mid : #lignes du milieu
        if y == 0 or y == 4 :
            lst.append([x,y+1])
        if y == 2 or y == 6 or (long == 5 and y == 1):
            lst.append([x,y-1])
        if long !=5 and (y == 1 or y == 5) :
            lst.extend(([x,y-1],[x,y+1]))

    #colonnes
    if y == 0 or y == long-1 :#grand carré
        if (x == 0 or x == long-1) and x != mid :
            lst.append([mid,y])
        if x == mid :
            lst.extend(([0,x],[long-1,y]))

    if long == 7 and (y == 1 or y == 5) :# carré du milieu
        if x == 1 or x == long -2 :
            lst.append([mid,y])
        if x == mid :
            lst.extend(([1,y],[long -2,y]))

    if long != 3 and (y == mid-1 or y == mid+1) :#plus petit carré
        if x == mid-1 or x == mid+1 :
            lst.append([mid,y])
        if x == mid :
            lst.extend(([mid-1,y],[mid+1,y]))

    if y == mid : #colonnes du milieu
        if x == 0 or x == 4 :
            lst.append([x+1,y])
        if x == 2 or x == 6 or (long == 5 and x == 1):
            lst.append([x-1,y])
        if long !=5 and (x == 1 or x == 5) :
            lst.extend(([x-1,y],[x+1,y]))
    
    #diagonales
    if diag and (long == 7 or long == 3): 
        if x != 3 :
            if x == y :
                if (x == mid-1 or x == long-1) and x !=0 :
                    lst.append([x-1,y-1])
                elif (x == 0 or x == mid + 1) and x != long -1 :
                    lst.append([x+1,y+1])
                elif x == 1 or x == 5 :
                    lst.extend(([x+1,y+1],[x-1,y-1]))
            if x+y == long-1 :
                if (x == mid-1 or x == long-1) and x !=0 :
                    lst.append([x-1,y+1])
                elif (x == 0 or x == mid + 1) and x != long -1 :
                    lst.append([x+1,y-1])
                elif x == 1 or x == 5 :
                    lst.extend(([x+1,y-1],[x-1,y+1]))
                    
    for a in range (len(lst)-1,-1,-1) :
        b = lst[a]
        if b[0] == mid and b[1] == mid and not plateau[mid][mid] :
            lst.pop(a)
    return lst


def deplacement(x1,y1,x2,y2,plateau,joueur,diag) :
    """
    Reçoit les coordonnées d'un pion d'un pion se trouvant sur le plateau ainsi que les cvoordonées où l'on souhaite se déplacer.
    En fonction de l'avancement du jeu, on peut se déplcé plus ou moins loins. Donc si le déplacement est possible, la fonction
    déplace le pions des coordonnées x1 et y1 aux coordonnées x2 et y2.
    >>> taille = 5
    >>> plateau = cree_plateau (taille)
    >>> placement(0,0,plateau,[0,"X"])
    >>> plateau
    [["X", False, True, False, True], [False, True, True, True, False], [True, True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    >>> deplacement(0,0,0,2,plateau,[1,"X"],False,False)
    >>> plateau
    [[True, False, True, False, True], [False, True, True, True, False], ['X', True, False, True, True], [False, True, True, True, False], [True, False, True, False, True]]
    """
    #depalce un pion d'un joueur 
    lst_voisin = voisins(x1,y1,plateau,diag)
    val = joueur[1]
    saut = joueur[3]
    
    plateau_backup = []
    #creer une sauvegarde du plateau
    for b in plateau :
        lst = []
        for a in plateau :
            lst.append(a)
        plateau_backup.append(lst)
    #print(plateau_backup)
    
    if plateau[y1][x1] == val and plateau[y2][x2] == True :#verifie que le pion choisis est bien celui du joueur et que l'emplacement jouer est disponible
        if saut :
            plateau[y1][x1] = True #supprime le pion de base
            plateau[y2][x2] = val #le remet sur la nouvelle case
        else :
            for co in lst_voisin:#verifie que le deplacement est possible sans saut
                if x2 == co[0] and y2 == co[1] :
                    plateau[y1][x1] = True
                    plateau[y2][x2] = val
    
    if plateau != plateau_backup : #compare si un changement à bien été fait
        return True
    else :
        return False