## Démarrage rapide

> DÉZIPPEZ les sources ou clonez le dépôt privé. Une fois le code obtenu, ouvrez un terminal et naviguez vers le répertoire de travail contenant le code source du produit.

```bash
$ # Récupérer le code
$ git clone https://github.com/itsmyjob12/PrjParcAuto1.git
$ cd argon-dashboard-django
$
$ # Installation des modules Virtualenv (systèmes Unix)
$ virtualenv env
$ source env/bin/activate
$
$ # Installation des modules Virtualenv (systèmes Windows)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Installer les modules - Stockage SQLite
$ pip install -r requirements.txt
$
$ # Créer les tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Démarrer l'application (mode développement)
$ python manage.py runserver # default port 8000
$
$ # Démarrer l'application - port personnalisé
$ # python manage.py runserver 0.0.0.0:<votre_port>
$
$ # Accéder à l'application Web dans le navigateur : http://127.0.0.1:8000/
```

> Remarque : Pour utiliser l'application, veuillez accéder à la page d'inscription et créer un nouvel utilisateur. Une fois authentifié, l'application déverrouillera les pages privées.


## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:

```bash
< RACINE_DU_PROJET >
   |
   |-- core/                       # Implémente la configuration de l'application
   |    |-- settings.py              # Définit les paramètres globaux
   |    |-- wsgi.py                    # Démarre l'application en production
   |    |-- urls.py                    # Définit les URL servies par toutes les applications/nœuds
   |
   |-- apps/
   |    |
   |    |-- home/                       # Une application simple qui sert des fichiers HTML
   |    |    |-- views.py                  # Sert des pages HTML aux utilisateurs authentifiés
   |    |    |-- urls.py                   # Définit des routes très simples  
   |    |
   |    |-- authentication/           # Gère les routes d'authentification (connexion et inscription)
   |    |    |-- urls.py                   # Définit les routes d'authentification  
   |    |    |-- views.py                  # Gère la connexion et l'inscription  
   |    |    |-- forms.py                  # Définit les formulaires d'authentification (connexion et inscription) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # Fichiers CSS, fichiers JavaScript
   |    |
   |    |-- templates/                     # Modèles utilisés pour le rendu des pages
   |         |-- includes/                 # Morceaux et composants HTML
   |         |    |-- navigation.html      # Composant du menu supérieur
   |         |    |-- sidebar.html         # Composant de la barre latérale
   |         |    |-- footer.html          # Pied de page de l'application
   |         |    |-- scripts.html         # Scripts communs à toutes les pages
   |         |
   |         |-- layouts/                   # Pages maîtresses
   |         |    |-- base-fullscreen.html  # Utilisé par les pages d'authentification (Used by Authentication pages)
   |         |    |-- base.html             # Utilisé par les pages courantes (Used by common pages)
   |         |
   |         |-- accounts/                  # Pages d'authentification (Authentication pages)
   |         |    |-- login.html            # Page de connexion (Login page)
   |         |    |-- register.html         # Page d'inscription (Register page)
   |         |
   |         |-- home/                      # Pages du kit d'interface utilisateur (UI Kit Pages)
   |              |-- index.html            # Page d'accueil (Index page)
   |              |-- 404-page.html         # Page 404 (404 page)
   |              |-- *.html                # Toutes les autres pages (All other pages)
   |
   |-- requirements.txt                     # Modules de développement - Stockage SQLite (Development modules - SQLite storage)
   |
   |-- .env                                 # Injecter la configuration via l'environnement (Inject Configuration via Environment)
   |-- manage.py                            # Démarrer l'application - Script de démarrage par défaut de Django (Start the app - Django default start script)
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Recompile CSS

To recompile SCSS files, follow this setup:

<br />

**Step #1** - Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally 
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional) 

<br />

**Step #2** - Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

<br />

**Step #3** - Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

**Step #4** - Edit & Recompile SCSS files 

```bash
$ gulp scss
```

The generated file is saved in `static/assets/css` directory.

<br /> 

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/creativetimofficial/argon-dashboard-django.git
$ cd argon-dashboard-django
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

<br />

