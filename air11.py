# Afficher une pyramide

import sys


def afficher_pyramide(string,number_of_line):
    number_of_line = int(number_of_line)
    # nommbre max d'espace devant la première ligne
    space_max = number_of_line - 1
    # utilisé pour rajouter 2 à chaque étage
    string_number = 1
    for i in range(number_of_line):
        print(" " * (space_max - i) + string * string_number)
        string_number += 2


def args_are_valid(arguments):
    if len(arguments) != 2:
        return False
    if not arguments[1].isdigit() and len(arguments[1]) != 1:
            return False
    return True


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        string = arguments[0]
        line = arguments[1]
        afficher_pyramide(string,line)
    else:
        error()


if __name__ == "__main__":
    main()