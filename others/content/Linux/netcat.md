Title: Crear chat con netcat
Date: 2015-10-8 01:51
Modified: 2015-10-8 01:51
Category: Linux
Tags: linux, netcat, network
Slug: netcat
Authors: procamora
Summary:

## Para hacer un chat entre ordenadores en una red local

###### Servidor

`nc -l -p 6698`


###### Cliente

`nc ip-server 6698`


> Importante: La conversación se manda por paquetes tcp sin cifrar, por lo que con un sniffer(wireshark) en la red local se pueden leer los paquetes
