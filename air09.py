# Rotation vers la gauche

import sys


def ma_rotation(array):
    result =[]
    for i in range(1,len(array)):
        result.append(array[i])
    result.append(array[0])   
    return result


def args_are_valid(arguments):
    if not len(arguments) > 1:
        return False
    return True


def display(chaine):
    if len(chaine) == 1:
        print(chaine[0])
    else:
        for i in range(len(chaine)-1):
            print(chaine[i],end=", ")
        print(chaine[-1])


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        resultat = ma_rotation(arguments)
        display(resultat)
    else:
        error()


if __name__ == "__main__":
    main()