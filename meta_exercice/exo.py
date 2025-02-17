from pprint import pprint
from pathlib import Path
import subprocess

tests_dict = [
    {"dossier": 'melanger_deux_tableaux_tries',
     "test": [['10', '20', '30', 'fusion', '15', '25', '35']],
     "result": ['10 15 20 25 30 35']
    },
    {"dossier": 'chercher_intru',
     "test": [['1', '2', '3', '4', '5', '4', '3', '2', '1']],
     "result": ['5']
    },
    {"dossier": 'concat_chaine',
     "test": [['Je', 'teste', 'des', 'trucs', ' ']],
     "result": ['Je teste des trucs ']
    },
    {"dossier": 'le_roi_des_tris',
     "test": [['6', '5', '4', '3', '2', '1']],
     "result": ['1 2 3 4 5 6']
    },
    {"dossier": 'insertion_dans_un_tableau_trie',
     "test": [['10', '20', '30', '40', '50', '60', '70', '90', '33']],
     "result": ['10 20 30 33 40 50 60 70 90']
    },
    {"dossier": 'split_chaine',
     "test": [['Bonjour les gars']],
     "result": ['Bonjour\nles\ngars']
    },
    {"dossier": 'rotation_vers_la_gauche',
     "test": [['Michel', 'Albert', 'Thérèse', 'Benoit']],
     "result": ['Albert, Thérèse, Benoit, Michel']
    },
    {"dossier": 'afficher_pyramide',
     "test": [['o', '5']],
     "result": ['    o\n   ooo\n  ooooo\n ooooooo\nooooooooo']
    },
    {"dossier": 'pass_sanitaire',
     "test": [['Michel', 'Albert', 'Thérèse', 'Benoit', 't'],
              ['Michel', 'Albert', 'Thérèse', 'Benoit', 'a']],
     "result": ['Michel',
                'Michel, Thérèse, Benoit']
    },
    {"dossier": 'split_en_fonction',
     "test": [['Crevette magique dans la mer des étoiles', 'la']],
     "result": ['Crevette magique dans\n mer des étoiles']
    },
    {"dossier": 'afficher_contenu',
     "test": [['/Users/christopheschulz/Harry/Epreuve_air/afficher_contenu/fichier.txt']],
     "result": ['Juste un essai']
    },
    {"dossier": 'sur_chacun_dentre_eux',
     "test": [['1', '2', '3', '4', '5', '+2']],
     "result": ['3 4 5 6 7']
    },
    {"dossier": 'une_seule_à_la_fois',
     "test": [['Hello milady,   bien ou quoi ??']],
     "result": ['Helo milady, bien ou quoi ?']
    }
]

p = Path.home() / "Harry" / "Epreuve_air"
success = 0
test = 0
# for dossier in dossiers:
for i in range(len(tests_dict)):
    for j in range(len(tests_dict[i]["test"])):
        fichier = p / tests_dict[i]["dossier"] / "exo.py"
        command = tests_dict[i]["test"][j]
        # dossier_parent = fichier.parent.name
        args = ["python3", str(fichier),*command]
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.stdout.strip() == tests_dict[i]["result"][j].strip():
            max_test = len(tests_dict[i]["test"])
            print(f"\033[32mair{str(i).zfill(2)} ({j+1}/{max_test}) : sucess\033[0m")
            success +=1
        else:
            #print(tests[i][0])
            print(f"\033[31mair{str(i).zfill(2)} ({j+1}/{max_test}) : failure\033[0m")
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

        


