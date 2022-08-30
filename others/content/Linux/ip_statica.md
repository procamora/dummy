Title: Poner ip statica
Date: 2015-11-10 19:35
Modified: 2015-11-10 19:35
Category: Linux
Tags: linux
Slug: ip_statica
Authors: procamora
Summary:

`vim /etc/network/interfaces`

```
auto eth0
inface eth0 inet static
address 192.168.1.3
netmask 255.255.255.0
gateway 192.168.1.1
```

`/etc/init.d/networking stop && /etc/init.d/networking start`

o

`/etc/init.d/networking restart`
