# carRental
Application pour la gestion de la location de voitures.

(Veuillez lancer la page login.py en premier)

__Problématique:__
 La plupart des gens rencontrent une difficulté à avoir une voiture, cette dernière est une chose très importante dans notre vie quotidienne. ils sont obligés de la demandée à leurs mais qui ne sont pas toujours disponibles.

__Solution proposée:__
 Pour répondre aux besoins fonctionnels et techniques, et pour la résolution des problèmes cités, on propose de réaliser une application prendra en charge la gestion de la location de voitures.

__Outils et techniques de modélisation:__
  - Langage UML : Langage de Modélisation Unifié, en anglais « Unified Modeling Language (UML) » est un langage de modélisation graphique basé sur des pictogrammes, conçu comme une méthode de visualisation standardisée dans le domaine du développement logiciel et de la conception orientée objet.

__Outils et technologie de developpement:__
  - PyQt : PyQt est un module libre qui permet de lier le langage Python avec la bibliothèque Qt. Il permet de créer des interfaces graphiques en Python a l'aide d'une utilitaire graphique de création d'interfaces Qt (Qt Creator) qui permet de générer le code Python d'interfaces graphiques.
Environnement de travail : 
  - PowerAMC : PowerAMC (PowerDesigner) est un logiciel de conception créé par la société SAP, qui permet de modéliser les traitements informatiques et leurs bases de données associées.
  - Qt Creator : Qt Creator est un environnement de développement intégré multiplateforme C++, JavaScript, Python et QML qui simplifie le développement d'applications GUI.
  - SQLite : SQLite est un moteur de base de données écrit en langage de programmation C. Ce n'est pas une application autonome ; il s'agit plutôt d'une bibliothèque que les développeurs de logiciels intègrent dans leurs applications.

__Spécification des besoins:__
  - L'application doit permettre aux utilisateurs de créer un compte avec un nom d'utilisateur et un mot 
de passe.
  - Stocker les informations des utilisateurs dans une table de la base de données.
  - Permettre aux utilisateurs de se connecter avec leur nom d'utilisateur et leur mot de passe.
  - Afficher la liste des voitures disponibles à la location, en présentant les attributs suivants : (Marque, Modèle, Image, Type de carburant, Nombre de places, Transmission (automatique ou manuelle), Prix de location par jour, Disponibilité (disponible ou non disponible)).
  - Stocker les informations des voitures dans une table de la base de données.
  - Permettre aux utilisateurs de rechercher des voitures par (Marque, Type de carburant, Nombre de places, Transmission, Prix de location par jour).

__Conception:__
  - Diagramme de classe :

![Class Diagram](https://user-images.githubusercontent.com/83224625/236510844-e34244c7-83b4-49e3-8f08-0a5cb59e7357.png)

  - Diagramme de cas d'utilisation : 

![Use case](https://user-images.githubusercontent.com/83224625/236511132-003bbcb5-75f7-4c36-a69f-4f260c68ff63.png)

__Realisation:__
  - Page de login : Pour créer un compte, l’utilisateur faut insérer son nom et mot de passe et cliquer sur «SignIn», et pour se connecter il faut cliquer sur «LogIn».

![login](https://user-images.githubusercontent.com/83224625/236511990-be626278-7bd5-47e3-aa44-42c3db8852b6.png)

  - Page principale : Après la création du compte utilisateur, ce dernier peut consulter une liste des voitures et leurs differentes caracteristiques, effectuer une recherche sur les voitures non-reservées a l'aide de l'option 'Search' situer dans la bar Menu.

![main](https://user-images.githubusercontent.com/83224625/236515298-6d2d56e0-75a2-4277-8096-8ea6b4570eb9.png)

  - Page d'ajout : Pour ajouter une voiture, il suffit de remplir les champs et de choisir une photo. La page aussi affiche toutes les voiture avec une option de recherche par Marque.

![add](https://user-images.githubusercontent.com/83224625/236514089-7163e22a-1771-4049-9da7-f89003c769b5.png)

  - Page de mise a jour : Pour MAJ une voiture, il suffit de modifier les champs ou la photo. La page aussi affiche toutes les voiture avec une option de recherche par Marque.

![update](https://user-images.githubusercontent.com/83224625/236515540-2c6e8d49-3432-421b-a27d-c61e95113fdd.png)

  - Page de reservation : Pour consulter les voitures reservées, on clique sur le button 'Voir reservation' dans la page principale. Cette page nous permet de voir les voitures reservée et aussi d'annuler la reservation de la voiture choisie.

![reservation](https://user-images.githubusercontent.com/83224625/236516434-6b7ffd15-47d4-42aa-a1e0-e97253359f8d.png)

__Conclusion:__
  - Ce projet s'est révélé profitable sur plusieurs points : il m’a permis de travailler sur une application en Python avec des interfaces graphiques. Il a été aussi le meilleur endroit pour consolider mes connaissances en développement et me familiariser avec la programmation orienté objet.
