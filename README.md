![HackaTAL 2023](https://raw.githubusercontent.com/HackaTAL/2023/gh-pages/HackaTAL_2023.png)

# Wikipédia & Politique / Détection de citations

## HackaTAL 2023
---------------
*(hackathon du Traitement Automatique des Langues)*  
avec la conférence CORIA TALN RJCRI RECITAL 2023

### Résumé

Tâches : Contributeurs et Politique sur Wikipédia / Détection de citations 
Site web : http://hackatal.github.io/2023  
Dates : 5 et 6 juin 2023  
Lieu : Paris, SCAI  
Inscription : https://framaforms.org/inscription-au-hackatal-2023-1683007751  
Fil twitter : https://twitter.com/hashtag/HackaTAL  
Slack : (TBC)  

### Le HackaTAL

Dans le cadre de la conférence TALN 2023, nous organisons la 5ème édition du hackathon en traitement automatique des langues, le HackaTAL 2023. L’objectif est de réunir les communautés scientifiques TAL et au delà, autour de défis à relever pour questionner, interroger, modéliser, prototyper, coder, expérimenter, développer, tester, évaluer, échanger, etc. par équipes, dans une ambiance dynamique et sympathique 😉

Les tâches proposées portent cette année sur deux thématiques (détails ci-dessous) :

- Wikipédia & Politique
- Détection de citations

L’événement aura lieu cette année à Paris le 5 juin 2023. Il est très largement ouvert à tous : juniors et séniors, informaticiens, linguistes, politologues, juristes, sociologues, etc. et ne nécessite aucune préparation particulière ni de compétences spécifiques... toute personne intéressée est bienvenue  pour apporter sa contribution aux travaux collaboratifs (par équipes) que nous réaliserons sur ces deux jours !

### Défis proposés

**1. Wikipédia & Politique**

En nous basant sur l’hypothèse que Wikipédia représenterait une base de référence du partage des représentations actuelles dans l’espace politique, nous proposons aux participants de saisir les recouvrements discursifs à l’oeuvre entre le Wikipédia francophone et les communiqués de presse politiques mis en ligne par les partis politiques français. Quelles sont les thématiques avec lesquelles chaque parti s’identifie ? Sur quelle(s) thématique(s) spécifique(s) se positionnent les partis politiques français ? Peut-on retrouver ces mêmes thématiques au sein du Wikipédia francophone, et dans quelle mesure ? 


Une attention particulière pourra être portée à l’évolution de ces thématiques au sein du Wikipédia francophone en suivant les modifications sur les pages pour lesquelles on observera un recouvrement avec les thématiques des partis politiques. Enfin, la question des sources utilisées pour ces pages pourra être approfondie. 


Il ne s’agira pas d’une surveillance des pages Wikipédia de personnalités politiques, qui font souvent l’objet de polémiques et conflits au sein de la communauté wikipédienne, mais d’une veille plus large de toutes les pages du Wikipédia francophone. 

*Tâches*

Trois tâches seront proposées : 

1. Extraire les thématiques de chacun des partis politiques français sélectionnés dans le cadre de ce défi, à partir des communiqués de presse mis en ligne sur les sites respectifs et organisés dans une base de données. Puis chercher un recouvrement de ces thématiques avec des pages du Wikipédia francophone
1. Extraire de ces pages du Wikipédia les modifications qui comportent une “intention politique” 
1. Extraire les sources des pages du Wikipédia identifiées aux étapes précédentes pour les comparer avec les sources qui sont recommandées aux contributeurs par WikiMedia mais aussi les situer dans le cadre de leur ligne éditoriale, tel que proposé dans la Roue des médias 

*Ressources*

Les ressources mises à disposition pour ce défi : 

- Un corpus des communiqués de presse de partis politiques français ( RN, FI et PS par ordre décroissant de nombre de communiqué de presse publiés sur ces 5 dernières années) 
- Un corpus “Dump du Wikipédia francophone” ainsi qu’un “historique” indexé dans PostGreSQL accessible en ligne
- Une mise à disposition d'environnements JupyterLab et Rstudio
- Une interface Shiny pour la participation des non-informaticiens



**2. Détection de Citations**

Dans ce défi nous proposons d'extraire les discours rapportés par les médias, et en particulier dans des contenus écrits du web. Ce type d'élément est constitué minimalement d'un segment de discours rapporté, souvent associé à sa source d'origine, c'est-à-dire la personne physique ou morale qui a tenu ces propos. Nous nous intéresserons ici uniquement aux discours délimités par des marqueurs typographiques de type guillemets, autrement dit le discours direct. Quant à la source, nous souhaiterions pouvoir retrouver une dénomination interprétable par un utilisateur à qui on présenterait les résultats, typiquement une Entité Nommée ou une expression référentielle.

Une sous-tâche de visualisation est également proposée pour se projeter dans un emploi de ces données.
Aussi les participants pourraient choisir de combiner une partie de l'extraction avec un type de visualisation de la donnée pour proposer un résultat possible.


*Tâches*

- détection de citations (discours rapportés direct)
- détection de source (entité qui a produit initialement le discours)
- détection du couple (discours, source) qui décrit un discours rapporté. Cette sous-tâches permet de mettre en relation les deux précédentes.
- Représentation des résultats (dataviz). Cette liste contient des propositions non exhaustives
  - similarité entre discours
  - distribution des discours par genre des sources (féminin/masculin)
  - textométrie
  - recouvrement des thématiques du défis "Wikipédia et politiques" avec les discours extraits

*Ressources*

- un corpus de contenus écrits du web annoté et utilisable pour l'entraînement et l'évaluation
- un corpus de donnée non annotée contenant des discours rapportés


### Prix

Deux prix seront décernés, un pour chaque défi (TBC).

### Planning prévisionnel

**Lundi 5 juin**

- 10h-11h : introduction, présentation du hackathon
- 11h-12h : discussions par groupes
- 12h-14h : pause déjeuner
- 13h-17h : développements par équipes
- 17h-18h : présentations intermédiaires
- 18h-20h : conférence, cocktail, repas
- 20h-00h : développements par équipes

**Mardi 6 juin**

- 15h15-16h15 : restitution des équipes, vote, remise du prix

### Organisation pratique

BYOD (amenez votre ordinateur)  
Pas de critères pour participer, le hackathon est ouvert à tous !  
Aucune préparation requise des participants  
Logiciels et données en ligne : https://github.com/HackaTAL/2023  

### Organisateurs

- Kévin Deturck (ERTIM, Inalco)
- Nicolas Dugué (LIUM, Université du Mans)
- Yoann Dupont (Lattice, Université Sorbonne Nouvelle)
- Sahar Ghannay (LISN, Université Paris Saclay)
- Loïc Grobol (MoDyCo, Université Paris Nanterre)
- Tania Jimenez (LIA, Université d'Avignon)
- Benoît Laurent (Aday)
- Guillaume Lechien (Aday)
- Damien Nouvel (ERTIM, Inalco)
- Benjamin Piwowarski (ISIR, UPMC)
- Éric San Juan (LIA, Université d'Avignon)
- Jeanne Vermeirsche (LBNC, Université d'Avignon)
- Manel Zarrouk (LIPN, Université Sorbonne Paris Nord)
- TBA (WikiMedia)
