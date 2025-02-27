# Chercher l’intrus

import sys

def chercher_intru(array):
    dictionnaire = {}
    for i in range(len(array)):
        # on vérifie si le dictionnaire existe
        if dictionnaire.get(array[i], 0) == 0:
            # sinon on le crée
            dictionnaire[array[i]] = 1
        else: 
            # si il existe on incrémente
            dictionnaire[array[i]] += 1
    
    for keys,value in dictionnaire.items():
        if value == 1:
            return keys

    erreur()


def args_are_valid(arguments):
      
    if not len(arguments) > 2:
        return False
    return True


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        print(chercher_intru(arguments))
    else:
        erreur()