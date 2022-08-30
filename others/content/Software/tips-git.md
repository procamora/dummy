---
Title: Tips Git
Date: 2019-10-8 18:33
Modified: 2019-10-8 18:33
Category: Software
Tags: git, linux, windows, consola, programacion, ramas, reopsitorio
Authors: procamora
Slug: tips-git
Summary: 
Status: published
---





# Pasos iniciales para crear una rama local y remota de desarrollo y de trabajo


Creamos la rama de desarrollo

```bash
# Crear una rama local de desarrollo y movernos a ella
git checkout -b dev

# Crear rama remota de desarrollo
git push origin dev
```

Creamos la rama de trabajo

```bash
# Crear una rama local de desarrollo y movernos a ella
git checkout -b watchdog

# Crear rama remota de desarrollo
git push origin watchdog
```


# Pasos comunes de trabajo



```bash
#!/bin/bash

# Commit repositorio actual
git add .
git commit -m "subida script"
#git push origin watchdog  # con el commit en local ya se puede hacer el merge y subirlo directamente a dev

# Merge dev
git checkout dev
git pull origin dev
git merge watchdog
git push origin dev

# Eliminacion de rama y creación de nueva rama de trabajo
git branch -D watchdog
git push origin :watchdog
git checkout -b watchdog
git push origin watchdog
```




