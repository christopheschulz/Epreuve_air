import sys

def sorted_fusion(array1,array2):
    result = []
    i, j = 0, 0
    len1, len2 = len(array1), len(array2)
    
    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    # Append remaining elements
    result.extend(array1[i:])
    result.extend(array2[j:])

    return result
    

def create_arrays(array):
    array1 = []
    array2 = []
    i=0
    while array[i] != "fusion":
        array1.append(array[i])
        i += 1
    array2 = array[i+1:]

    return array1,array2


def verification_arguments(arguments):
    ok = False 
    if "fusion" in arguments and arguments[-1] != "fusion":
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
        array1,array2 = create_arrays(arguments)
        resultat = sorted_fusion(array1,array2)
        afficher(resultat)
    
    else:
        erreur()