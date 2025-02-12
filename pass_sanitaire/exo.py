import sys

def pass_sanitaire(array,controle):
    result = []

    for word in array:
        if controle.lower() not in word.lower():
            result.append(word)

    return result
    

def verification_arguments(arguments):
    ok = False  
    if len(arguments[-1]) == 1:
        ok = True
    return ok


def afficher(chaine):
    if len(chaine) == 1:
        print(chaine[0])
    else:
        for i in range(len(chaine)-1):
            print(chaine[i],end=", ")
        print(chaine[-1])
        print()


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        resultat = pass_sanitaire(arguments[:-1],arguments[-1])
        afficher(resultat)
    else:
        erreur()