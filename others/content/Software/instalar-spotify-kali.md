Title: Instalar spotify en kali
Date: 2016-1-31 19:06
Modified: 2016-1-31 19:06
Category: Software
Tags: linux, spotify, kali
Authors: procamora
Slug: instalar-spotify-kali
Summary: Descargar paquete de spotify de su repositorio oficial, o del directorio de descargas
Status: published



Descargar paquete de spotify de su [repositorio oficial][0], o del directorio de [descargas][1]

Una vez descargado instalarlo con dpkg

`dpkg -i Descargas/spotify-client-0.9.17_0.9.17.8.gd06432d.31-1_amd64.deb`


<br />
***Precaución***

No hacerlo de modo gráfico ya que se queda colgado a mitad de la instalación, instalar con dpkg


En kali me da este error

`spotify: error while loading shared libraries: libgcrypt.so.11: 
cannot open shared object file: No such file or directory `

Se soluciona instalando la librería libgcrypt11, puedes descargarla desde su repositorio [oficial][2] o del directorio de [descargas][3]

Una vez descargado ejecutar:

`dpkg -i libgcrypt11_1.5.0-5+deb7u1_amd64.deb`

[0]: http://repository.spotify.com/pool/non-free/s/spotify/ "repositorio spotify"
[1]: /../descargas/spotify-client-0.9.17_0.9.17.8.gd06432d.31-1_amd64.deb
[repositorio]: http://repository.spotify.com/pool/non-free/s/spotify/
[2]: https://packages.debian.org/wheezy/libgcrypt11
[3]: /../descargas/libgcrypt11_1.5.0-5+deb7u3_amd64.deb
