# Projet : Évaluation de la robustesse des LLM avec HarmBench

## Description
[cite_start]Ce projet vise à évaluer la sécurité et l'éthique des modèles de langage (LLM) face à des sollicitations malveillantes[cite: 85]. [cite_start]Nous nous basons sur la méthodologie **HarmBench** pour mesurer la capacité des modèles à résister aux attaques[cite: 90].

## Objectifs
1. [cite_start]Analyser les failles de sécurité des modèles actuels (ouverts et propriétaires)[cite: 100].
2. [cite_start]Comparer les résultats obtenus avec d'autres benchmarks[cite: 98].
3. [cite_start]Proposer une grille d'analyse des réponses (taux de refus, justification, dangerosité)[cite: 101].

## Méthodologie
[cite_start]Nous testons les modèles sur trois axes principaux[cite: 102]:
* [cite_start]**Harmbench_contextual** : Injections de prompt pour tromper le contexte[cite: 103].
* [cite_start]**Harmbench_copyright** : Demandes d'informations protégées par le droit d'auteur[cite: 105].
* [cite_start]**Harmbench_standard** : Comportements dangereux classiques et atteinte à autrui[cite: 106].

## Structure du projet
* `/data` : Contient les datasets de prompts (questions pièges).
* `/src` : Contient les scripts Python d'évaluation.
* `/docs` : Contient le rapport final et les analyses.
