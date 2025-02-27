
import sys

def fonction_split(string_a_couper,separateur):
    result = []
    word = ""
    
    for i in range(len(string_a_couper)):   
        if string_a_couper[i] != separateur:
            word += string_a_couper[i]
        else:
            result.append(word)
            word = ""
    result.append(word)

    return result


def verification_arguments(arguments):
 
    if len(arguments) != 1: 
            return False
    return True


def afficher(chaine):
    for word in chaine:
        print(word)


def erreur():
    print("error")

def main():
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        afficher(fonction_split(arguments[0]," "))
    else:
        erreur()

if __name__ == "__main__":
    main()