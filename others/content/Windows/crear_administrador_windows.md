Title: Crar administrador por consola
Date: 2015-09-10 13:11
Modified: 2015-09-10 13:11
Category: Windows
Tags: windows, consola
Slug: crear_administrador_windows
Authors: procamora
Summary:

## Para crear un usuario administrador a través de la consola:

###### 1. Creamos un usuario
`net user /add SuperAdmin`

###### 2. Metemos dentro del grupo *Administradores* el usuario creado
`net localgroup administradores SuperAdmin /add`

###### 3. Asignamos una contraseña al usuario creado
`net user SuperAdmin "contraseña"`
