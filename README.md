# Attaques par Canaux Auxiliaires et Contre-mesures sur AES & RSA

## Présentation

Ce projet a été réalisé en 1ere année de master informatique Cryptis dans le cadre de l'UE Analyse & Développement Logiciel et encadré par Mr Nicolas Aragon à l'Université de Limoges.
L'objectif était de travailler en équipe sur un projet de recherche dans le domaine de la sécurité informatique qui allait impliquer recherches bibliographiques et implémentation logicielle. Nous avons choisi d'étudier les attaques par canaux auxiliaires pour leur aspect mathématique poussé, leurs nombreuses applications et leur pertinence dans le contexte actuel de recrudescence d'études sur le sujet. 

## Déroulement
Ce projet s'est donc étendu sur l'année en deux phases : 
- le premier semestre a été consacré aux recherches bibliographiques sur les attaques par canaux auxiliaires : leur historique, leur fondements théoriques, leur fonctionnement en pratique, les implémentations déjà réalisées (papiers de recherche) et les contre-mesures existantes. (voir `Analyse_et_Développement_Logiciel_S1.pdf`)
- le second semestre a été consacré à l'implémentation en Python d'attaques classiques (SPA, DPA, CPA) et d'autres plus élaborées (reverse engineering sur bootloader AES-256), le tout en environnement simulé (traces de consommation électrique pré-enregistrées) en étant guidés par des labs Jupyter dédiés à l'apprentissage des side-channels et de la technologie Chipwhisperer. Mais nous avons aussi écrit nos propres labs d'apprentissage des différents types d'attaques classiques (voir `homemade_labs`). Nous avons également implémenté les grandes lignes d'une attaque SPA sur RSA en conditions réelles via un Chipwhisperer (voir `HomemadeChipwhispererScripts`). Et enfin, nous avons étudié et comparé les différents modèles d'attaques side-channels basées sur de l'IA (section 5 du rapport S2). (voir `Analyse_et_Développement_Logiciel_S2.pdf`)

## Contributeurs
  - Gaetan Bois-Baumann : recherches bibliographiques, implémentation d'attaque SPA sur RSA avec le Chipwhisperer (voir `HomemadeChipwhispererScripts`), étude des attaques basées deep-learning (voir `DLSPA` et `ASCAD`).
  - Anaïs Espicier : recherches bibliographiques, implémentation d'attaques SPA/DPA/CPA sur AES et RSA à l'aide des labs Chipwhisperer (voir `ChipWhispererLabSolutions`), réalisation de labs d'initiation aux attaques par canaux auxiliaires (voir `homemade_labs`).
  - Noah Staple : recherches bibliographiques, reverse engineering sur bootloader AES-256.
