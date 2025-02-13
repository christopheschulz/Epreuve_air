from pprint import pprint
from pathlib import Path
import subprocess

tests = [
['melanger_deux_tableaux_tries',['10', '20', '30', 'fusion', '15', '25', '35'],'10 15 20 25 30 35'
],
['chercher_intru',['1','2','3','4','5','4','3','2','1'],'5'
],
['concat_chaine',['Je', 'teste', 'des', 'trucs', ' '],'Je teste des trucs '
],
['le_roi_des_tris',['6', '5', '4', '3', '2', '1'],'1 2 3 4 5 6'
],
['insertion_dans_un_tableau_trie',['10', '20', '30', '40', '50', '60', '70', '90', '33'],'10 20 30 33 40 50 60 70 90'
],
['split_chaine',['Bonjour les gars'],'Bonjour\nles\ngars'
],
['rotation_vers_la_gauche',['Michel', 'Albert', 'Thérèse', 'Benoit'],'Albert, Thérèse, Benoit, Michel'
],
['afficher_pyramide',['o', '5'],'    o\n   ooo\n  ooooo\n ooooooo\nooooooooo'
],
['pass_sanitaire',['Michel', 'Albert', 'Thérèse', 'Benoit', 't'],'Michel'
],
['split_en_fonction',['Crevette magique dans la mer des étoiles', 'la'],'Crevette magique dans\n mer des étoiles'
],
['afficher_contenu',['/Users/christopheschulz/Harry/Epreuve_air/afficher_contenu/fichier.txt'],'Juste un essai'
],
['sur_chacun_dentre_eux',['1', '2', '3', '4', '5', '+2'],'3 4 5 6 7'
],
['une_seule_à_la_fois',['Hello milady,   bien ou quoi ??'],'Helo milady, bien ou quoi ?'
]
]

p = Path.home() / "Harry" / "Epreuve_air"
success = 0

# for dossier in dossiers:
for i in range(len(tests)):
    fichier = p / tests[i][0] / "exo.py"
    command = tests[i][1]
    # dossier_parent = fichier.parent.name
    args = ["python3", str(fichier),*command]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if result.stdout.strip() == tests[i][2].strip():
        #print(tests[i][0])
        print(f"\033[32mair{str(i).zfill(2)} (1/1) : sucess\033[0m")
        success +=1
    else:
        #print(tests[i][0])
        print(f"\033[31mair{str(i).zfill(2)} (1/1) : failure\033[0m")

print(f"Total success {success}/{len(tests)}")

# Voici quelques codes de couleurs de base :

# 30 : Noir
# 31 : Rouge
# 32 : Vert
# 33 : Jaune
# 34 : Bleu
# 35 : Magenta
# 36 : Cyan
# 37 : Blanc

        


