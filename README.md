<img width="1680" alt="image" src="https://github.com/HackaTAL/2023/assets/21262253/6bdc9487-bbe7-44ca-b9ab-5a3706fbd0c7">

# Wikipédia & Politique / Détection de citations

## HackaTAL 2023
---------------
*(hackathon du Traitement Automatique des Langues)*  
avec la conférence CORIA TALN RJCRI RECITAL 2023

### Résumé

Tâches : Contributeurs et Politique sur Wikipédia / Détection de citations 
Site web : http://hackatal.github.io/2023  
Dates : 5 et 6 juin 2023  
Lieu : SCAI, 4 place Jussieu, 75005 Paris 
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

Dans ce défi nous proposons d'extraire les discours rapportés par les médias, et en particulier dans des contenus écrits du web. Ce type d'élément est constitué minimalement d'un segment de discours rapporté, souvent associé à sa source d'origine, c'est-à-dire la personne physique ou morale qui a tenu ces propos. Nous nous intéresserons aussi bien au discours direct, délimités par des marqueurs typographiques de type guillemets, qu'au discours indirect. Quant à la source, nous souhaiterions pouvoir retrouver une dénomination interprétable par un utilisateur à qui on présenterait les résultats, typiquement une Entité Nommée ou une expression référentielle.

Une sous-tâche de visualisation est également proposée pour se projeter dans un emploi de ces données.
Aussi les participants pourraient choisir de combiner une partie de l'extraction avec un type de visualisation de la donnée pour proposer un résultat possible.


*Tâches*

- Détection de citations (discours rapportés direct et indirect)
- Détection de source (entité qui a produit initialement le discours)
- Détection du couple (discours, source) comme relation entre les deux détections précédentes
- Représentation des résultats (dataviz), propositions non exhaustives :
  - Similarité entre discours
  - Distribution des discours par genre des sources (féminin/masculin)
  - Textométrie
  - Recouvrement des thématiques du défis "Wikipédia et politiques" avec les discours extraits

*Ressources*

- Corpus de contenus écrits du web annoté et utilisable pour l'entraînement et l'évaluation
- Corpus de données non annotée contenant des discours rapportés


### Prix

Deux prix seront décernés, un pour chaque défi (TBC).

### Planning prévisionnel

**Lundi 5 juin** au SCAI, 4 place Jussieu, 75005 Paris 

- 10h-11h : introduction, présentation du hackathon
- 11h-12h : discussions par groupes
- 12h-13h : pause déjeuner
- 13h-17h : développements par équipes
- 17h-18h : NLP pour les sciences sociales (et vice-versa) (Étienne Ollion, CNRS)
- 18h-20h : cocktail et buffet
- 20h-23h : développements par équipes

**Mardi 6 juin** aux Cordeliers, 15 rue de l'École de Médecine, 75006 Paris

- 15h15-16h15 : restitution des équipes, vote, remise du prix

### Organisation pratique

BYOD (amenez votre ordinateur)  
Pas de critères pour participer, le hackathon est ouvert à tous !  
Aucune préparation requise des participants 

### Plan d'accés à SCAI

<img width="428" alt="image" src="https://github.com/HackaTAL/2023/assets/21262253/ddd6f7a5-70e6-436b-98b3-ea3fc6aa4d8e">


### Organisateurs

- Adelaïde Calais (WikiMedia France)
- Kévin Deturck (ERTIM, Inalco)
- Nicolas Dugué (LIUM, Université du Mans)
- Yoann Dupont (Lattice, Université Sorbonne Nouvelle)
- Xavier Fresquet (SCAI, Sorbonne Université)
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
- Lili Wu (ERTIM, Inalco)
