from pprint import pprint
from pathlib import Path
import subprocess

tests_dict = [
    {"fichier": 'air00.py',
     "test": [['Bonjour les gars']],
     "result": ['Bonjour\nles\ngars']
     },
     {"fichier": 'air01.py',
     "test": [['Crevette magique dans la mer des étoiles', 'la']],
     "result": ['Crevette magique dans\n mer des étoiles']
    },
    {"fichier": 'air02.py',
     "test": [['Je', 'teste', 'des', 'trucs', ' ']],
     "result": ['Je teste des trucs ']
    },
    {"fichier": 'air03.py',
     "test": [['1', '2', '3', '4', '5', '4', '3', '2', '1'],
              ["bonjour","monsieur","bonjour"]],
     "result": ['5',
                "monsieur"],
    },
    {"fichier": 'air04.py',
     "test": [['Hello milady,   bien ou quoi ??']],
     "result": ['Helo milady, bien ou quoi ?']
    },
    {"fichier": 'air05.py',
     "test": [['1', '2', '3', '4', '5', '+2'],
              ['10','11','12','20','-5']],
     "result": ['3 4 5 6 7',
                '5 6 7 15']
    },
    {"fichier": 'air06.py',
     "test": [['Michel', 'Albert', 'Thérèse', 'Benoit', 't'],
              ['Michel', 'Albert', 'Thérèse', 'Benoit', 'a']],
     "result": ['Michel',
                'Michel, Thérèse, Benoit']
    },
    {"fichier": 'air07.py',
     "test": [['10', '20', '30', '40', '50', '60', '70', '90', '33']],
     "result": ['10 20 30 33 40 50 60 70 90']
    },
    {"fichier": 'air08.py',
     "test": [['10', '20', '30', 'fusion', '15', '25', '35']],
     "result": ['10 15 20 25 30 35']
    },
    {"fichier": 'air09.py',
     "test": [['Michel', 'Albert', 'Thérèse', 'Benoit']],
     "result": ['Albert, Thérèse, Benoit, Michel']
    },
    {"fichier": 'air10.py',
     "test": [['/Users/christopheschulz/Harry/Epreuve_air/air10.txt']],
     "result": ['Juste un essai']
    },
    {"fichier": 'air11.py',
     "test": [['o', '5']],
     "result": ['    o\n   ooo\n  ooooo\n ooooooo\nooooooooo']
    },
    {"fichier": 'air12.py',
     "test": [['6', '5', '4', '3', '2', '1']],
     "result": ['1 2 3 4 5 6']
    }
]

p = Path.home() / "Harry" / "Epreuve_air"
success = 0
test = 0
len_dict_tests = len(tests_dict)
# for dossier in dossiers:
for i in range(len_dict_tests):
    number_of_tests = len(tests_dict[i]["test"])
    for j in range(number_of_tests):
        fichier = p / tests_dict[i]["fichier"]
        command = tests_dict[i]["test"][j]
        args = ["python3", str(fichier),*command]
        
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        if result.stdout.strip() == tests_dict[i]["result"][j].strip():
            print(f"\033[32m{fichier} ({j+1}/{number_of_tests}) : sucess\033[0m")
            success +=1
        else:
            #print(tests[i][0])
            print(f"\033[31m{fichier} ({j+1}/{number_of_tests}) : failure\033[0m")
        test += 1

print(f"Total success {success}/{test}")

# Voici quelques codes de couleurs de base :

# 30 : Noir
# 31 : Rouge
# 32 : Vert
# 33 : Jaune
# 34 : Bleu
# 35 : Magenta
# 36 : Cyan
# 37 : Blanc

        


