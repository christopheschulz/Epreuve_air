# Afficher le contenu

import sys
from pathlib import Path


def afficher_contenu_fichier(file):
    with open(file,"r") as f:
        content = f.read()
    return content


def args_are_valid(arguments):
    if len(arguments) != 1:
        return False
    return True


def display(resultat):
    print(resultat)


def error():
    print("error")


def main():
    dossier = Path.cwd()
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        fichier = dossier / arguments[0]
        resultat = afficher_contenu_fichier(fichier)
        display(resultat)
    else:
        error()


if __name__ == "__main__":
    main()