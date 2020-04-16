import pygame as pg
import widget
import settings

class textbox(widget.widget):
    def __init__(self, programScene, tl, dimensions, txt = ""):
        self.groups = programScene.objects.groupAll, programScene.objects.groupTextBoxes
        super().__init__(programScene, tl, dimensions, self.groups, txt)
        self.type = "textbox"
        self.textLocked, self.posLocked = False, False

class inputbox(widget.widget):
    def __init__(self, programScene, tl, dimensions, txt = "",q = ": "):
        self.groups = programScene.objects.groupAll, programScene.objects.groupInputBoxes
        self.question = q
        self.answer = ""
        super().__init__(programScene, tl, dimensions, self.groups, q)
        self.text = self.question + self.answer
        self.type = "inputbox"
        self.textLocked, self.posLocked, self.widthLocked = False, False, False
    
    def update(self):
        self.text = self.question + self.answer
        super().update()

class button(widget.widget):
    def __init__(self, programScene, tl, dimensions, txt = ""):
        self.groups = programScene.objects.groupAll, programScene.objects.groupButtons
        super().__init__(programScene, tl, dimensions, self.groups, txt)
        self.type = "button"
        self.textLocked = True
        self.posLocked = False
    
    def buttonFunc(self):
        print("heheheh")
