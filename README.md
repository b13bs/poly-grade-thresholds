poly-seuils-notes
=================

Analyse du fichier des résultats d'un cours à l'École Polytechnique de Montréal pour déterminer les seuils de chaque note.

Exécution
---------
Lancement du script:
	$ python main.py foo1001.txt

Voici un exemple de sortie:
```
32 notes analysees
A* (4): [19.29 , 19.99]
A (4): [16.81 , 18.64]
B+ (4): [14.29 , 15.80]
B (4): [13.77 , 14.25]
C+ (4): [13.34 , 13.59]
C (3): [12.79 , 13.07]
D+ (3): [11.65 , 12.19]
D (3): [10.72 , 11.38]
F (3): [1.29 , 6.33]
```


Dependances
-----------

  * [PyPDF2](http://mstamy2.github.io/PyPDF2/)


TODO
----

  * Ajout de [argparse](https://code.google.com/p/argparse/)