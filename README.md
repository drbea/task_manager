## Gestionnaire basic de tache
- cette application permet de voire, creer, supprimer des taches

## Utilisation
- 1 commencer par creer un environement virtuelle si vous vouller
```bash
  python -m venv virtenv
```
    virtenv est le nom de l'environement virtuelle (vous pouver le changer)

- 2 activer l'environement virtuelle
      sous linux
  ```bash
  python virtenv/bin/activate
  ```
        sous windows
  ```bash
  python virtenv/Scripts/activate
  ```
- 3 clonner le depot
```bash
git clone https://github.com/drbea/task_manager.git
```
puis deplacer vous dans le dossier du projet
```bash
    cd task_manager
```
- 4 installer les dependances:
    Note: je n'ai pas encore ajouter les dependances dans un fichier donc
  dans votre termial
  ```bash
  pip install django pillow
```
- 5 lancer le serveur local
```bash
    python manage.py runserver
```

- ouvrir votre navigateur et mettre ceci dans la barre de recherche:   http://localhost:8000/
  
