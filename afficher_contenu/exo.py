import sys
from pathlib import Path


def afficher_contenu_fichier(file):
    with open(file,"r") as f:
        content = f.read()
    return content


def verification_arguments(arguments):
    ok = False
    if len(arguments) == 1:
        ok = True
    return ok


def afficher(chaine):
    print(resultat)


def erreur():
    print("error")


if __name__ == "__main__":
    dossier = Path.cwd()
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        fichier = dossier / arguments[0]
        resultat = afficher_contenu_fichier(fichier)
        afficher(resultat)
    else:
        erreur()