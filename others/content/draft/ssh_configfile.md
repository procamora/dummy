Title: ssh_configfile
Date: 2015-12-20 18:30
Modified: 2015-12-20 18:30
Category:
Tags:
Slug: ssh_configfile
Summary:
Status: published



.ssh/config

```
Host github.com
    User git
    HostName github.com
    IdentityFile ~/.ssh/github.project1.key
    
Host bitbucket.org
    User git
    HostName bitbucket.org
    IdentityFile ~/.ssh/github.org.key
    
Host github.com
    User git
    IdentityFile ~/.ssh/github.key
```


http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/
