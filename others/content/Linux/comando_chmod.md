---
title: autorun script linux systemd
description: 
date: 
lastmod: 
slug: 
image: "covers/linux.png"
tags:
  - 
categories:
  - Linux
---
Title: Uso de chmod
Date: 2015-11-4 14:24
Modified: 2015-11-4 14:24
Category: Linux
Tags: linux, chmod
Slug: comando_chmod
Authors: procamora
Summary:

######chmod sirve para modificar los permisos de ficheros y directorios

`chmod [opciones] modo[,modo] fichero`

Para ello tenemos que tener claros los distintos grupos de usuarios:
```
u: usuario dueño del fichero
g: grupo de usuarios del dueño del fichero
o: todos los otros usuarios
a: todos los tipos de usuario (dueño, grupo y otros)
```


También hay que saber la letra que abrevia cada tipo de permiso:
```
r: se refiere a los permisos de lectura
w: se refiere a los permisos de escritura
x: se refiere a los permisos de ejecución
```



```
 - - - = 0 no se tiene ningún permiso
 - - x = 1 solo permiso de ejecución
 - w - = 2 solo permiso de escritura
 - w x = 3 permisos de escritura y ejecución
 r - - = 4 solo permiso de lectura
 r - x = 5 permisos de lectura y ejecución
 r w - = 6 permisos de lectura y escritura
 r w x = 7 todos los permisos establecidos, lectura, escritura y ejecución
```
