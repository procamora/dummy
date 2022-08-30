---
Title: Reducir tamaño repositorio git
Date: 2019-4-27 15:33
Modified: 2019-4-27 15:33
Category: Software
Tags: git
Authors: procamora
Slug: reducir-tamano-repositorio-git
Summary: Para comprimir el tamaño de un repositorio git podemos usar los siguientes comandos:
Status: published
---



Para comprimir un repositorio git y reducir su tamaño podemos usar los siguientes comandos:


```bash
git reflog expire --all --expire=now
git gc --prune=now --aggressive
```



Fuente: [0][sf1]

[sf1]: https://stackoverflow.com/questions/2116778/reduce-git-repository-size