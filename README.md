J'écris ce fichier pour expliquer ma démarche de développement de l'application.

https://notes.teklia.com/s/SxgmcAI_YL#

J'utilise pycharm et Github Copilot. À l'occasion j'utilise MammouthAI pour contre vérifier les réponses de Copilot.
Pycharm me permet de naviguer dans la bdd sqllite, je n'avais jamais eu l'occasion d'utiliser cette petite DB.

Je choisis une app flask car plus simple et rapide qu'un DJango. 

Mon choix sans contraintes aurait NestJS + React.

En // de la lecture de l'énoncé, je l'envoi à mammouth pour qu'il l'analyse

# Part 1: Setup de l'app

J'init mon app flask
Je rajoute un hello world
Je dockerise 

# Part 2: Partie métier

J'utilise PyCharm pour explorer la BDD sqlite
https://doc.teklia.com/arkindex/project/export/

Je n'ai pas bien compris ce que c'était ce 'Photograph'. Est-ce que c'est ce qu'il appelle element ?

# Partie 3 : Page classification

Je crois que je suis à coté sur les classifications 
J'ai 45 element classifié acrobate alors que je devrais en avoir 17 
https://demo.arkindex.org/browse/b3471f6a-1ce8-4702-959f-60bcad44eb93?type=photograph&class_id=bf256a7d-4cbe-4784-b962-95052db85959

Je crois que j'ai. Il peut y avoir plusieurs accrobate par image. 

J'avais à moitié, il fallait rajouter le type photograph idiot

Example d'image url
https://europe.iiif.teklia.com/iiif/2/hikaria%2Fflickr%2F037_69_12206557985_o.jpg

je peux la récupérer avec l'url suivante

https://europe.iiif.teklia.com/iiif/2/hikaria%2Fflickr%2F037_69_12206557985_o.jpg/full/400,/0/default.jpg


J'aurais du commencer par l'autre page j'aurais pu etre sur de ce que je manipule

# Partie 4 : Page search by tag

  >  the list of Photograph tagged with a classification (this is a detail view of a classification), displaying all the images


Il fqut que je récupère la liste de toutes les image qui ont un élement classifié "la valeur de l'input"


# Dépot Github rendu 

https://github.com/geourjoa/random-project

# Install

```bash
git clone https://github.com/geourjoa/random-project
cp .env.whatyouwant.sample .env
# get the db and put it in the app folder (next to config.py)
docker compose up -d
```

# Deploiement accessible

https://random-project.tetras-libre.fr

# Liste de chose qui ne vont pas : 
- Db management catastrophique
   - open db est call à chaque fois et n'est pas fermé
   - database.init() est appelé aussi à chaque fois
- Aucune gestion d'erreur
- Inline CSS à l'arrache 
- 