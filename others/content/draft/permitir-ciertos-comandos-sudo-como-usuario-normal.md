---
Title: Permitir ciertos comandos sudo como usuario normal
Date: 2016-4-20 12:54
Modified: 2016-4-20 12:54
Category: Linux
Tags: sudo 
Authors: procamora
Slug: permitir-ciertos-comandos-sudo-como-usuario-normal
Summary:
Status: published
---



```
llows members of the users group to mount and unmount the
## cdrom as root
%users  ALL=/sbin/mount /mnt/cdrom, /sbin/umount /mnt/cdrom
```

http://www.cyberciti.biz/tips/allow-a-normal-user-to-run-commands-as-root.html
