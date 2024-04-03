# tp2_ci-cd_devops

Création d'une application Flask sur Azure avec CI/CD.

## Création d'un repository github

Dans un premier temps, vous aurez besoin de créer un repository github pour stocker tous les fichiers nécessaires au projet.

## Création d'une application python simple avec tests unitaires

Ensuite, vous aurez besoin d'une application à faire tourner. Pour cela, vous pouvez simplement récupérer les fichiers (`app.py`, `test_app.py` et `requirements.txt`) disponibles dans ce repository et les ajouter dans le votre.

## Création d'un Web App Azure

Dans un premier temps, dans l'onglet `Basics` définissez un nom pour votre Web App et précisez le langage utilisé pour l'application, ici `python 3.12`.
Vous pouvez vous référer à l'image ci-dessous :
![image](https://github.com/Viveledelire/tp2_ci-cd_devops/assets/97473758/83e53c30-fe1b-414f-9ede-6f978b9c8418)

Ensuite, dans l'onglet `Deployment`, activez le `déploiement continu` et liez votre compte github à azure. Vous pourrez ensuite choisir le repository ainsi que la branche que vous souhaitez viser.
Encore une fois, vous pouvez vous référer à l'image ci-dessous :
![image](https://github.com/Viveledelire/tp2_ci-cd_devops/assets/97473758/2d146171-31a6-40f2-a909-8d3e59fe09d5)

Une fois ces étapes passées, vous pouvez cliquer sur le bouton `Review + Create` et finaliser la création de votre Web App.

## Le Workflow et la CI/CD

Après avoir finalisé votre Web App en suivant les indications, un dossier `.github/workflows/` a dû se créer automatiquement. Si ce n'est pas le cas, attendez bien que votre Web App ait terminé de se déployer et recharger votre page github. 
Dans ce dossier devrait se trouver un fichier .yml dont le nom devrait ressembler à ça : `<nom_branche>_<nom_webapp>.yml`.

Ce Workflow contient, par défaut, deux jobs : `build` et `deploy`. Mais vous pouvez en rajouter autant que vous voulez. Vous pouvez, par exemple, récupérer le job `test` ci-dessous et l'ajouter dans votre Workflow.
```
  test:
    runs-on: ubuntu-latest
    needs: build

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python version
        uses: actions/setup-python@v1
        with:
          python-version: '3.12'

      - name: Create and start virtual environment
        run: |
          python -m venv venv
          source venv/bin/activate
          
      - run: pip install -r requirements.txt 
      
      - name: Run tests
        run: python -m pytest -v
```
Attention cependant à bien modifier les `needs` du job `deploy` par la suite pour que la pipeline reste fonctionnelle.
```
  deploy:
    runs-on: ubuntu-latest
    needs: test
```
Vous pouvez ensuite allez dans l'onglet `Actions` de github pour voir vos jobs en "action" sous la forme d'une pipeline.
![image](https://github.com/Viveledelire/tp2_ci-cd_devops/assets/97473758/41177943-5b80-40e4-93e7-f7138965efb9)

### Conseil

Avant de modifier votre Workflow, attendez bien qu'il se soit terminé une première fois pour être sûr que le déploiement fonctionne sans encombre.
