# Modificateur de Texte

Ce programme est une application graphique en Python utilisant la bibliothèque `Tkinter` qui permet de modifier le contenu d'un fichier texte. Il remplace un élément spécifié dans le fichier par un autre. L'utilisateur peut choisir un fichier à modifier et indiquer quel texte remplacer, ainsi que par quel texte.

## Fonctionnalités

- Choisir un fichier texte à modifier.
- Spécifier un texte à remplacer et le texte de remplacement.
- Sauvegarder le fichier modifié sous un nouveau nom.
- Interface simple et intuitive via une fenêtre Tkinter.

## Comment ça marche ?

1. Le programme demande à l'utilisateur de choisir un fichier texte existant (`fichier_originale`).
2. Ensuite, il demande où sauvegarder le fichier modifié (`fichier_modifier`).
3. L'utilisateur entre l'élément à remplacer (`ancien`) et l'élément par lequel il veut le remplacer (`nouveau`).
4. Une fois que l'utilisateur clique sur le bouton "Modifier", le programme ouvre le fichier original, remplace toutes les occurrences du texte et sauvegarde le fichier modifié.
5. Un message de confirmation est affiché une fois l'opération terminée.

## Prérequis

- Python 3.x
- Bibliothèque `tkinter` (préinstallée avec Python)

## Installation

1. Clonez ce dépôt sur votre machine :
   ```bash
        git clone https://github.com/tonutilisateur/tonprojet.git
   ```

2. Accédez au dossier du projet :
    cd tonprojet

3. Exécutez le programme :
    python Modificateur.py

## Utilisation

1. Lancez le programme avec la commande python Modificateur.py.
2. Sélectionnez un fichier texte à modifier.
3. Entrez le texte à remplacer et le texte de remplacement.
4. Cliquez sur "Modifier" pour effectuer les modifications.
5. Le fichier modifié sera sauvegardé à l'endroit que vous avez spécifié.


### Exemple 

Si vous avez un fichier texte contenant :
```
    Hello World
    This is a test.
```

Et que vous remplacez "World" par "Universe", votre fichier modifié sera :
```
    Hello Universe
    This is a test.
```

## Contribuer 

1. Fork ce projet.
2. Créez une branche pour votre fonctionnalité : 
```bash
git checkout -b feature-nouvelle-fonctionnalité
```
3. Commitez vos modifications :
```bash
git commit -am 'Ajout de ma fonctionnalité'
```
4. Poussez vers votre branche :
```bash
git push origin feature-nouvelle-fonctionnalité
```
5. Créez une Pull Request.

## Auteur

- **AHOUSSI Sainth-Nathan** – *Développeur et Mainteneur*

## License
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.
