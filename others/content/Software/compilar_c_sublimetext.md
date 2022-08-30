﻿Title: Compilar C con Sublimetext 2
Date: 2015-12-17 2:46
Modified: 2015-12-17 2:46
Category: Software
Tags: software, sublimetext, c
Authors: procamora
Slug: compilar_c_sublimetext
Summary:En esta entrada veremos como configurar Sublime Text 2 para que al presionar ctrl + b se compile y ejecute nuestra aplicación en C.
Status: published


En esta entrada veremos como configurar Sublime Text 2 para que al presionar **ctrl + b** se compile y ejecute nuestra aplicación en C.

Lo primero que debemos hacer es iniciar Sublime Text, una vez lo hallamos hecho, vamos a `Tools -> Build System -> New Build System`... Esto abrirá un pequeño archivo con unas lineas escritas en JSON, de modo que debemos copiar el siguiente código y pegarlo en este archivo.

En mi caso la ruta es: `%AppData%\Sublime Text 2\Packages\User`

```json
//Windows
{
	"cmd" : ["gcc", "-Wall", "$file_name", "-o", "${file_base_name}.exe", "&&", "${file_base_name}.exe"],
	"selector" : "source.c",
	"shell" : true,
	"working_dir" : "$file_path"
}

//Linux
{
	"cmd" : ["gcc", "-Wall", "$file_name", "-o", "${file_base_name}", "&&", "${file_base_name}"],
	"selector" : "source.c",
	"shell" : true,
	"working_dir" : "$file_path"
}
```

Cuando lo hallamos hecho, guardamos dicho archivo en la carpeta donde nos sugiere Sublime Text, y le ponemos un nombre descriptivo como por ejemplo C.sublime-build, **ten cuidado que la extensión del archivo sea .sublime-build.**

Y con eso ya hemos terminado, para compilar y ejecutar nuestros programas en C tan solo debes ir a `Tools -> Build System` y elegir el nombre del archivo que has modificado ante.,

Fuentes: [1][0]



[0]: http://ayudasprogramacionweb.blogspot.com.es/2013/03/compilar-y-ejecutar-c-en-terminal-linux-sublime-text.html