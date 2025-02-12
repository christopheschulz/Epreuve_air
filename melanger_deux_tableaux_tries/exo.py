import sys

def sorted_fusion(array1,array2):
    result =[]
    print(array1,array2)
    for i in range(len(array2)):
        for j in range(len(array1)-1):
           
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
        print(sorted_fusion(array1,array2))
    
    else:
        erreur()