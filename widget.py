import pygame as pg
import settings
import utils
vec = pg.math.Vector2

class widget(pg.sprite.Sprite):
    def __init__(self, programScene, tl, dimensions, groups = [], txt = ""):
        pg.sprite.Sprite.__init__(self,groups)
        self.scene = programScene
        self.dimensions = dimensions
        self.pos = vec(tl)
        self.text = str(txt)
        self.image = pg.Surface(dimensions)
        self.rect = self.image.get_rect(topleft=tl)
        self.bgColor, self.bdrColor, self.fColour = settings.bgColour, settings.bdrColour, settings.fColour
        self.editText = self.mFollow = False
        self.draw(tl =self.pos)


    def draw(self, tl = None, c = None):
        if tl != None:
            self.pos = tl
        elif c != None:
            self.rect.center = c
            self.pos = self.rect.topleft

        self.image.fill(self.bgColor)
        self.rect = self.image.get_rect(topleft=self.pos)
        pg.draw.rect(self.image, self.fColour, pg.Rect((0,0),self.dimensions), 1)
        self.textSurf = self.scene.state.font.render(self.text, True, self.fColour)
        self.textRect = self.textSurf.get_rect(center = self.rect.center)

    def editor(self):
        keys = self.getKeys()
        for key in keys:
            self.text += key

    def getKeys(self):
        events = []
        if pg.event.peek(pg.KEYDOWN): 
            events = pg.event.get(pg.KEYDOWN)
        return [event.unicode for event in events]
        
    
    def update(self):
        
        # mouse hover #
        if self.rect.collidepoint(self.scene.state.mousePos):
            self.bgColor = settings.GREY 
            # mouse click #
            if self.scene.state.mousePressed[2]:self.mFollow = True
            else: self.mFollow = False
        else: self.bgColor = settings.LGREY
        
        if self.mFollow:
            self.pos = self.scene.state.mousePos
            self.draw(c=self.pos)
        else: self.draw(tl=self.pos)

        if self.editText:
            self.editor()

        
        
        
