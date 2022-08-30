Title: Script sacar ip linux
Date: 2015-10-9 18:51
Modified: 2015-10-9 18:51 
Category: Linux
Tags: linux, consola
Slug: ip
Authors: procamora
Summary:

`ifconfig eth0 | awk '/inet addr/ {split ($2,A,":"); print A[2]}'`
