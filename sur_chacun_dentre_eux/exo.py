import sys

def sur_chacun(array):
    result = []
    calcul = array[:-1]
    operateur = array[-1][0]
    calculateur = int(array[-1][1:])

    for i in range(len(calcul)):
        if operateur == "+":
            result.append(int(calcul[i]) + calculateur)
        elif operateur == "-":
            result.append(int(calcul[i]) - calculateur)
        if operateur == "*":
            result.append(int(calcul[i]) * calculateur)
        if operateur == "/":
            result.append(int(calcul[i]) / calculateur)
    
    return result


    


def verification_arguments(arguments):
    ok = False  
    operateur = ["+", "-", "*", "/"]
    all_digit = all(arg.isdigit() for arg in arguments[:-1])
    if arguments[-1][0] in operateur and all_digit:
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
        calcul = sur_chacun(arguments)
        afficher(calcul)
    else:
        erreur()