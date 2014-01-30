#!/usr/bin/python2

import os
import urllib

from gi.repository import Nautilus, GObject

class OpenExFalsoExtension(GObject.GObject, Nautilus.MenuProvider):
    def _open_exfalso(self, file):
        filename = urllib.unquote(file.get_uri()[7:])
        
        os.spawnlp(os.P_NOWAIT, '/usr/bin/exfalso', '/usr/bin/exfalso', filename)

    def menu_activate_cb(self, menu, file):
        self._open_exfalso(file)

    def menu_background_activate_cb(self, menu, file):
        self._open_exfalso(file)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]

        if not file.is_directory() or file.get_uri_scheme() != 'file':
            return

        item = Nautilus.MenuItem(name='NautilusPython::openexfalso_file_item', label='Open in Ex Falso', tip='Open Ex Falso in %s' % file.get_name())
        item.connect('activate', self.menu_activate_cb, file)
        return item,

    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='NautilusPython::openexfalso_item',
                                 label='Open in Ex Falso',
                                 tip='Open Ex Falso In %s' % file.get_name())
        item.connect('activate', self.menu_background_activate_cb, file)
        return item,


