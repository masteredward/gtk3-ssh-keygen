#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import run
from os import path

class GridWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
		
        grid = Gtk.Grid()
        self.add(grid)
		
        label_kname = Gtk.Label(label="Enter Private Key Name:")
        global entry_kname
        entry_kname = Gtk.Entry()
        
        label_kpass = Gtk.Label(label="Enter Private Key Pass:")
        global entry_kpass
        entry_kpass = Gtk.Entry()
        
        label_kcomment = Gtk.Label(label="Enter Public Key Comment:")
        global entry_kcomment
        entry_kcomment = Gtk.Entry()
        button_kgen = Gtk.Button(label="Generate Key Pair")
        button_kgen.connect("clicked", self.on_kgen_clicked)
        
        grid.add(label_kname)
        grid.attach_next_to(entry_kname, label_kname, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(label_kpass, entry_kname, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(entry_kpass, label_kpass, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(label_kcomment, entry_kpass, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(entry_kcomment, label_kcomment, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(button_kgen, entry_kcomment, Gtk.PositionType.BOTTOM, 1, 1)
        
    def on_kgen_clicked(self, button_kgen):
        run(["mkdir", "-p", path.expanduser("~/.ssh")])
        run(["ssh-keygen", "-f", path.expanduser("~/.ssh/")+entry_kname.get_text(), "-C", entry_kcomment.get_text(), "-N", entry_kpass.get_text()])
        Gtk.main_quit()

win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
