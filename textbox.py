import pygame as pg
import widget
import settings

class textbox(widget.widget):
    def __init__(self, programScene, tl, dimensions, txt = ""):
        self.groups = programScene.objects.groupAll
        super().__init__(programScene, tl, dimensions, self.groups, txt)
        