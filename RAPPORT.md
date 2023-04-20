# Introduction

**Étude de l'impact de la mobilité spatiale sur la biodiversité d'un milieu**

**Study regarding the impact of spatial mobility on an environement's biodiversity**

Par/by Lucas le Roc'h Morgère, Ilias Ouriagli

![image](https://user-images.githubusercontent.com/125641635/233152681-69193145-5ad4-497c-8430-d6388c9ffbc9.png)

Dans le cadre de cette ARE DYNAMIC, nous fûmes ammenés à étudier les différents enjeux que pouvaient engendrer les interactions entre différentes populations dans un écosystème donné ainsi que leur impact sur la biodiversité du dit écosystème. Cette dernière est régie par les interactions cycliques et non hiérarchiques entre les différentes populations concurrentes. Afin de mieux pouvoir observer les conséquences de ces intéractions, nous avons décidé d'abstraire ces différentes dynamiques par le modèle du "Spatial rock paper scissors".

### Présentation de notre modèle

![image](https://user-images.githubusercontent.com/125641635/233149337-59fe4ca0-3582-4dbc-b384-f12aff287494.png)

Le principe est simple, nous avons ici trois espèces en compétition, A, B et C. Ces dernières assument le rôle de pierre, feuille et ciseaux, tout comme dans le jeu éponyme dans lequel la pierre écrase les ciseaux, les ciseaux coupent le papier et le papier enveloppe la pierre. C'est donc ce principe qui nous sert de socle sur lequel batir notre modèle.
Ce dernier est gouverné par trois paramètres, la prédation, la reproduction et la mobilité. Son fonctionnement est le suivant: des individus des trois espèces concurrentes A, B et C occupent les cases d’une matrice. Ils interagissent avec les cases qui leur sont adjacentes par la prédation ou la reproduction, les deux réactions se produisent de manière aléatoire à des probabilités σ et μ, respectivement. La prédation représente la dominance d'une espèce sur l'autre et représente l'application du pierre feuille ciseau, de fait: 

-A peut tuer B, donnant un site vide. 

-B peut tuer C

-C à son tour peut tuer A

La reproduction des individus n’est autorisée que sur les sites adjacents vides. La mobilité, régie par une probabilité ε, consiste au changement de position avec un individu adjacent, ce dernier pouvant être une case vide.

Les actions décries ci-dessus sont vérifiées pour la globalité des individus composant notre matrice à chaque tour de boucle pour un nombre total défini par l'utilisateur. 

### Problématique

Nous avons ici pour but d'étudier l'impact qu'a la migration spatiale des individus (corrèspondant au paramètre mobilité de notre modèle) sur que la biodiversité car il s'agit d'une caractéristique omniprésente des écosystèmes réels. En effet, la mobilité fait concurrence aux interactions locales comme la reproduction et la sélection qui favorisent la préservation des espèces et la biodiversité. Nous avons donc émis comme hypothèse que pour des valeurs de mobilité faibles, le développement temporel sera dominé par les interactions entre les individus voisins, ce qui entraînera le maintien à long terme de la diversité des espèces. En revanche, lorsque la mobilité des espèces sera élevée, l’homogénéité spatiale et la biodiversité seront perdues. Nous tacherons donc le biais de tests effectués sur ordinateur par notre modèle, de valider cette hypothèse au long de notre travail. De manière plus précise, nous aimerions pouvoir relever des changements concernant l'extinction ou la dominance d'une espèce en fonction de notre paramètre ε. 

### Tests

Afin de pouvoir répondre à la question énoncée précedemenent, nous avons décidé de créer une fonction ayant pour but d'éffectuer plusieurs test sur notre modèle en variant le paramètre ε. Une fois ce paramètre choisi, nous effectuons 100 itérations de notre algorythme sur une matrice de taille 40*40 jusqu'à ce qu'on parvienne à une situation d'extinction ou jusqu'à ce que 5000 tours ai été effectués. Nous recenssons le nombre de tour nécessaires à la satisfaction de nos conditions d'arrêt puis nous en faisons la moyenne. Nous obtenons les résultats suivant:

*nombre de tours moyen nécessaires à l'extinction d'une espèce selon le paramètre ε*

<img width="219" alt="Courbe nb tours en fct de permutation" src="https://user-images.githubusercontent.com/125641635/233406310-ef4bc624-6507-4dbe-93fa-bcc9bef3f38b.PNG">

Nous pouvons constater sur cette courbe une relation décroissante entre le paramètre de mobilité et l'extinction d'une espèce. En effet, plus la probabilité de mobilité est élevée, moins le nombre moyens de tours nécessaire à un scénario dans lequel une espèce domine est faible.

*proportion des itérations étant parvenues à l'extinction d'une espèce selon le paramètre ε*

<img width="202" alt="courbe2 ARE" src="https://user-images.githubusercontent.com/125641635/233484278-fa590816-74d1-4fa5-8b39-e7f6d71ec0ba.PNG">

Cette courbe ci nous permet d'établir un seuil de mobilité critique, c'est a dir, un seuil de mobilité au dessus duquel il y aura toujours dominance d'une espèce. En effet, nous pouvons constater qu'au delà d'un ε d'environ 0.18, notre modèle arrive toujours à un état où une seule espèce dommine.
Cette courbe ci
