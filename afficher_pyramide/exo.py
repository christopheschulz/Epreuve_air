import sys


def afficher_pyramide(string,number_of_line):
    number_of_line = int(number_of_line)
    string_number = 1
    for i in range(number_of_line):
        print(" "* (number_of_line - 1 - i) + string * string_number)
        string_number += 2


def verification_arguments(arguments):
    ok = False
    if len(arguments) == 2:
        if arguments[1].isdigit():
            ok = True
    return ok


def afficher(chaine):
   pass


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        string = arguments[0]
        line = arguments[1]
        afficher_pyramide(string,line)
        
    else:
        erreur()