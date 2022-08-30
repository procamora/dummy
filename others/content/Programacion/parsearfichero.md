---
Title: Parsear Fichero
Date: 2015-12-13 17:51
Modified: 2015-12-13 17:51
Category: Programacion
Tags: code, python programacion, parser
Slug: parsearfichero
Summary: Para parsear un fichero con python y remplazar ciertos ficheros el código seria algo como este.
Status: published
---




Para parsear un fichero con python y remplazar ciertos ficheros el código seria algo como este.


```python
TEMPLATE = """Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Modified: {year}-{month}-{day} {hour}:{minute:02d}
Category:
Tags:
Slug: {slug}
Summary:
Status: draft
"""

t = TEMPLATE.strip().format(title=title,
							year=today.year,
							month=today.month,
							day=today.day,
							hour=today.hour,
							minute=today.minute,
							slug=slug)

f_create = 	"fichero.txt"
with open(f_create, 'w') as w:
	w.write(t)
print("File created -> " + f_create)
```


