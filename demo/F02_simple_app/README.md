Application Flask de démonstration
===

This small repo demonstrates a proper file structure for a Flask app. The folders named *static* and *templates* are required.

**Routes** and **static files** are handled correctly in all `src` and `href` attributes in the template files.

The template file `base.html` is used as a shell by the other three HTML templates. This means they insert content into `base.html` according to Jinja2 template rules.

## Installation des dépendances
Installation des packages nécessaires à l'application
```sh
conda install --file requirements.txt
```

NB: Si des packages non pris en charge par `conda` doivent être installés via `pip` un fichier `requirements_pip.txt` devra être créé (`pip install -r requirements_pip.txt`)

## Lancement de l'application
Pour lancer localement ce rapport, exécuter depuis ce dossier : 

```sh
python app.py
```
