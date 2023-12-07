
# Alignment free - TP 1

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Vous trouverez les données en suivant [ce lien](https://we.tl/t-ACiDxJko7s)

## Composer le TP

Vous devez forker ce projet puis compléter ses fonctions.
Le rendu sera le dépot git dans lequel vous aurrez forké.

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.
Vous devez compléter le README pour y afficher la matrice des distances des bactéries.
Vous devez également y indiquer le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. Pour cela vous pouvez utiliser la commande ```/usr/bin/time -v```.

## Resultats
### Par Brenda Enriquez et Isabelle Wu

Dans nos séquences, on a trouvé des lettres qui peuvent correspondre à plusieurs nucléotides et on a décidé de ne pas les considérés dans notre algorithme.

Voici donc la matrice de distance de Jaccard qu'on obtient:

## Matrice des distances:
File0 : GCF_008244785.1_ASM824478v1_genomic.fna   [[1.         *0.95545907* 0.01880051 0.01932558 0.00176802]
File1 : GCF_000006945.2_ASM694v2_genomic.fna      [0.95545907 1.         0.01871978 0.01928407 0.00177782]
File2 : GCF_020535205.1_ASM2053520v1_genomic.fna  [0.01880051 0.01871978 1.         *0.65841015* 0.00211935]
File3 : GCF_020526745.1_ASM2052674v1_genomic.fna  [0.01932558 0.01928407 0.65841015 1.         0.00194663]
File4 : GCF_014892695.1_ASM1489269v1_genomic.fna  [0.00176802 0.00177782 0.00211935 0.00194663 1.        ]]

Résultats des distances de Jaccard entre chaque pair de génome et la similarité pour les 2 files :

fileA	fileB	Jaccard	  Sim_A	    Sim_B
0	    1	    0.937756	0.975885	0.978545
0	    2	    0.018013	0.036862	0.036971
0	    3	    0.019326	0.037067	0.038809
0	    4	    0.001768	0.003205	0.003928
1	    2	    0.017910	0.037048	0.037056
1	    3	    0.019092	0.037038	0.038674
1	    4	    0.001759	0.003227	0.003944
2	    3	    0.613899	0.777660	0.811818
2	    4	    0.003901	0.007401	0.009044
3	    4	    0.001947	0.003603	0.004217


## En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

La distance max de Jaccard est: 0.937756 trouvé entre les sequences: GCF_008244785.1_ASM824478v1_genomic.fna et GCF_000006945.2_ASM694v2_genomic.fna
La similarité plus grand pour la seq A est: 0.975885 trouvé entre les sequences: GCF_008244785.1_ASM824478v1_genomic.fna et GCF_000006945.2_ASM694v2_genomic.fna
La similarité plus grand pour la seq B est: 0.978545 trouvé entre les sequences: GCF_008244785.1_ASM824478v1_genomic.fna et GCF_000006945.2_ASM694v2_genomic.fna

La distance maximun de Jaccard est *0.937756*, trouvé entre le génome des files 0 et 1.
La similarité pour le file1 est de 0.975885 et pour le file2 est de 0.978545, donc la similarité du file2 est plus élévée.

On peut également voir une distance de 0.613899 qui n'est pas négligable entre les files 2 et 3.
En ce qui concernent les autres pairs de génomes, ils ont très peu de ressemblance, en effet les distances de Jaccard sont inférieurs à 0.02. Notamment entre les files 0 et 4 où la distance de Jaccard est la plus faible mais on peut remarquer que le génome du file 4 a les distances les plus faibles en général.

## Execution:
--- 44.86461687088013 seconds ---
       44.95 real        44.13 user         0.77 sys
           650739712  maximum resident set size
                   0  average shared memory size
                   0  average unshared data size
                   0  average unshared stack size
              304775  page reclaims
                  12  page faults
                   0  swaps
                   0  block input operations
                   0  block output operations
                   0  messages sent
                   0  messages received
                   0  signals received
                  49  voluntary context switches
                1939  involuntary context switches
        525664221720  instructions retired
        142454336621  cycles elapsed
           423528704  peak memory footprint
