from pprint import pprint
from pathlib import Path
import subprocess

tests = [
['melanger_deux_tableaux_tries',['10', '20', '30', 'fusion', '15', '25', '35'],['10 15 20 25 30 35']
],
['/Users/christopheschulz/Harry/Epreuve_air/chercher_intru',['1','2','3','4','5','4','3','2','1'],['5']
],
['/Users/christopheschulz/Harry/Epreuve_air/concat_chaine',['je', 'teste', 'des', 'trucs', ' '],['Je teste des trucs']
],
['/Users/christopheschulz/Harry/Epreuve_air/le_roi_des_tris',['6', '5', '4', '3', '2', '1'],['1 2 3 4 5 6']
],
['/Users/christopheschulz/Harry/Epreuve_air/insertion_dans_un_tableau_trie',['10', '20', '30', '40', '50', '60', '70', '90', '33'],['10 20 30 33 40 50 60 70 90']
],
['/Users/christopheschulz/Harry/Epreuve_air/split_chaine',['Bonjour les gars'],['Bonjour', 'les', 'gars']
],
['/Users/christopheschulz/Harry/Epreuve_air/rotation_vers_la_gauche',['Michel', 'Albert', 'Thérèse', 'Benoit'],['Albert, Thérèse, Benoit, Michel']
],
# ['/Users/christopheschulz/Harry/Epreuve_air/afficher_pyramide'],
['/Users/christopheschulz/Harry/Epreuve_air/pass_sanitaire',['Michel', 'Albert', 'Thérèse', 'Benoit', 't'],['Michel']
],
['/Users/christopheschulz/Harry/Epreuve_air/split_en_fonction',['Crevette magique dans la mer des étoiles', 'la'],['Crevette magique dans',' mer des étoiles']
],
['/Users/christopheschulz/Harry/Epreuve_air/afficher_contenu',['/Users/christopheschulz/Harry/Epreuve_air/afficher_contenu/fichier.txt'],['Juste un essai']
],
['/Users/christopheschulz/Harry/Epreuve_air/sur_chacun_dentre_eux',['1', '2', '3', '4', '5', '+2'],['3 4 5 6 7']
],
['/Users/christopheschulz/Harry/Epreuve_air/une_seule_à_la_fois',['Hello milady,   bien ou quoi ??'],['Helo milady, bien ou quoi ?']
]
]

p = Path.home() / "Harry" / "Epreuve_air"

# for dossier in dossiers:
for i in range(len(tests)):
    print(i)
    fichier = p / tests[i][0] / "exo.py"
    command = tests[i][1]
    args = ["python3", str(fichier),*command]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(f">> {result.stdout}")


        


