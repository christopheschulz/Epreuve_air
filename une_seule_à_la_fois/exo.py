import sys

def une_seule_a_la_fois(array):
    print(len(array))
    result = ""
    result += array[0]
    j = 0
    for i in range(1,len(array)):
        if array[i] != result[j]:
            result += array[i]
            j += 1
        
            
    return result

    


def verification_arguments(arguments):
    ok = False  
    if len(arguments) == 1:
        ok = True
    return ok


def afficher(chaine):
   return

def erreur():
    print("error")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if verification_arguments(arguments):
        print(une_seule_a_la_fois(arguments[0]))
    else:
        erreur()