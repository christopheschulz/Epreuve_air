import sys

#partitionner(tableau T, entier premier, entier dernier, entier pivot)
def partitionner(tableau, premier, dernier, pivot):
    #  échanger T[pivot] et T[dernier]  // échange le pivot avec le dernier du tableau , le pivot devient le dernier du tableau
    tableau[pivot], tableau[dernier] = tableau[dernier], tableau[pivot]
    #j := premier
    j = premier
     #pour i de premier à dernier - 1 // la boucle se termine quand i = (dernier élément du tableau).
    for i in range(premier, dernier):
        # si T[i] <= T[dernier] alors échanger T[i] et T[j]      
        if tableau[i] <= tableau[dernier]:
            tableau[i], tableau[j] = tableau[j], tableau[i]
            # j := j + 1
            j += 1
    
    # échanger T[dernier] et T[j]
    # renvoyer j
    tableau[dernier], tableau[j] = tableau[j], tableau[dernier]
    return j

def choix_pivot(tableau, premier, dernier):
    return premier

#tri_rapide(tableau T, entier premier, entier dernier)
def tri_rapide(tableau, premier=None, dernier=None):
    
    if premier is None:
        premier = 0
    if dernier is None:
        dernier = len(tableau) - 1
    
    # si premier < dernier alors
            #pivot := choix_pivot(T, premier, dernier)
            #pivot := partitionner(T, premier, dernier, pivot)   
    if premier < dernier:
        pivot = choix_pivot(tableau, premier, dernier)
        pivot = partitionner(tableau, premier, dernier, pivot)
        
        # Ttri_rapide(T, premier, pivot-1)
        # tri_rapide(T, pivot+1, dernier)
        tri_rapide(tableau, premier, pivot - 1)  # Partie gauche
        tri_rapide(tableau, pivot + 1, dernier)  # Partie droite
    
    return tableau

def verification_arguments(arguments):
    ok = False  
    all_arguments_int = all(arg.isdigit() for arg in arguments)
    if all_arguments_int:
        ok = True
    return ok


def afficher(chaine):
    for c in chaine:
       print(c,end=" ")
    print()


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        resultat = tri_rapide(arguments)
        afficher(resultat)
    else:
        erreur()