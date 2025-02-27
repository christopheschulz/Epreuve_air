import sys

def pass_sanitaire(array,controle):
    result = []

    for word in array:
        if controle.lower() not in word.lower():
            result.append(word)

    return result
    

def args_are_valid(arguments):
     
    if len(arguments[-1]) != 1:
        return False
    return True


def display(chaine):
    if len(chaine) == 1:
        print(chaine[0])
    else:
        for i in range(len(chaine)-1):
            print(chaine[i],end=", ")
        print(chaine[-1])
        print()


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        resultat = pass_sanitaire(arguments[:-1],arguments[-1])
        display(resultat)
    else:
        error()


if __name__ == "__main__":
    main()