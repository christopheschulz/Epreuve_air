# Concat

import sys

def fonction_concat(array_de_string,separateur):
    result = ""
    for i,ar in enumerate(array_de_string,1):
        if i != len(array_de_string):
            result += ar + separateur
        else :
            result += ar
    return result


def args_are_valid(arguments):
    
    if not len(arguments) > 2:
       return False
    return True


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        print(fonction_concat(arguments[:-1],arguments[-1]))
    else:
        error()


if __name__ == "__main__":
    main()