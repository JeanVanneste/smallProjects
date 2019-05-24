# Extracteur de marbre
Ce script permet de convertir en csv le marbre de super ciné battle.

## Mode d'emploi
Installer la bibliothèque BeautifulSoup

`pip install beautifulsoup4`

Lancer le script main.py avec python3  
Choisir la décennie à convertir (*60*, *70*, *80*, *90* ou *2000*) ou *all* pour récupérer tout d'un coup  
Attention à bien écrire la bonne valeur sinon le script ne fonctionne pas.

## Comment ça marche

Le html de la page correspondante à la décennie est téléchargée à l'aide de urllib.
Ensuite les informations pertinente sont extraite du tableau via la library BeautifulSoup.
Ces données sont ensuite écrite dans un fichier csv dont le titre est fixé par la décennie choisie
