Title: Cambiar monitor guake
Date: 2016-1-9 17:50
Modified: 2016-1-11 17:50
Category: Linux
Tags: linux, software, guake
Authors: procamora
Slug: 2016_01_09_cambiar-monitor-guake
Summary: Cuando tienes varios monitores, guake por defecto arranca en el monitor de la izquierda, para colocarlo en la derecha hay que editar el ejecutable de guake
Status: published

Cuando tienes varios monitores, guake por defecto arranca en el monitor de la izquierda, para colocarlo en la derecha hay que editar el ejecutable de guake

`vim /usr/bin/guake`


Buscar la función  ***get_final_window_rect*** y sustituirla por esta:


```python
    def get_final_window_rect(self):
        """Gets the final size of the main window of guake. The height
        is the window_height property, width is window_width and the
        horizontal alignment is given by window_alignment.
        """
        screen = self.window.get_screen()
        height = self.client.get_int(KEY('/general/window_height'))
        width = 100
        halignment = self.client.get_int(KEY('/general/window_halignment'))

        # future we might create a field to select which monitor you
        # wanna use
        #monitor = 0 # use the left most monitor
        monitor = screen.get_n_monitors() - 1 # use the right most monitor

        monitor_rect = screen.get_monitor_geometry(monitor)
        window_rect = monitor_rect.copy()
        window_rect.height = window_rect.height * height / 100
        window_rect.width = window_rect.width * width / 100

        if width < monitor_rect.width:
            if halignment == ALIGN_CENTER:
                window_rect.x = monitor_rect.x + (monitor_rect.width - window_rect.width) / 2
            elif halignment == ALIGN_LEFT:
                window_rect.x = monitor_rect.x
            elif halignment == ALIGN_RIGHT:
                window_rect.x = monitor_rect.x + monitor_rect.width - window_rect.width

        window_rect.y = monitor_rect.y
        return window_rect
```

Fuentes: [0][0]

[0]: http://www.marcogiordanotd.com/blog/ubuntu/fix-guake-terminal-position-multi-monitor
