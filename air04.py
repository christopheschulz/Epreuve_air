# Un seul à la fois

import sys

def une_seule_a_la_fois(array):
    result = ""
    result += array[0]
    j = 0
    for i in range(1,len(array)):
        if array[i] != result[j]:
            result += array[i]
            j += 1
                
    return result


def args_are_valid(arguments): 
    if len(arguments) != 1:
        return False
    return True


def error():
    print("error")


def main():
    arguments = sys.argv[1:]
    if args_are_valid(arguments):
        print(une_seule_a_la_fois(arguments[0]))
    else:
        error()


if __name__ == "__main__":
    main()