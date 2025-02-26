
import sys

def fonction_concat(array_de_string,separateur):
    result = ""
    for i,ar in enumerate(array_de_string,1):
        if i != len(array_de_string):
            result += ar + separateur
        else :
            result += ar
    return result

   


def verification_arguments(arguments):
    ok = False
    
    if len(arguments) > 2:
        ok = True
    return ok


def afficher(chaine):
    pass

def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(fonction_concat(arguments[:-1],arguments[-1]))
    else:
        erreur()