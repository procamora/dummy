Title: Ver puertos abiertos
Date: 2015-10-3 06:51 
Modified: 2015-10-3 06:51
Category: Linux
Tags: linux
Slug: puertos
Authors: procamora
Summary:

`sudo nmap -O localhost | grep "open"`

`sudo fuser -n tcp puerto`

`sudo ps -l PID`

`sudo /etc/init.d/aplicación stop`


######matar a lo burro
`sudo fuser -nk tcp puerto`

`sudo killall servicio`

`sudo kill -9 PID`
