
import sys

def fonction_split(string_a_couper,string_separateur):
    result = []
    phrase = []
    word = ""
    
    for i in range(len(string_a_couper)):   
        if string_a_couper[i] != " ":
            word += string_a_couper[i]
        else:
            if word == string_separateur:
                word = " "
                result.append(" ".join(phrase))
                phrase = []
                continue
            phrase.append(word)
            word = ""
    phrase.append(word)
    result.append(" ".join(phrase))

    return result


def verification_arguments(arguments):
    ok = False
    arguments_is_alpha = all(argument.replace(' ','').isalpha() for argument in arguments)
 
    if len(arguments) == 2 and arguments_is_alpha:
        ok = True
    return ok


def afficher(chaine):
    for c in chaine:
        print(c)


def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        afficher(fonction_split(arguments[0],arguments[1]))
    else:
        erreur()