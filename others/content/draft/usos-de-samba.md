Title: Usos de samba
Date: 2016-4-22 1:22
Modified: 2016-4-22 1:22
Category: 
Tags: 
Authors: procamora
Slug: usos-de-samba
Summary: 
Status: draft






###Crear usuario
`sudo useradd -s /bin/true username`


###Asignarle contraseña
```
sudo smbpasswd -L -a username
sudo smbpasswd -L -e username
```



###Listar usuarios samba
```
sudo pdbedit -L -v
```


testparm /etc/samba/smb.conf















