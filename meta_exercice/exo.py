from pprint import pprint
from pathlib import Path
import subprocess

tests = [
['melanger_deux_tableaux_tries',['10', '20', '30', 'fusion', '15', '25', '35'],['10','15','20','25','30','35']
],
['/Users/christopheschulz/Harry/Epreuve_air/chercher_intru',['1','2','3','4','5','4','3','2','1'],['5']
],
['/Users/christopheschulz/Harry/Epreuve_air/concat_chaine',['je', 'teste', 'des', 'trucs', ' '],['Je teste des trucs']
],
['/Users/christopheschulz/Harry/Epreuve_air/le_roi_des_tris'],['6', '5', '4', '3', '2', '1'],['1', '2', '3', '4', '5', '6'],
['/Users/christopheschulz/Harry/Epreuve_air/insertion_dans_un_tableau_trie']['10', '20', '30', '40', '50', '60', '70', '90', '33'],['10', '20', '30', '33', '40', '50', '60', '70', '90']
['/Users/christopheschulz/Harry/Epreuve_air/split_chaine'],
['/Users/christopheschulz/Harry/Epreuve_air/rotation_vers_la_gauche'],
['/Users/christopheschulz/Harry/Epreuve_air/afficher_pyramide'],
['/Users/christopheschulz/Harry/Epreuve_air/pass_sanitaire'],
['/Users/christopheschulz/Harry/Epreuve_air/split_en_fonction'],
['/Users/christopheschulz/Harry/Epreuve_air/afficher_contenu'],
['/Users/christopheschulz/Harry/Epreuve_air/sur_chacun_dentre_eux'],
['/Users/christopheschulz/Harry/Epreuve_air/une_seule_à_la_fois'],
]

p = Path.home() / "Harry" / "Epreuve_air"

# for dossier in dossiers:

fichier = p / tests[0][0] / "exo.py"
print(fichier)
command = tests[0][1]
args = ["python3", str(fichier),*command]
print(args)
subprocess.run(args)


        


