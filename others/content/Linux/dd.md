Title: Uso de dd
Date: 2015-11-8 14:10
Modified: 2015-11-8 14:10
Category: Linux
Tags: linux, dd
Slug: dd
Authors: procamora
Summary:

La orden **dd** hace una copia exacta byte a byte.

Ejemplos:

###### Clonar un disco duro:
`dd if=/dev/sda |pv|dd of=/dev/sdb`


######Clonar una partición:
`dd if=/dev/sdc2 |pv|dd of=/dev/sda1`


######Crear una imagen iso de una partición o disco duro (excelente opción para backups):
`dd if=/dev/sda1 |pv|dd of=/home/usuario/backup.iso`


> En algunas distros puede que pv no venga instalado, así que bastará con instalarlo para poder usar este tip.
