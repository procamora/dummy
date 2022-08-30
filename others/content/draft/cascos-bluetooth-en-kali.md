Title: Cascos bluetooth en Kali
Date: 2016-2-23 11:11
Modified: 2016-2-23 11:11
Category: 
Tags: bluetooth, kali
Authors: procamora
Slug: cascos-bluetooth-en-kali
Summary: 
Status: published


## Primeros instalamos la librería para gestionar el bluetooth con pulseaudio

`sudo apt-get install pulseaudio-module-bluetooth` 

Iniciamos el servicio de bluetooth

`/etc/init.d/bluetooth start`


foto



Para poder activarlo en la configuración n hay que activar el modulo
`sudo pactl load-module module-bluetooth-discover`


después vamos a configuración de sonido y establecemos que el sonido salga por el casco en vez de por el altavoz

foto
