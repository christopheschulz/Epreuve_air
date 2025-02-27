# Insertion dans un tableau trié

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
    

def args_are_valid(arguments): 
    all_arguments_int = all(arg.isdigit() for arg in arguments)
    if not all_arguments_int:
        return False
    return True


def display(chaine):
    for c in chaine:
       print(c,end=" ")
    print()


def erreur():
    print("error")

def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        resultat = sorted_insert(arguments[:-1],arguments[-1])
        display(resultat)
    else:
        erreur()

if __name__ == "__main__":
    main()