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


def args_are_valid(arguments): 
    operateur = ["+", "-", "*", "/"]
    all_digit = all(arg.isdigit() for arg in arguments[:-1])
    if arguments[-1][0] not in operateur and not all_digit:
        return False
    return True


def display(chaine):
    for c in chaine:
       print(c,end=" ")
    print()


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        calcul = sur_chacun(arguments)
        display(calcul)
    else:
        error()


if __name__ == "__main__":
    main()