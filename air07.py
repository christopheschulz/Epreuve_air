import sys

def sorted_insert(array,new_element):
    result = []
    new_element = int(new_element)
    inserted = False  

    for i in range(len(array)):
        if not inserted and int(array[i]) > new_element:
            result.append(new_element)
            inserted = True
        result.append(int(array[i]))

    if not inserted:
        result.append(new_element)

    return result
    

def verification_arguments(arguments):
    ok = False  
    all_arguments_int = all(arg.isdigit() for arg in arguments)
    if all_arguments_int:
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
        resultat = sorted_insert(arguments[:-1],arguments[-1])
        afficher(resultat)
    else:
        erreur()