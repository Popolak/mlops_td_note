### Justification des choix
1. Utiliser docker compose permet de lancer tout les containers en une seule commande. Je n'implémente pas les Domain Unix Socket car nginx les remplace en étant plus intuitif.
2. J'ai choisi d'implémenter kibana et elasticsearch pour la base. Je suis conscient que la base elasticsearch est orienté documents, mais le td de big data durant lequel nous devions travailler dessus s'est soldé par des erreurs en cascades, ce TD noté était une occasion de retravailler avec cette base. Une base de données est nécessaire pour enrichir les capacités de nos services.
3. Pas de github actions pour ma part. Le scope du projet étant uniquement local, celà ne me parait pas nécessaire d'automatiser des déploiements. A la limite on peut imaginer des actions pour automatiser des tests néanmoins.
4. L'utilisation de nginx n'est pas nécessaire, d'autant plus avec les domain unix sockets. Mais la praticité apportée par nginx m'a poussé à l'utiliser.
5. De la même manière que la CI/CD avec github actions, minikube ne me semble pas adapté à ce projet. Minikube permet d'utiliser éssentiellement kubernetes en local, en s'abrogeant le besoin d'une machine virtuelle en ligne. 


# Vers du DevOps (Code Engineering)

**Attention : ces TD font office de contrôle continu pour le module MLOps. Une note individuelle sera attribuée.**

## Partie I : 

### Contexte Général

Les deux séances de TD seront consacrées au déploiement (ingénierie logicielle). L'objectif est d'aborder des notions essentielles à travers un projet pratique. Ces notions seront intégrées dans l'ordre suivant :

1. Gérer la communication entre des microservices (API) avec Docker Compose, via des Domain Unix Sockets.
2. Ajouter une base de données dans l'écosystème.
3. Introduire les GitHub Actions (.github/workflows/ci_cd.yml).
4. L'utilisation de Nginx est-elle nécessaire ?
5. Migrer de Docker Compose vers Kubernetes (Minikube) ?

### Lien vers la base commune

Une base commune vous a été fournie sous le lien suivant : [https://github.com/AghilasSini/build_api_ml.git](https://github.com/AghilasSini/build_api_ml.git). Vous devrez décider si vous souhaitez intégrer ou non les éléments mentionnés dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Instructions Générales : 

Une base commune vous a été fournie. À vous de décider si vous souhaitez intégrer ou non les éléments évoqués dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Partie II – Un portail web adapté 

Il s'agit de concevoir une solution prenant en compte les éléments mentionnés ci-dessus et répondant au cahier des charges illustré par la figure ci-dessous (analogie avec Umtice).

![Projet](./un_portail_pour_les_gouverner_tous.png)
---

## Partie III – Un portail web pour tous les gouvernés (conception et architecture de système pour du ML)

Il s'agit de concevoir une plateforme d'annotation automatique de données brutes. Cette plateforme devra héberger des outils de traitement automatique des langues.

---

