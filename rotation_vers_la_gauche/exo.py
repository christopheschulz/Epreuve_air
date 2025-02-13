import sys


def ma_rotation(array):
    result =[]
    for i in range(1,len(array)):
        result.append(array[i])
    result.append(array[0])   
    return result


def verification_arguments(arguments):
    ok = False
    if len(arguments) > 1:
        ok = True
    return ok


def afficher(chaine):
    if len(chaine) == 1:
        print(chaine[0])
    else:
        for i in range(len(chaine)-1):
            print(chaine[i],end=", ")
        print(chaine[-1])


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        resultat = ma_rotation(arguments)
        afficher(resultat)
    else:
        erreur()