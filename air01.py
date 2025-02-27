# Split en fonction

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


def args_are_valid(arguments):
 
    if len(arguments) != 2: 
        return False
    return True


def display(chaine):
    for c in chaine:
        print(c)


def error():
    print("error")

def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        display(fonction_split(arguments[0],arguments[1]))
    else:
        error()

if __name__ == "__main__":
    main()