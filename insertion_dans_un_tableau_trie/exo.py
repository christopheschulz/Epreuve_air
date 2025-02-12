import sys

def sorted_insert(array,new_element):
    result = []
    new_element = int(new_element)
    for i in range(0,len(array)-1):
        if int(array[i]) < new_element < int(array[i+1]):
            result.append(int(array[i]))
            result.append(new_element)
        else:
            result.append(int(array[i]))
    result.append(int(array[-1]))
                  
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