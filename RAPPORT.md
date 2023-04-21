# Introduction

**Étude de l'impact de la mobilité spatiale sur la biodiversité d'un milieu**

Par Lucas le Roc'h Morgère, Ilias Ouriagli

![image](https://user-images.githubusercontent.com/125641635/233152681-69193145-5ad4-497c-8430-d6388c9ffbc9.png)

Dans le cadre de cette ARE DYNAMIC, nous avons été ammenés à étudier les différents enjeux que peuvent engendrer les interactions entre différentes populations dans un écosystème donné ainsi que les impacts de ces interactions sur la biodiversité du dit écosystème. Par exemple, les espèces en mangent d'autres et peuvent migrer d'un endroit à l'autre. Afin de mieux pouvoir observer les conséquences de ces interactions, nous avons décidé d'abstraire ces différentes dynamiques par le modèle du "Spatial rock paper scissors".

### Présentation de notre modèle

![image](https://user-images.githubusercontent.com/125641635/233149337-59fe4ca0-3582-4dbc-b384-f12aff287494.png)

Le principe est simple, nous avons ici trois espèces en compétition, A, B et C. Ces dernières assument le rôle de pierre, feuille et ciseaux, tout comme dans le jeu éponyme dans lequel la pierre l'emporte sur les ciseaux, les ciseaux l'emportent le papier et le papier l'emporte sur la pierre. C'est donc ce principe qui nous sert de socle sur lequel batir notre modèle.
Ce dernier est gouverné par trois paramètres, la prédation, la reproduction et la mobilité. Son fonctionnement est le suivant: des individus des trois espèces concurrentes A, B et C occupent les cases d’une matrice. Ils interagissent avec les cases qui leur sont adjacentes par la prédation, la reproduction ou la mobilité, les trois réactions se produisent de manière aléatoire à des probabilités σ, μ et ε, respectivement. 

La prédation représente la dominance d'une espèce sur l'autre et représente l'application du pierre feuille ciseau, de fait: 

-A peut tuer B, donnant un site vide. 

-B peut tuer C

-C à son tour peut tuer A

La reproduction d'un individu consiste à transormer une case adjacente vide en une case de la couleur de l'individu. 

La mobilité, aussi appelée permutation, consiste à l'échange de position avec un individu adjacent, ce dernier pouvant être une case vide.

A chaque tour de boucle, chaque indidivu est considéré et peut effectuer une ou plusieurs des actions décrites plus haut, en fonction des probabilités définies.

En cliquant sur les liens suivants, on peut voir trois vidéos de notre modèle en action. Les espèces sont représentées par des couleurs différentes. En fonction de nos trois paramètres σ, μ et ε (correspondant à la probabilité de prédation, de reproduction et de mobilité respectivement), le comportement de l'algorithme est différent.

https://imgur.com/a/5CajVVb

https://imgur.com/a/LIDKk96

https://imgur.com/a/o27XBHy

Dans la troisième vidéo, on constate qu'une couleur l'emporte sur les autres. 

On peut également exécuter notre code posté sur le github pour tester notre modèle et faire varier les paramètres. 


### Problématique

Nous avons ici pour but d'étudier l'impact qu'a la migration spatiale des individus (correspondant au paramètre mobilité de notre modèle) sur la biodiversité. En effet, la mobilité fait concurrence aux interactions locales que sont la reproduction et la prédation. Nous avons émis comme hypothèse que pour des valeurs de mobilité faibles, les interactions habituelles entre les individus voisins sont maintenues, ce qui entraine le maintien à long terme de la diversité des espèces. En revanche, lorsque la mobilité des espèces est élevée, la biodiversité est perdue, c'est à dire que l'on arrive à une situation où des espèces disparaissent et une seule survit. Nous tacherons donc par le biais de tests effectués sur notre modèle, de valider cette hypothèse au long de notre travail.

### Résultats

Afin de pouvoir répondre à la question énoncée précedemenent, nous avons décidé de créer une fonction ayant pour but d'effectuer plusieurs tests sur notre modèle en variant le paramètre ε. Pour chaque valeur de ε, nous lançons notre algorithme 100 fois sur une matrice de taille 40*40 avec des valeurs de σ et μ fixées à 0.3 et sur chacun des 100 cas, on itère jusqu'à ce que l'on parvienne à une situation d'extinction ou jusqu'à ce que 5000 tours aient été effectués. Nous recensons le nombre de tours nécessaires à la satisfaction de nos conditions d'arrêt puis nous en faisons la moyenne sur les 100 exécutions de l'algorithme. Nous obtenons les résultats suivant:

*nombre de tours moyen nécessaires à l'extinction d'une espèce selon le paramètre ε*

<img width="219" alt="Courbe nb tours en fct de permutation" src="https://user-images.githubusercontent.com/125641635/233406310-ef4bc624-6507-4dbe-93fa-bcc9bef3f38b.PNG">

Nous pouvons constater sur cette courbe une relation décroissante entre le paramètre de mobilité et le nombre moyen de tours nécessaire à l'extinction d'une espèce. En effet, plus la probabilité de mobilité est élevée, moins le nombre moyen de tours nécessaire pour arriver à un scénario dans lequel seule une espèce survit est élevé. A noter que dès lors qu'une espèce arrive à extinction, cela signifie forcément qu'une autre espèce va s'éteindre et qu'une seule survivra (en effet, de par la nature même de notre modèle, sur les deux espèces restantes l'une domine l'autre). 

*proportion des itérations étant parvenues à l'extinction d'une espèce selon le paramètre ε*

<img width="202" alt="courbe2 ARE" src="https://user-images.githubusercontent.com/125641635/233484278-fa590816-74d1-4fa5-8b39-e7f6d71ec0ba.PNG">

Cette courbe-ci nous permet d'établir un seuil de mobilité critique, c'est a dire, un seuil de mobilité au dessus duquel il y aura toujours l'extinction de deux espèces au bout d'un certain temps. En effet, nous pouvons constater qu'au delà d'un ε d'environ 0.2, notre modèle arrive toujours à un état où une seule espèce survit.

### Conclusions

Du fait des résultats des tests que nous avons effectué plus haut, on voit bien qu'une trop grande mobilité dans un milieu entraine de grands risques de perte de biodiversité, en venant perturber les intercations cycliques localement en place entre les espèces de l'écosystème. On peut penser aux espèces invasives qui mettent en danger les écosystèmes, comme les frelons asiatiques qui provoquent une baisse de la population d'abeilles et de frelons européens en France. 

### Analyse critique et ouverture

La limite de notre travail est que notre modèle ne reste qu'une simplification de la réalité et ne prend pas en compte de nombreux autres paramètres qui influent sur la biodiversité dans un milieu.

On pourrait également vouloir, en restant avec notre modèle, s'intéresser aux paramètres prédation et reproduction plus en détail et étudier également l'impact de leur variation sur la convergence de l'algorithme vers une situation d'extinction de deux espèces.

